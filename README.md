# When Label Entropy Removes the Advantage of Quantum Examples

**When can copies of a noisy quantum example be reproduced from ordinary classical data?** This project gives a simulation criterion controlled by conditional label collision probability and input repetition. It covers repeated copies of one pure state whose noisy labels were selected once and then kept fixed.

The simulator receives exactly the same number of ordinary classical examples as the learner receives quantum examples. It may perform quantum computation, including coherent permutation of its supplied examples. Its data access is classical, and it needs no QRAM.

## Main result

Let inputs follow probabilities $`p_a`$. Independently draw one label $`F(a)\sim P_a`$ at every input, and define

```math
|\psi_F\rangle=\sum_a\sqrt{p_a}|a,F(a)\rangle,
\qquad
\Omega_T=\mathbb E_F
[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}].
```

There is an efficient quantum simulator fed exactly $`T`$ ordinary examples from $`p_aP_a(y)`$ whose output $`\sigma_T`$ obeys

```math
D(\Omega_T,\sigma_T)
\le
T\sum_a p_a\sum_yP_a(y)^2
+\binom{T}{2}\sum_a p_a^2,
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The distance is also bounded by one. The [full theorem](science/frozen_sources.md) gives a sharper expression from a common positive operator contained in both states. The bound holds before every joint measurement or coherent learning procedure. It averages over the initially selected hidden label table, while holding the underlying signal and conditional laws fixed.

For uniform inputs on $`N`$ addresses and additive errors with distribution $`\chi`$, write

```math
c=\sum_e\chi(e)^2=2^{-H_2(\chi)}.
```

| Source | Simulation error |
|---|---|
| Independently refreshed table for each example | At most $`Tc(1-1/N)`$; the one-copy distance is exactly $`c(1-1/N)`$ |
| One frozen table reused across $`T`$ copies | At most $`1-[(N)_T/N^T](1-c)^T\le Tc+T(T-1)/(2N)`$ |

Repeated copies retain permutation coherence. The simulator reproduces it by preparing a coherent superposition of permutations of the classical examples when their input addresses are distinct. A fixed fallback handles repeated addresses. The [construction](science/simulator.md) uses a polynomial-size list and ordinary reversible operations.

## Consequences for learning with errors

Scalar LWE has an established efficient quantum-example learner. Adding independent, address-dependent random labels can preserve the entire classical learning problem while removing the advantage of its coherent example source. This is the [auxiliary-label separation](science/lattice_examples.md#3-adding-classically-irrelevant-labels).

For a full ring-valued output with $`d`$ independent error coefficients, the collision probability is $`c_0^d`$. Polynomially many examples can therefore be simulated with negligible error when the total collision entropy is sufficiently large. Under quantum hardness of the **specified ordinary classical-input Ring-LWE problem**, the corresponding fresh and frozen quantum-example sources remain hard. The [lattice account](science/lattice_examples.md) fixes the access model, sample budget and parameter assumptions and separates this conditional consequence from the unconditional simulation theorem.

The source includes the full noisy output. [Coherent label deletion](science/label_erasure.md) explains why discarding unused coefficients does not generally produce a pure scalar example. The [related-work comparison](references/RELATED_WORK.md) treats the published Ring-LWE scalar-extraction claim proportionately and credits the earlier noisy-example, permutation-simulation and positive-subset methods.

## Read the science

| Question | Authoritative account |
|---|---|
| What is supplied, hidden, averaged and charged? | [Model and exact claims](science/model.md) |
| Why are frozen pure examples simulable? | [Common positive-operator proof](science/frozen_sources.md) |
| How is the simulator implemented? | [Coherent permutation and costs](science/simulator.md) |
| Can the source be built without an exponential table? | [Finite-independence source preparation](science/source_preparation.md) |
| What happens for scalar, ring and module labels? | [Lattice examples and conditional hardness](science/lattice_examples.md) |
| Why is coherent output deletion an additional operation? | [Label-erasure obstruction](science/label_erasure.md) |
| What is the exact refreshed-source distance? | [Refreshed examples](science/refreshed_sources.md) |
| What does the associated memoryless channel transmit? | [Channel distance and capacity](science/channels.md) |
| What is the physical and computational meaning? | [Interpretation](science/interpretation.md) |
| Which ingredients and nearby results are established prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [science entrypoint](science/README.md) connects these topics in one reading route. The [LLM guide](llms.txt) maps questions to the same authoritative proofs.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

The suite directly constructs small source states and independently builds the classical-data simulator. It checks the moment identities, common positive operator, trace distances, source-schedule distinction and channel calculations. [Verification details](verification/README.md) identify the cases, tolerances and actual outputs. The analytical proofs establish the general laws; finite checks do not establish lattice hardness or scientific priority.

## Scope

Labels are randomized independently across full input addresses, and the hidden seed is unavailable to the learner. A common error shared by all branches and a coherent value oracle with inverse access define different experiments. A finite $`2T`$-wise construction reproduces a declared $`T`$-copy frozen experiment; source preparation and precision are explicitly charged.

The simulator preserves quantum processing while replacing coherent data access. Large collision probability does not by itself imply an efficient learner, and high entropy does not certify a hard classical problem. The channel-capacity companion assumes a known memoryless channel and has a separate operational scope.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository is distributed under the [MIT License](LICENSE).
