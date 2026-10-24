# Quantum examples with independently randomized labels

## Question and operational comparison

A quantum example places many classical input–label pairs in superposition. This access can make a learning task easier, even when a quantum computer supplied only ordinary classical examples is believed unable to solve it efficiently. The question here is which noise in the **label-generation rule** removes that additional source access.

The main result supplies a quantum simulator whose only data input is a list of ordinary classical examples. It produces an approximation to the complete quantum experiment before any measurement. Consequently, a learner may use joint measurements, quantum memory, adaptive processing and an arbitrary quantum output model. The simulation preserves the learner's quantum computational power. It does not claim that an arbitrary quantum computation can be simulated by a classical computer.

The source model below follows the independently randomized-label construction used for noisy quantum examples in [Grilo–Kerenidis–Zijlstra](../references/RELATED_WORK.md#gkz2019) and, for binary labels, the mixture-of-superpositions model discussed in [Caro and collaborators](../references/RELATED_WORK.md#caro2024). The frozen-table joint experiment requires its own definition because repeated copies are correlated after the table is averaged out.

## 1. Classical data and hidden label tables

Let $`\mathcal A`$ and $`\mathcal Y`$ be finite sets encoded by bit strings. Let $`p_a`$ be an input distribution and $`P_a(y)`$ a conditional label distribution:

```math
p_a\ge0,\qquad \sum_a p_a=1,
\qquad P_a(y)\ge0,\qquad \sum_yP_a(y)=1.
```

The ordinary classical example oracle independently draws

```math
A\sim p,\qquad Y\mid A=a\sim P_a.
```

The family $`P_a`$ may depend on an unknown secret or signal. The simulator is not given that signal, a formula for $`P_a`$, or a description of $`p`$. It receives sampled bit strings only.

To define a quantum example, independently draw one label $`F(a)\sim P_a`$ at every address $`a`$. This random table defines the normalized positive-amplitude graph state

```math
|\psi_F\rangle
=\sum_{a\in\mathcal A}\sqrt{p_a}\,|a\rangle|F(a)\rangle.
```

For a fixed realized table this is a pure state. The table, its generating seed and any purification of the random choice remain unavailable to the learner. The learner receives example states; a coherent value oracle, an inverse value oracle and a classical table description are separate resources.

Measuring one example in the computational basis reproduces the ordinary classical distribution after averaging over $`F`$. Its diagonal density operator is

```math
\tau=\sum_{a,y}p_aP_a(y)
|a,y\rangle\langle a,y|.
```

The labels are sampled as classical values before the graph state is emitted. The model is therefore different from a coherent conditional-distribution state with amplitudes $`\sqrt{P_a(y)}`$ over every possible label. That latter source has a different density operator and is not supplied here.

## 2. Two source schedules

| Source schedule | Joint state supplied in a $`T`$-example experiment |
|---|---|
| **Refreshed table:** an independent hidden table is selected for each emitted example | $`\rho^{\otimes T}`$, where $`\rho=\mathbb E_F|\psi_F\rangle\langle\psi_F|`$ |
| **Frozen table:** one hidden table is selected and its pure state is copied $`T`$ times | $`\Omega_T=\mathbb E_F[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}]`$ |

The order of averaging and taking tensor powers is essential. In general $`\Omega_T\ne\rho^{\otimes T}`$. For example, the swap test accepts two copies from the same pure source with probability one, whereas two independently refreshed mixed examples need not pass with certainty.

All frozen-source conclusions average over the **initial hidden table**, while holding the underlying conditional laws and secret fixed. They do not assert closeness to a classical simulator for each disclosed or adversarially chosen table realization. This ensemble quantifier is compatible with arbitrary coherent processing of all copies.

The source cost and its finite-randomness realization are specified in [source preparation](source_preparation.md). For arbitrary $`p`$, efficient preparation of $`\sum_a\sqrt{p_a}|a\rangle`$ is an explicit additional requirement. Uniform finite-group inputs used in the lattice examples have direct circuit constructions.

## 3. Collision quantities and accuracy

Define the conditional label collision probabilities, their input average, and the input collision probability by

```math
c_a=\sum_yP_a(y)^2,
\qquad \overline c=\sum_a p_ac_a,
\qquad \alpha=\sum_a p_a^2.
```

Thus $`c_a`$ is the probability that two independent labels at address $`a`$ agree. The quantity $`\alpha`$ is the probability that two independently drawn input addresses agree. Both appear because a collection of examples can repeat labels and input addresses in different ways.

For a translated error law on a finite additive group,

```math
P_a(y)=\chi(y-f(a)),\qquad
c_a=c=\sum_e\chi(e)^2=2^{-H_2(\chi)},
```

where $`H_2`$ uses base-two logarithms. For uniform inputs on $`N`$ addresses, $`\alpha=1/N`$.

We use half trace distance

```math
D(\omega,\sigma)=\frac12\|\omega-\sigma\|_1.
```

An error bound $`D\le\varepsilon`$ bounds the change in the probability of any final event by $`\varepsilon`$. It survives any common quantum channel, measurement, adaptive postprocessing or addition of independent ancillas. Reference systems correlated with a chosen channel input are handled by the separate [diamond-distance theorem](channels.md); that stronger channel interface is not silently added to the random-example learning model.

## 4. Canonical result index

| Result | Statement and authoritative proof |
|---|---|
| **F1 — refreshed examples** | Exact one-copy difference and trace distance; translated uniform case $`D(\rho,\tau)=c(1-1/N)`$. [Refreshed sources](refreshed_sources.md) |
| **S1 — frozen examples** | A quantum simulator using exactly $`T`$ classical examples satisfies $`D(\Omega_T,\sigma_T)\le T\overline c+\binom{T}{2}\alpha`$, with the sharper common-core expression below. [Frozen sources](frozen_sources.md) |
| **S1 implementation** | Coherent permutation of a supplied polynomial-size classical list, a collision fallback, and finite-precision costs. [Simulator](simulator.md) |
| **P1 — source realization** | Pairwise independence for fresh examples and $`2T`$-wise independence for a declared frozen-copy budget; hidden seed and sampler precision charged explicitly. [Source preparation](source_preparation.md) |
| **L1 — learning transfer** | Any learner for the specified source can be simulated by a quantum processor supplied ordinary classical examples, with the stated success-probability loss. [Lattice examples](lattice_examples.md) |
| **L2 — auxiliary labels** | Classically irrelevant independently randomized labels can suppress the advantage of a scalar LWE quantum-example source. [Lattice examples](lattice_examples.md#3-adding-classically-irrelevant-labels) |
| **L3 — ring and module examples** | Independent coefficient errors multiply collision probabilities; hardness transfers only for the explicitly assumed classical problem and sample budget. [Lattice examples](lattice_examples.md#4-ring-and-module-valued-labels) |
| **E1 — coherent label deletion** | No universal exact one-copy channel deletes unknown output coordinates while preserving the desired pure projected example. [Label erasure](label_erasure.md) |
| **C1 and C2 — channel consequences** | Exact half diamond distance and a known-channel capacity formula. [Channels](channels.md) |

For S1 define the common-core weight

```math
w_T=\sum_{\substack{a_1,\ldots,a_T\\\text{pairwise distinct}}}
\prod_{i=1}^T p_{a_i}(1-c_{a_i}).
```

The sharp expression established by the proof is

```math
D(\Omega_T,\sigma_T)\le1-w_T
\le\min\!\left\{1,\ T\overline c+\binom{T}{2}\alpha\right\}.
```

For uniform inputs and a common translated error law,

```math
w_T=\frac{(N)_T}{N^T}(1-c)^T.
```

Here $`(N)_T=N(N-1)\cdots(N-T+1)`$ for $`T\le N`$, and the distinct-address probability is zero for $`T>N`$. The result is useful when the conditional label collision mass and the input birthday probability are small. It is a sufficient condition for simulation; a large bound does not establish a quantum advantage.

## 5. Computational and physical interpretation

For a security parameter $`\lambda`$, all input/output encodings and the copy count are charged. If $`T=\operatorname{poly}(\lambda)`$, $`\overline c`$ is negligible and $`\alpha`$ is negligible, the source experiment is reproducible to negligible error by an efficient quantum circuit fed ordinary examples. More generally, the explicit finite expression applies without an asymptotic security convention.

The noise acts through independent classical label choices at different input addresses. It is not a claim about arbitrary local laboratory noise. In particular, applying the same random output shift at every address preserves different coherences. Reusing an unknown table is allowed, but revealing its seed changes the learner's resources. The [interpretation](interpretation.md) explains these distinctions and the difference between operational simulation, entropy diagnostics and computational hardness.

Proceed to the [frozen-source proof](frozen_sources.md) for the main result, or to the [lattice examples](lattice_examples.md) for its learning consequences.
