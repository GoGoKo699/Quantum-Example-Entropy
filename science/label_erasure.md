# What coherent deletion of an output label requires

A classical learner can delete unused coordinates of a sample without affecting the coordinates it retains. For quantum examples, those coordinates can record which input branch occurred. Tracing them out then removes off-diagonal matrix elements. This section identifies the corresponding access requirement and gives a finite impossibility witness.

## 1. Discarding a register

For two label functions $`u(a)`$ and $`v(a)`$, consider

```math
|\Psi\rangle
=\sum_a\sqrt{p_a}\,|a,u(a)\rangle|v(a)\rangle.
```

The state obtained by discarding the last register is

```math
\operatorname{Tr}_v|\Psi\rangle\langle\Psi|
=\sum_{a,b}\sqrt{p_ap_b}\,
\mathbf1_{v(a)=v(b)}
|a,u(a)\rangle\langle b,u(b)|.
```

The desired pure projected example has the same expression without the equality indicator. Equality holds only when the omitted label is constant on the occupied branches, or under another condition that makes the unwanted record harmless. In a noisy vector-valued example, that condition is not generally satisfied.

A known reversible value circuit would provide a different operation. One may coherently copy the retained coordinates into a clean register, run the inverse full-value circuit to clear the original label, and keep the copied coordinates. The same hidden error function must be used by that inverse. Sample copies alone do not supply such a circuit or its inverse.

## 2. E1: no universal exact one-copy deletion channel

Take two input addresses and two output bits. Three possible label tables are

| Table | Output at address $`0`$ | Output at address $`1`$ |
|---|---|---|
| $`f`$ | $`00`$ | $`00`$ |
| $`g`$ | $`00`$ | $`01`$ |
| $`h`$ | $`10`$ | $`00`$ |

Let $`|\Psi_f\rangle,|\Psi_g\rangle,|\Psi_h\rangle`$ be their uniform graph states. Let $`|\phi_f\rangle,|\phi_g\rangle,|\phi_h\rangle`$ be the uniform graph states after deleting the second output bit from the tables. Directly,

```math
\langle\Psi_f|\Psi_g\rangle=\frac12,
\qquad
\langle\Psi_f|\Psi_h\rangle=\frac12,
\qquad
\langle\Psi_g|\Psi_h\rangle=0,
```

whereas

```math
|\phi_f\rangle=|\phi_g\rangle,
\qquad
\langle\phi_f|\phi_h\rangle
=\langle\phi_g|\phi_h\rangle=\frac12.
```

**E1.** No quantum channel, supplied one copy of the input state, maps each of these three full graph states to its corresponding pure projected graph state.

**Proof.** A Stinespring isometry for such a channel would have to satisfy

```math
V|\Psi_j\rangle=|\phi_j\rangle|\eta_j\rangle
\qquad (j\in\{f,g,h\}),
```

because a pure reduced output has a product purification. Preservation of inner products would require

```math
\langle\eta_f|\eta_g\rangle=\frac12,
\qquad
\langle\eta_f|\eta_h\rangle=1,
\qquad
\langle\eta_g|\eta_h\rangle=0.
```

The middle equality makes the unit vectors $`\eta_f`$ and $`\eta_h`$ identical. The first and last equalities then contradict one another. This proves E1.

All three tables can occur with nonzero probability under independently sampled bounded binary output errors. The statement is a one-copy, tablewise impossibility for a universal exact deletion operation. This finite witness does not rule out all collective transformations using additional copies. It is also not an unconditional impossibility theorem for every learning procedure on an averaged noisy ensemble; the [simulation theorem](frozen_sources.md) supplies the relevant many-copy ensemble comparison.

## 3. Ring-LWE scalar extraction

A polynomial ring sample has several output coefficients. A known linear coordinate transformation on the input can identify the scalar linear form associated with one output coefficient. It does not by itself erase the other coefficients, which depend on the unknown secret and hidden error table.

[Kim and Kim, Result 1](../references/RELATED_WORK.md#kimkim2024), first retain the full noisy polynomial label and then pass to a pure single-coefficient example. The stated sample-output interface does not justify that coherent-deletion step. The partial-trace calculation above explains why simply discarding the unwanted outputs does not implement it. A reversible noisy-value oracle, supplied with the appropriate inverse and the same hidden table, would constitute additional access and would require its own analysis.

The conclusion is scoped to the reduction as written under sample-state access. It does not claim that every stronger quantum Ring-LWE oracle is hard. For independent coefficient errors with negligible total collision probability, [L3](lattice_examples.md#4-ring-and-module-valued-labels) gives the more general consequence: every efficient learner on the stated fresh or frozen sample ensemble can be simulated from ordinary classical samples, up to the explicit error bound.
