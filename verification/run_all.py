#!/usr/bin/env python3
"""Finite consistency checks for F1, S1, C1, C2, lattice applications, and preparation.

Every source matrix is built by enumerating actual label tables. No test is an
asymptotic proof or a check of a lattice-hardness assumption. Only NumPy is needed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import time
import traceback

import numpy as np

TOL = 5e-10
SEED = 20261024


def hermitian(x):
    return (x + x.conj().T) / 2


def eigs(x):
    return np.linalg.eigvalsh(hermitian(x))


def distance(x, y):
    return float(np.abs(eigs(x - y)).sum() / 2)


def entropy(x):
    values = eigs(x)
    if values.min(initial=0.0) < -TOL:
        raise ValueError("Entropy requested for a matrix with a negative eigenvalue.")
    positive = values[values > 1e-14]
    return float(-(positive * np.log2(positive)).sum())


def binary_entropy(c):
    return float(sum(-x * math.log2(x) for x in (c, 1-c) if x > 0))


def ket_density(v):
    return np.outer(v, v.conj())


def tensor_power(v, copies):
    result = np.array([1.0], dtype=complex)
    for _ in range(copies):
        result = np.kron(result, v)
    return result


def tensor_matrices(matrices):
    result = np.array([[1.0]], dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def flatten_index(entries, base):
    result = 0
    for entry in entries:
        result = result * base + int(entry)
    return result


class Case:
    def __init__(self, name, theorem, purpose):
        self.name = name
        self.theorem = theorem
        self.purpose = purpose
        self.metrics = {}
        self.checks = []

    def metric(self, name, value):
        if isinstance(value, np.generic):
            value = value.item()
        self.metrics[name] = value

    def near(self, name, actual, expected=0.0, tolerance=TOL):
        error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
        self.checks.append({
            "name": name, "passed": bool(error <= tolerance),
            "absolute_error": error, "tolerance": tolerance,
        })

    def at_most(self, name, value, bound, tolerance=TOL):
        self.checks.append({
            "name": name, "passed": bool(value <= bound + tolerance),
            "value": float(value), "upper_bound": float(bound),
            "tolerance": tolerance,
        })

    def at_least(self, name, value, bound, tolerance=TOL):
        self.checks.append({
            "name": name, "passed": bool(value >= bound - tolerance),
            "value": float(value), "lower_bound": float(bound),
            "tolerance": tolerance,
        })

    def state(self, name, rho, trace=1.0):
        self.near(name + "_Hermiticity", np.linalg.norm(rho-rho.conj().T))
        self.near(name + "_trace", np.trace(rho), trace)
        self.at_least(name + "_minimum_eigenvalue", float(eigs(rho).min()), 0.0)

    def result(self):
        return {
            "name": self.name, "theorem": self.theorem, "purpose": self.purpose,
            "passed": all(check["passed"] for check in self.checks),
            "metrics": self.metrics, "checks": self.checks,
        }


def table_ensemble(p, conditional):
    """Enumerate the independent table law before forming any density matrix."""
    p = np.asarray(p, dtype=float)
    conditional = np.asarray(conditional, dtype=float)
    n, k = conditional.shape
    if p.shape != (n,) or abs(p.sum()-1) > TOL:
        raise ValueError("Invalid input law.")
    if np.min(p) < 0 or np.min(conditional) < 0:
        raise ValueError("Negative probability.")
    if np.max(np.abs(conditional.sum(axis=1)-1)) > TOL:
        raise ValueError("Invalid conditional law.")
    ensemble = []
    for labels in itertools.product(range(k), repeat=n):
        weight = float(np.prod([conditional[a, labels[a]] for a in range(n)]))
        if weight == 0:
            continue
        vector = np.zeros(n*k, dtype=complex)
        for a, y in enumerate(labels):
            vector[a*k+y] = math.sqrt(p[a])
        ensemble.append((labels, weight, vector))
    return ensemble


def moment(ensemble, copies):
    dim = ensemble[0][2].size ** copies
    rho = np.zeros((dim, dim), dtype=complex)
    for _, weight, vector in ensemble:
        rho += weight * ket_density(tensor_power(vector, copies))
    return rho


def conditional_shifts(chi, shifts):
    chi = np.asarray(chi, dtype=float)
    return np.stack([np.roll(chi, int(s)) for s in shifts])


def positive_secular_root(r):
    positive = np.asarray(r)[np.asarray(r) > 0]
    if positive.size <= 1:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo+hi)/2
        if np.sum(positive/(positive+mid)) > 1:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def fresh_case(name, p, conditional):
    case = Case(name, "F1", "Compare explicit label-table averaging with the full nonuniform spectrum.")
    p = np.asarray(p, dtype=float)
    conditional = np.asarray(conditional, dtype=float)
    n, k = conditional.shape
    ensemble = table_ensemble(p, conditional)
    rho = moment(ensemble, 1)
    classical = np.diag((p[:, None]*conditional).reshape(-1)).astype(complex)
    c_a = np.sum(conditional**2, axis=1)
    cbar = float(p @ c_a)
    r = p*c_a/cbar
    small = np.outer(np.sqrt(r), np.sqrt(r))-np.diag(r)
    predicted_spectrum = np.sort(np.concatenate((cbar*eigs(small), np.zeros(n*k-n))))
    case.state("enumerated_source", rho)
    case.state("classical_encoding", classical)
    case.near("difference_entire_spectrum", eigs(rho-classical), predicted_spectrum)
    lam = positive_secular_root(r)
    actual = distance(rho, classical)
    case.near("distance_secular_root", actual, cbar*lam)
    case.at_most("distance_collision_bound", actual, cbar)
    case.at_least("distance_Rayleigh_bound", actual, cbar*(1-float(r @ r)))
    case.at_most("distance_fidelity_bound", actual, cbar*math.sqrt(max(0, 1-float(r @ r))))
    for a in range(n):
        mu = conditional[a].astype(complex)
        covariance = np.zeros((k, k), dtype=complex)
        for y in range(k):
            centered = np.eye(k, dtype=complex)[:, y]-mu
            covariance += conditional[a, y]*ket_density(centered)
        formula = np.diag(conditional[a])-ket_density(mu)
        case.near(f"label_covariance_{a}", covariance, formula)
        case.at_least(f"label_covariance_{a}_PSD", float(eigs(covariance).min()), 0)
        case.near(f"label_covariance_{a}_trace", np.trace(covariance), 1-c_a[a])
    if np.max(np.abs(p-1/n)) < TOL and np.max(np.abs(c_a-c_a[0])) < TOL:
        case.near("uniform_exact_distance", actual, c_a[0]*(1-1/n))
    case.metric("N", n)
    case.metric("label_dimension", k)
    case.metric("tables_enumerated", len(ensemble))
    case.metric("input_collision_alpha", float(p @ p))
    case.metric("average_label_collision_cbar", cbar)
    case.metric("trace_distance", actual)
    case.metric("positive_eigenvalue_lambda", lam)
    return case


def symmetrize_record(indices, n, k):
    copies = len(indices)
    vector = np.zeros((n*k)**copies, dtype=complex)
    for permutation in itertools.permutations(range(copies)):
        output = [indices[j] for j in permutation]
        vector[flatten_index(output, n*k)] += 1/math.sqrt(math.factorial(copies))
    return vector


def symmetrization_isometry(addresses, n, k):
    """Acts on arbitrary, possibly entangled, quantum label inputs."""
    copies = len(addresses)
    if len(set(addresses)) != copies:
        raise ValueError("Distinct addresses are required.")
    result = np.zeros(((n*k)**copies, k**copies), dtype=complex)
    for labels in itertools.product(range(k), repeat=copies):
        record = [addresses[j]*k+labels[j] for j in range(copies)]
        result[:, flatten_index(labels, k)] = symmetrize_record(record, n, k)
    return result


def classical_simulator(p, conditional, copies):
    """Exactly T iid classical records; fixed pure fallback on any repeated address."""
    n, k = conditional.shape
    one_record_law = (p[:, None]*conditional).reshape(-1)
    dim = (n*k)**copies
    sigma = np.zeros((dim, dim), dtype=complex)
    distinct_part = np.zeros_like(sigma)
    duplicate_probability = 0.0
    for record in itertools.product(range(n*k), repeat=copies):
        weight = float(np.prod([one_record_law[index] for index in record]))
        if weight == 0:
            continue
        addresses = [index//k for index in record]
        if len(set(addresses)) != copies:
            duplicate_probability += weight
            sigma[0, 0] += weight
        else:
            vector = symmetrize_record(record, n, k)
            block = weight*ket_density(vector)
            sigma += block
            distinct_part += block
    return sigma, distinct_part, duplicate_probability


def static_case(name, p, conditional, copies):
    case = Case(name, "S1", "Check the global orthogonal core and the exact-T classical-record simulator.")
    p = np.asarray(p, dtype=float)
    conditional = np.asarray(conditional, dtype=float)
    n, k = conditional.shape
    ensemble = table_ensemble(p, conditional)
    dim = (n*k)**copies
    mean = sum(weight*vector for _, weight, vector in ensemble)
    tuples = list(itertools.product(range(n*k), repeat=copies))
    mask = np.array([len({index//k for index in row}) == copies for row in tuples])
    omega = np.zeros((dim, dim), dtype=complex)
    core = np.zeros_like(omega)
    cross = np.zeros_like(omega)
    remainder = np.zeros_like(omega)
    for _, weight, vector in ensemble:
        full = tensor_power(vector, copies)
        v = tensor_power(vector-mean, copies)*mask
        w = full-v
        omega += weight*ket_density(full)
        core += weight*ket_density(v)
        cross += weight*np.outer(v, w.conj())
        remainder += weight*ket_density(w)
    sigma, distinct_part, duplicate_probability = classical_simulator(p, conditional, copies)
    covariances = [np.diag(row)-np.outer(row, row) for row in conditional]
    c_a = np.sum(conditional**2, axis=1)
    w_T = 0.0
    distinct_probability = 0.0
    core_from_covariances = np.zeros_like(core)
    isometry_residual = 0.0
    for addresses in itertools.permutations(range(n), copies):
        input_weight = float(np.prod([p[a] for a in addresses]))
        distinct_probability += input_weight
        w_T += input_weight*float(np.prod([1-c_a[a] for a in addresses]))
        sym = symmetrization_isometry(addresses, n, k)
        isometry_residual = max(isometry_residual, float(np.linalg.norm(sym.conj().T @ sym-np.eye(k**copies))))
        core_from_covariances += input_weight*(sym @ tensor_matrices([covariances[a] for a in addresses]) @ sym.conj().T)
    case.state("frozen_moment", omega)
    case.state("exact_T_simulator", sigma)
    case.near("unconditional_cross_term_zero", np.linalg.norm(cross))
    case.near("global_orthogonal_decomposition", omega, core+remainder)
    case.near("centered_core_covariance_construction", core, core_from_covariances)
    case.near("core_trace_w_T", np.trace(core), w_T)
    case.at_least("core_PSD", float(eigs(core).min()), 0)
    case.at_least("frozen_minus_core_PSD", float(eigs(omega-core).min()), 0)
    case.at_least("simulator_minus_core_PSD", float(eigs(sigma-core).min()), 0)
    case.at_least("distinct_simulator_part_minus_core_PSD", float(eigs(distinct_part-core).min()), 0)
    case.near("quantum_label_symmetrization_isometry", isometry_residual)
    case.near("exact_T_collision_probability", duplicate_probability, 1-distinct_probability)
    actual = distance(omega, sigma)
    cbar, alpha = float(p @ c_a), float(p @ p)
    simple_bound = copies*cbar+math.comb(copies, 2)*alpha
    case.at_most("distance_common_core_bound", actual, 1-w_T)
    case.at_most("common_core_union_bound", 1-w_T, simple_bound)
    if np.max(np.abs(p-1/n)) < TOL and np.max(np.abs(c_a-c_a[0])) < TOL:
        falling = math.perm(n, copies)/n**copies if copies <= n else 0.0
        case.near("uniform_core_closed_form", w_T, falling*(1-c_a[0])**copies)
    if copies > np.count_nonzero(p):
        case.near("excess_copies_zero_core", w_T, 0)
        case.near("excess_copies_all_fallback", duplicate_probability, 1)
    case.metric("N", n)
    case.metric("label_dimension", k)
    case.metric("copies_T", copies)
    case.metric("matrix_dimension", dim)
    case.metric("tables_enumerated", len(ensemble))
    case.metric("input_collision_alpha", alpha)
    case.metric("average_label_collision_cbar", cbar)
    case.metric("distinct_address_probability", distinct_probability)
    case.metric("common_core_weight_w_T", w_T)
    case.metric("actual_trace_distance", actual)
    case.metric("exact_common_core_bound", 1-w_T)
    case.metric("union_bound", simple_bound)
    return case


def fresh_frozen_case():
    case = Case("fresh_frozen_swap_control", "F1/S1", "Detect the erroneous replacement of frozen specimens by independent one-copy averages.")
    n, k = 4, 2
    p = np.full(n, 1/n)
    conditional = np.full((n, k), 1/k)
    ensemble = table_ensemble(p, conditional)
    rho = moment(ensemble, 1)
    frozen = moment(ensemble, 2)
    refreshed = np.kron(rho, rho)
    sigma, _, _ = classical_simulator(p, conditional, 2)
    def swap_expectation(state):
        return float(np.einsum("ijji->", state.reshape(n*k, n*k, n*k, n*k)).real)
    frozen_swap = swap_expectation(frozen)
    refreshed_swap = swap_expectation(refreshed)
    simulator_swap = swap_expectation(sigma)
    purity = float(np.trace(rho @ rho).real)
    case.near("frozen_SWAP_expectation", frozen_swap, 1)
    case.near("refreshed_SWAP_equals_purity", refreshed_swap, purity)
    case.near("symmetrized_simulator_SWAP_expectation", simulator_swap, 1)
    case.at_least("fresh_frozen_operational_separation", (frozen_swap-refreshed_swap)/2, 0.1)
    case.metric("frozen_SWAP_acceptance", (1+frozen_swap)/2)
    case.metric("refreshed_SWAP_acceptance", (1+refreshed_swap)/2)
    case.metric("simulator_SWAP_acceptance", (1+simulator_swap)/2)
    case.metric("one_copy_purity", purity)
    return case


def table_isometries(conditional):
    n, k = conditional.shape
    ensemble = table_ensemble(np.full(n, 1/n), conditional)
    result = []
    for labels, weight, _ in ensemble:
        isometry = np.zeros((n*k, n), dtype=complex)
        for a, y in enumerate(labels):
            isometry[a*k+y, a] = 1
        result.append((weight, isometry))
    return result


def apply_channel(rho, isometries, reference_dimension=1):
    output_dim = isometries[0][1].shape[0]*reference_dimension
    result = np.zeros((output_dim, output_dim), dtype=complex)
    for weight, isometry in isometries:
        extended = np.kron(np.eye(reference_dimension), isometry)
        result += weight*(extended @ rho @ extended.conj().T)
    return result


def dephase_address(rho, n):
    addresses = np.arange(rho.shape[0]) % n
    return rho*(addresses[:, None] == addresses[None, :])


def random_density(n, rng):
    matrix = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))
    result = matrix @ matrix.conj().T
    return result/np.trace(result)


def purification(rho):
    values, vectors = np.linalg.eigh(hermitian(rho))
    root = (vectors*np.sqrt(np.maximum(values, 0))) @ vectors.conj().T
    return root.T.reshape(-1)


def channel_case(name, n, chi, shifts):
    case = Case(name, "C1/C2", "Enumerate channel isometries; check references, Choi blocks, covariance, and coherent information.")
    chi = np.asarray(chi, dtype=float)
    k = chi.size
    conditional = conditional_shifts(chi, shifts)
    isometries = table_isometries(conditional)
    c = float(chi @ chi)
    expected_half_diamond = c*(1-1/n)
    w = np.zeros((n*k, n), dtype=complex)
    for a in range(n):
        w[a*k:(a+1)*k, a] = conditional[a]/math.sqrt(c)
    plus = np.ones(n, dtype=complex)/math.sqrt(n)
    plus_rho = ket_density(plus)
    difference = apply_channel(plus_rho, isometries)-apply_channel(dephase_address(plus_rho, n), isometries)
    case.near("C1_uniform_input_attains_bound", float(np.abs(eigs(difference)).sum()/2), expected_half_diamond)
    maximally_entangled = np.eye(n).reshape(-1)/math.sqrt(n)
    choi = apply_channel(ket_density(maximally_entangled), isometries, n)
    measured_choi = apply_channel(dephase_address(ket_density(maximally_entangled), n), isometries, n)
    case.near("C1_maximally_entangled_input_attains_bound", distance(choi, measured_choi), expected_half_diamond)
    rng = np.random.default_rng(SEED+n+k)
    worst_reference_distance = 0.0
    for index in range(4):
        input_state = random_density(n*n, rng)
        actual = apply_channel(input_state, isometries, n)-apply_channel(dephase_address(input_state, n), isometries, n)
        extended_w = np.kron(np.eye(n), w)
        expected = c*(extended_w @ (input_state-dephase_address(input_state, n)) @ extended_w.conj().T)
        case.near(f"C1_reference_operator_identity_{index}", actual, expected)
        d = float(np.abs(eigs(actual)).sum()/2)
        worst_reference_distance = max(worst_reference_distance, d)
        case.at_most(f"C1_reference_distance_bound_{index}", d, expected_half_diamond)
    tau = np.diag(chi)
    a_matrix = tau-np.outer(chi, chi)
    b_matrix = (tau+(n-1)*np.outer(chi, chi))/n
    block_spectrum = np.concatenate((eigs(b_matrix), np.tile(eigs(a_matrix/n), n-1), np.zeros(n*n*k-n*k)))
    case.state("normalized_Choi", choi)
    case.near("C2_full_Choi_spectrum", eigs(choi), np.sort(block_spectrum))
    uniform = np.eye(n)/n
    uniform_output = apply_channel(uniform, isometries)
    capacity_by_enumeration = entropy(uniform_output)-entropy(choi)
    capacity_formula = math.log2(n)+entropy(tau)-entropy(b_matrix)-(n-1)*entropy(a_matrix/n)
    case.near("C2_capacity_formula", capacity_by_enumeration, capacity_formula)
    lower = max(0.0, c*math.log2(n)-binary_entropy(c))
    upper = c*math.log2(n)
    case.at_least("C2_flagged_lower_bound", capacity_by_enumeration, lower)
    case.at_most("C2_flagged_upper_bound", capacity_by_enumeration, upper)
    positive = chi[chi > 0]
    if np.max(np.abs(positive-1/positive.size)) < TOL:
        case.near("C2_uniform_support_capacity", capacity_by_enumeration, math.log2(n)/positive.size)
    max_sampled_ci = -float("inf")
    for index in range(8):
        input_state = random_density(n, rng)
        output = apply_channel(input_state, isometries)
        joint = apply_channel(ket_density(purification(input_state)), isometries, n)
        ci = entropy(output)-entropy(joint)
        max_sampled_ci = max(max_sampled_ci, ci)
        case.at_most(f"C2_sampled_input_below_uniform_{index}", ci, capacity_by_enumeration)
    pure_input = ket_density(plus)
    pure_joint = apply_channel(ket_density(purification(pure_input)), isometries, n)
    case.near("C2_pure_input_zero_coherent_information", entropy(apply_channel(pure_input, isometries))-entropy(pure_joint), 0)
    # Expose the coherent/measurement branch flag and check the entropy cost.
    flag_input = random_density(n, rng)
    flag_purification = ket_density(purification(flag_input))
    ordinary_output = apply_channel(flag_input, isometries)
    ordinary_joint = apply_channel(flag_purification, isometries, n)
    coherent_output = c*(w @ flag_input @ w.conj().T)
    extended_w = np.kron(np.eye(n), w)
    coherent_joint = c*(extended_w @ flag_purification @ extended_w.conj().T)
    residual_output = ordinary_output-coherent_output
    residual_joint = ordinary_joint-coherent_joint
    flagged_output = np.block([[coherent_output, np.zeros_like(coherent_output)], [np.zeros_like(coherent_output), residual_output]])
    flagged_joint = np.block([[coherent_joint, np.zeros_like(coherent_joint)], [np.zeros_like(coherent_joint), residual_joint]])
    flagged_ci = entropy(flagged_output)-entropy(flagged_joint)
    ordinary_ci = entropy(ordinary_output)-entropy(ordinary_joint)
    case.at_least("C2_flagged_residual_joint_PSD", float(eigs(residual_joint).min()), 0)
    case.near("C2_flagged_coherent_information", flagged_ci, c*entropy(flag_input))
    case.at_least("C2_forgetting_flag_CI_loss_nonnegative", flagged_ci-ordinary_ci, 0)
    case.at_most("C2_forgetting_flag_CI_loss_bounded_by_binary_entropy", flagged_ci-ordinary_ci, binary_entropy(c))
    undo = np.zeros((n*k, n*k))
    for a in range(n):
        for y in range(k):
            undo[a*k+(y-int(shifts[a])) % k, a*k+y] = 1
    test_input = random_density(n, rng)
    zero_isometries = table_isometries(np.tile(chi, (n, 1)))
    case.near("known_f_output_unitary_equivalence", undo @ apply_channel(test_input, isometries) @ undo.T, apply_channel(test_input, zero_isometries))
    # A common error on all branches is a different, fully coherent channel.
    common_output = np.zeros((n*k, n*k), dtype=complex)
    for error in range(k):
        common_v = np.zeros((n*k, n))
        for address in range(n):
            common_v[address*k+(int(shifts[address])+error) % k, address] = 1
        common_output += chi[error]*(common_v @ test_input @ common_v.T)
    case.near("common_shift_is_identity_tensor_noise_after_undo", undo @ common_output @ undo.T, np.kron(test_input, tau))
    case.metric("N", n)
    case.metric("label_dimension", k)
    case.metric("tables_enumerated", len(isometries))
    case.metric("collision_c", c)
    case.metric("half_diamond_formula", expected_half_diamond)
    case.metric("largest_sampled_reference_distance", worst_reference_distance)
    case.metric("capacity_from_explicit_Choi_qubits_per_use", capacity_by_enumeration)
    case.metric("capacity_closed_formula", capacity_formula)
    case.metric("flagged_lower_bound", lower)
    case.metric("flagged_upper_bound", upper)
    case.metric("largest_of_eight_sampled_input_coherent_informations", max_sampled_ci)
    return case


def degradability_case():
    case = Case("explicit_Stinespring_degradability", "C2", "Construct the environment explicitly and reproduce it by measuring the retained output address.")
    conditional = conditional_shifts([0.7, 0.3], [0, 1, 0])
    n, k = conditional.shape
    isometries = table_isometries(conditional)
    bdim, edim = n*k, len(isometries)
    stinespring = np.zeros((bdim, edim, n), dtype=complex)
    for e, (weight, isometry) in enumerate(isometries):
        stinespring[:, e, :] = math.sqrt(weight)*isometry
    flat = stinespring.reshape(bdim*edim, n)
    rng = np.random.default_rng(SEED+99)
    input_state = random_density(n, rng)
    joint = (flat @ input_state @ flat.conj().T).reshape(bdim, edim, bdim, edim)
    output = np.trace(joint, axis1=1, axis2=3)
    environment = np.trace(joint, axis1=0, axis2=2)
    reconstructed = np.zeros((edim, edim), dtype=complex)
    for address in range(n):
        column = stinespring[:, :, address]
        eta = column.T @ column.conj()
        probability = np.trace(output[address*k:(address+1)*k, address*k:(address+1)*k]).real
        reconstructed += probability*eta
    case.near("Stinespring_isometry", flat.conj().T @ flat, np.eye(n))
    case.state("channel_output", output)
    case.state("environment_output", environment)
    case.near("degrading_map_recovers_environment", environment, reconstructed)
    case.near("Stinespring_output_agrees_with_table_channel", output, apply_channel(input_state, isometries))
    case.metric("input_dimension", n)
    case.metric("output_dimension", bdim)
    case.metric("environment_dimension", edim)
    return case


def gf4_multiply(a, b):
    """GF(4)=GF(2)[x]/(x^2+x+1), with elements encoded by two bits."""
    result = 0
    for _ in range(2):
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return result


def gf4_trace(a):
    value = a ^ gf4_multiply(a, a)
    if value not in (0, 1):
        raise ValueError("GF(4) trace did not lie in GF(2).")
    return value


def polynomial_table_histogram(degree):
    histogram = Counter()
    for coefficients in itertools.product(range(4), repeat=degree+1):
        table = []
        for address in range(4):
            value = 0
            for coefficient in reversed(coefficients):
                value = gf4_multiply(value, address) ^ coefficient
            table.append(gf4_trace(value))
        histogram[tuple(table)] += 1
    total = 4**(degree+1)
    return {table: count/total for table, count in histogram.items()}


def histogram_ensemble(histogram):
    ensemble = []
    for labels, weight in histogram.items():
        vector = np.zeros(8, dtype=complex)
        for a, y in enumerate(labels):
            vector[2*a+y] = 0.5
        ensemble.append((labels, weight, vector))
    return ensemble


def finite_hash_case():
    case = Case("finite_hash_moment_order", "F1/S1/P1", "Check pairwise sufficiency for fresh sources and its failure for two frozen copies.")
    pairwise = polynomial_table_histogram(1)
    fourwise = polynomial_table_histogram(3)
    independent = {table: 1/16 for table in itertools.product(range(2), repeat=4)}
    max_pair_marginal_error = 0.0
    for a, b in itertools.combinations(range(4), 2):
        for x, y in itertools.product(range(2), repeat=2):
            probability = sum(weight for table, weight in pairwise.items() if table[a] == x and table[b] == y)
            max_pair_marginal_error = max(max_pair_marginal_error, abs(probability-0.25))
    case.near("affine_GF4_pairwise_label_independence", max_pair_marginal_error)
    case.near("cubic_GF4_fourwise_table_distribution", np.array([fourwise.get(table, 0) for table in independent]), np.full(16, 1/16))
    iid_ensemble = histogram_ensemble(independent)
    pair_ensemble = histogram_ensemble(pairwise)
    four_ensemble = histogram_ensemble(fourwise)
    fresh_gap = distance(moment(iid_ensemble, 1), moment(pair_ensemble, 1))
    frozen_pair_gap = distance(moment(iid_ensemble, 2), moment(pair_ensemble, 2))
    frozen_four_gap = distance(moment(iid_ensemble, 2), moment(four_ensemble, 2))
    case.near("pairwise_hash_exact_one_copy_moment", fresh_gap)
    case.at_least("pairwise_hash_not_enough_for_two_frozen_copies", frozen_pair_gap, 1e-6, tolerance=0)
    case.near("fourwise_hash_exact_two_copy_moment", frozen_four_gap)
    case.metric("pairwise_seed_count", 4**2)
    case.metric("fourwise_seed_count", 4**4)
    case.metric("pairwise_distinct_tables", len(pairwise))
    case.metric("fourwise_distinct_tables", len(fourwise))
    case.metric("one_copy_pairwise_trace_distance", fresh_gap)
    case.metric("two_copy_pairwise_trace_distance", frozen_pair_gap)
    case.metric("two_copy_fourwise_trace_distance", frozen_four_gap)
    return case


def scalar_fourier_case():
    case = Case("scalar_Fourier_and_fixed_table_verification", "L2/GKZ", "Check the scalar positive endpoint on explicit bounded tables, including address-dependent errors.")
    q, n, bound = 17, 2, 1
    addresses = np.array(list(itertools.product(range(q), repeat=n)))
    secret = np.array([2, 5])
    count = q**n
    patterns = [
        np.zeros(count, dtype=int),
        np.ones(count, dtype=int),
        np.where(addresses.sum(axis=1) % 2, 1, -1),
        ((addresses[:, 0]+3*addresses[:, 1]) % 3)-1,
    ]
    correct_probabilities = []
    max_false_pass = []
    for index, errors in enumerate(patterns):
        vector = np.zeros((q,)* (n+1), dtype=complex)
        for a, error in zip(addresses, errors):
            label = int((a @ secret + error) % q)
            vector[tuple(a)+(label,)] = 1/math.sqrt(count)
        # ifftn with orthonormal normalization implements the positive-phase QFT.
        probabilities = np.abs(np.fft.ifftn(vector, norm="ortho"))**2
        success = sum(float(probabilities[tuple((-y*secret) % q)+(y,)])
                      for y in range(1, q//(8*bound)+1))
        case.near(f"table_{index}_QFT_normalization", probabilities.sum(), 1.0)
        case.at_least(f"table_{index}_small_frequency_success", success, 1/(32*bound))
        worst_pass = 0.0
        for difference in addresses[1:]:
            residues = (addresses @ difference + errors) % q
            centered_magnitude = np.minimum(residues, q-residues)
            worst_pass = max(worst_pass, float(np.mean(centered_magnitude <= bound)))
        case.at_most(f"table_{index}_all_wrong_candidates", worst_pass, (4*bound+1)/q)
        correct_probabilities.append(success)
        max_false_pass.append(worst_pass)
    # Independently average all ternary tables for a small exact Fourier law.
    q_small = 3
    chi = np.array([0.5, 0.3, 0.2])
    conditional = conditional_shifts(chi, range(q_small))
    observed = np.zeros((q_small, q_small))
    for _, weight, vector in table_ensemble([1/q_small]*q_small, conditional):
        observed += weight*np.abs(np.fft.ifftn(vector.reshape(q_small, q_small), norm="ortho"))**2
    characteristic = np.fft.ifft(chi)*q_small
    predicted = np.zeros_like(observed)
    for x, y in itertools.product(range(q_small), repeat=2):
        magnitude = float(abs(characteristic[y])**2)
        predicted[x, y] = (1-magnitude)/(q_small*q_small)
        if x == (-y) % q_small:
            predicted[x, y] += magnitude/q_small
    case.near("averaged_Fourier_distribution_from_all_tables", observed, predicted)
    correct_nonzero = sum(observed[(-y) % q_small, y] for y in range(1, q_small))
    collision = float(chi @ chi)
    case.near("averaged_nonzero_candidate_probability", correct_nonzero,
              collision-1/q_small+(1-collision)/q_small)
    case.metric("bounded_table_parameters", {"q": q, "n": n, "B": bound})
    case.metric("small_frequency_success_by_table", correct_probabilities)
    case.metric("worst_false_candidate_pass_by_table", max_false_pass)
    case.metric("averaged_table_count", q_small**q_small)
    return case


def erasure_witness_case():
    case = Case("one_copy_erasure_scope", "E1", "Check the exact one-copy Stinespring obstruction and the two-copy boundary of that witness.")
    tables = [(0, 0), (0, 1), (2, 0)]
    inputs, outputs = [], []
    for table in tables:
        full = np.zeros(8)
        projected = np.zeros(4)
        for a, label in enumerate(table):
            full[4*a+label] = 1/math.sqrt(2)
            projected[2*a+label//2] = 1/math.sqrt(2)
        inputs.append(full)
        outputs.append(projected)
    input_gram = np.array(inputs) @ np.array(inputs).T
    output_gram = np.array(outputs) @ np.array(outputs).T
    one_environment = input_gram / output_gram
    two_environment = input_gram**2 / output_gram
    one_values = np.linalg.eigvalsh(one_environment)
    two_values = np.linalg.eigvalsh(two_environment)
    case.near("full_graph_state_Gram_matrix", input_gram,
              [[1, 0.5, 0.5], [0.5, 1, 0], [0.5, 0, 1]])
    case.near("projected_graph_state_Gram_matrix", output_gram,
              [[1, 1, 0.5], [1, 1, 0.5], [0.5, 0.5, 1]])
    case.near("one_copy_required_environment_spectrum", one_values,
              [1-math.sqrt(5)/2, 1, 1+math.sqrt(5)/2])
    case.at_most("one_copy_required_Gram_is_not_PSD", float(one_values.min()), -1e-3)
    case.near("two_copy_required_environment_spectrum", two_values,
              [1-math.sqrt(5)/4, 1, 1+math.sqrt(5)/4])
    case.at_least("witness_does_not_rule_out_two_copy_conversion", float(two_values.min()), 0)
    case.metric("one_copy_minimum_required_Gram_eigenvalue", float(one_values.min()))
    case.metric("two_copy_minimum_required_Gram_eigenvalue", float(two_values.min()))
    return case


def folded_gaussian_case():
    case = Case("folded_Gaussian_collision_bound", "L3", "Check modular folding and the stated elementary collision estimate at growing widths.")
    observations = []
    for sigma, modulus in [(4, 17), (8, 37), (16, 67)]:
        # This truncation discards less than 1e-80 mass in the selected cases.
        integers = np.arange(-8*sigma, 8*sigma+1)
        weights = np.exp(-np.pi*(integers/sigma)**2)
        probabilities = weights/weights.sum()
        folded = np.bincount(integers % modulus, weights=probabilities, minlength=modulus)
        collision = float(folded @ folded)
        case.near(f"sigma_{sigma}_modular_normalization", folded.sum(), 1.0)
        case.at_most(f"sigma_{sigma}_collision_at_most_max_mass", collision, float(folded.max()))
        case.at_most(f"sigma_{sigma}_maximum_mass_bound", float(folded.max()), 2/sigma)
        observations.append({"sigma": sigma, "q": modulus, "collision": collision,
                             "maximum_mass": float(folded.max()), "bound": 2/sigma})
    case.metric("finite_folding_checks", observations)
    case.metric("integer_truncation_radius_in_width_units", 8)
    return case


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("verified_results.json"))
    args = parser.parse_args()
    started = time.perf_counter()
    jobs = [
        ("fresh_uniform_shifted", lambda: fresh_case("fresh_uniform_shifted", [1/3]*3, conditional_shifts([0.6, 0.3, 0.1], [0, 1, 2]))),
        ("fresh_nonuniform_conditional", lambda: fresh_case("fresh_nonuniform_conditional", [0.5, 0.3, 0.2], [[0.9, 0.1], [0.45, 0.55], [0.2, 0.8]])),
        ("fresh_single_supported_address", lambda: fresh_case("fresh_single_supported_address", [1, 0, 0], [[0.9, 0.1], [0.45, 0.55], [0.2, 0.8]])),
        ("fresh_deterministic_labels", lambda: fresh_case("fresh_deterministic_labels", [1/3]*3, [[1, 0], [0, 1], [1, 0]])),
        ("frozen_uniform_shifted_T2", lambda: static_case("frozen_uniform_shifted_T2", [1/3]*3, conditional_shifts([0.6, 0.3, 0.1], [0, 1, 2]), 2)),
        ("frozen_nonuniform_conditional_T2", lambda: static_case("frozen_nonuniform_conditional_T2", [0.5, 0.3, 0.2], [[0.9, 0.1], [0.45, 0.55], [0.2, 0.8]], 2)),
        ("frozen_nonuniform_conditional_T3", lambda: static_case("frozen_nonuniform_conditional_T3", [0.5, 0.3, 0.2], [[0.9, 0.1], [0.45, 0.55], [0.2, 0.8]], 3)),
        ("frozen_T_exceeds_address_support", lambda: static_case("frozen_T_exceeds_address_support", [0.7, 0.3], [[0.6, 0.4], [0.2, 0.8]], 3)),
        ("frozen_product_label_noise_T2", lambda: static_case("frozen_product_label_noise_T2", [1/3]*3, conditional_shifts([0.36, 0.24, 0.24, 0.16], [0, 1, 2]), 2)),
        ("fresh_frozen_swap_control", fresh_frozen_case),
        ("channel_biased_noise", lambda: channel_case("channel_biased_noise", 3, [0.85, 0.10, 0.05], [0, 1, 2])),
        ("channel_uniform_support_noise", lambda: channel_case("channel_uniform_support_noise", 3, [0.5, 0.5, 0], [0, 1, 2])),
        ("channel_deterministic_noise", lambda: channel_case("channel_deterministic_noise", 3, [0, 1, 0], [0, 1, 2])),
        ("explicit_Stinespring_degradability", degradability_case),
        ("finite_hash_moment_order", finite_hash_case),
        ("scalar_Fourier_and_fixed_table_verification", scalar_fourier_case),
        ("one_copy_erasure_scope", erasure_witness_case),
        ("folded_Gaussian_collision_bound", folded_gaussian_case),
    ]
    results = []
    for name, function in jobs:
        try:
            result = function().result()
        except Exception as error:
            result = {"name": name, "passed": False, "exception": str(error), "traceback": traceback.format_exc()}
        results.append(result)
        print(("PASS" if result["passed"] else "FAIL") + " " + name)
    passed = all(result["passed"] for result in results)
    report = {
        "schema_version": 1,
        "all_passed": passed,
        "scope": "Deterministic finite-dimensional consistency checks; not proofs of asymptotic theorems or cryptographic hardness.",
        "construction": "Sources are formed by explicit enumeration of label tables; the classical simulator is formed independently from iid classical record tuples with a fixed collision fallback.",
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "platform": platform.platform()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "random_seed_for_fixed_finite_probes": SEED,
        "absolute_tolerance": TOL,
        "elapsed_seconds": time.perf_counter()-started,
        "case_count": len(results),
        "check_count": sum(len(result.get("checks", [])) for result in results),
        "cases": results,
        "limitations": [
            "No finite calculation proves a statement for arbitrary alphabets or copy counts.",
            "The diamond-norm upper bound and uniform-input capacity optimum are analytic results; finite reference probes and input probes only check selected instances.",
            "Small supplied quantum-example Fourier calculations are consistency checks, not cryptanalytic benchmarks or verification of any lattice-hardness assumption.",
            "The finite hash example checks a specific GF(4) family and is not a performance benchmark.",
            "Floating-point eigenvalues within the stated tolerance are treated as numerical roundoff.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False)+"\n", encoding="utf-8")
    print(f"{sum(result['passed'] for result in results)}/{len(results)} cases passed; {report['check_count']} checks.")
    print(f"Results: {args.output}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

