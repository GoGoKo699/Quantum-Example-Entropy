# What label entropy changes about quantum data access

## The resource being compared

The comparison keeps quantum computation available on both sides. One learner receives noisy quantum examples; another receives ordinary classical examples and may run a quantum circuit on them. The main theorem constructs that circuit, including the correlations needed to reproduce a frozen-source experiment. A negligible simulation error therefore removes the extra power of the coherent **data source**, without asserting that quantum computation itself has become classically simulable.

The statement is also stronger than the failure of a chosen algorithm. Trace distance controls every final measurement, so an alternative collective measurement, an adaptive learning strategy or a retained quantum hypothesis cannot exceed the simulation error merely by changing the postprocessing. [L1](lattice_examples.md) makes the computational consequence precise.

## Why collision probability appears

A label at address $`a`$ is a random computational-basis vector $`|Y_a\rangle`$. Its mean vector is

```math
|\mu_a\rangle=\mathbb E|Y_a\rangle
=\sum_yP_a(y)|y\rangle,
\qquad
\|\mu_a\|^2=\sum_yP_a(y)^2=c_a.
```

The probability weights appear directly as amplitudes of the **mean vector** because the source selects one classical label per address. They are not the square-root weights of a coherent sampler over all labels. This distinction explains the collision probability in the theorem.

The second moment decomposes into two positive terms:

```math
D_a=\mathbb E|Y_a\rangle\langle Y_a|
=K_a+|\mu_a\rangle\langle\mu_a|,
\qquad
K_a\ge0,\qquad \mathrm{Tr}K_a=1-c_a.
```

When $`c_a`$ is small, the centered covariance carries almost all the mass. In a collection of copies, products of independent centered variables vanish unless the same input addresses are matched on the bra and ket sides. For distinct addresses, the surviving terms are precisely the coherent permutations reproduced by the classical-data simulator. The [common-core proof](frozen_sources.md) identifies that large positive component inside both experiments.

Thus there are two losses. Some weight lies outside the centered covariance, contributing at most $`T\overline c`$. Some input addresses repeat, contributing at most $`\binom{T}{2}\alpha`$. This mechanism gives the general law without a linear function, a Fourier decoder or a lattice assumption.

## Purity and repeated copies

A frozen example is pure for every realized label table. The comparison nevertheless averages over the hidden table when describing the learner's experiment:

```math
\Omega_T=\mathbb E_F
[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}].
```

This is the same averaging used to evaluate an algorithm's success over randomized input instances. It does not say that an individual realized pure state has a nearly diagonal density matrix. Its purity can be detected across copies: for example, two copies pass a swap test with certainty.

The simulator retains this permutation coherence. On distinct sampled addresses it outputs a coherent superposition of all permutations of the supplied classical examples. Its successful output also lies in the symmetric subspace. Replacing the frozen experiment by independent diagonal states would lose this feature and would generally be wrong, even when the one-copy distance is tiny.

The one-copy [fresh-source identity](refreshed_sources.md) and the frozen-source theorem therefore answer different questions. The former identifies the mixed output of a renewed random source; the latter controls all collective observations on copies generated from one hidden random choice.

## Output size and noise magnitude

For independent coefficient errors, collision probabilities multiply. If one coefficient has collision probability $`c_0`$, a label with $`d`$ independent noisy coefficients has $`c_0^d`$. Each coefficient can remain numerically small relative to the modulus while the total conditional label entropy is large.

This explains why scalar and vector labels behave differently in the [lattice examples](lattice_examples.md). The output is an information-bearing register, so its number of independently randomized coordinates is an operational feature. A classical conversion that retains one coordinate does not automatically lift to coherent conversion of the corresponding quantum example.

The auxiliary-label construction makes the point without ring algebra. The additional classical labels are independent random bits, so they provide no information about the secret. Yet their address-dependent quantum records change the graph source and can suppress its advantage. The [label-erasure lemma](label_erasure.md) identifies the missing operation in an attempted coherent deletion.

## Dependence of the specified simulator's error

The linear collision term is meaningful, although the theorem is not a universal optimality result over all possible simulators. Consider uniform inputs on $`N`$ addresses and uniform labels on $`K`$ values, so $`c=1/K`$. Let

```math
P=|+_N\rangle\langle+_N|\otimes I_{\mathcal Y}.
```

If a realized table assigns $`n_y`$ addresses to label $`y`$, then

```math
\langle\psi_F|P|\psi_F\rangle
=\sum_y\frac{n_y^2}{N^2}\ge\frac1K=c.
```

Measure $`\{P,I-P\}`$ separately on all $`T`$ registers and accept if at least one outcome is $`P`$. On the frozen source the acceptance probability is at least $`1-(1-c)^T`$. On a coherent permutation of distinct classical examples, every single-register reduced state is diagonal in the address–label basis, so each marginal has $`P`$-probability $`1/N`$. Choose a computational-basis fallback on a collision. The union bound then makes the simulator's acceptance probability at most $`T/N`$. Therefore this particular simulator obeys the lower bound

```math
D(\Omega_T,\sigma_T)
\ge 1-(1-c)^T-\frac TN.
```

Together with S1, the upper and lower bounds are both asymptotic to $`Tc`$ when $`Tc=o(1)`$ and $`T^2/N=o(Tc)`$. It is a lower bound against the **specified coherent-permutation simulator**. If the conditional law is known, another simulator may exploit that knowledge; this example does not establish an impossibility threshold for all classical-data simulators.

## Access and implementation boundaries

| Change to the experiment | Why the theorem does not silently cover it |
|---|---|
| One common error added to every input branch | Errors at different addresses are then correlated, so the centered-variable cancellation changes. |
| A quantum register independent of the address is appended | It can be discarded without changing the original example; this is different from address-dependent random labels. |
| The hidden error seed is supplied | A learner may be able to evaluate and undo the error function. |
| Coherent value queries and their inverse are supplied | They can enable output erasure or chosen-input strategies unavailable from sample copies. |
| An arbitrary input distribution is declared efficiently available in superposition | Its preparation cost must be supplied explicitly; P1 does not provide free data loading. |
| A fixed finite-independence seed is reused for an unrestricted number of copies | The exact source compilation is tied to its declared copy budget. |

[P1](source_preparation.md) provides polynomial source constructions for the stated finite experiments and charges random-seed length, reversible computation, workspace return and precision. The learner's simulator scans only its polynomial-size list of supplied examples. These constructions avoid an exponential lookup table and do not assume QRAM.

## Channels and computational assumptions

The [channel companion](channels.md) quantifies the refreshed append map in half diamond norm and computes its known-channel quantum capacity. A channel with negligible coherent transmission but intact classical address transmission is a useful physical interpretation of the one-copy mechanism. The capacity statement assumes a known, memoryless channel and unrestricted coding in that channel model; the learning problem has an unknown signal and random example inputs. The two conclusions should not be substituted for one another.

For lattice learning, the source simulation is unconditional. Hardness follows only after fixing a classical-input problem and assuming that quantum algorithms cannot solve it efficiently. High entropy does not make an easy classical problem hard, and a nonzero per-coefficient entropy does not certify a secure parameter choice. The precise transfer and examples are in [L1–L3](lattice_examples.md).

The [related-work account](../references/RELATED_WORK.md) credits the established symmetrization, random-subset and bounded-independence methods. The contribution is the explicit conditional-label comparison, its common positive component, and the consequences for structured noisy quantum data.
