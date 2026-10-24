# Learning with errors: scalar labels, auxiliary labels and rings

The simulation theorem does not use linearity. Linearity matters here because scalar LWE has an established efficient quantum-example learner, while ordinary classical-input LWE and suitable ring variants are used as computational hardness assumptions. This produces a concrete comparison between different coherent sources for closely related classical data.

The unconditional part of every result below is the source simulation and its error bound. A computational hardness conclusion assumes hardness of the **specified classical distribution against quantum algorithms**, with the same secret distribution and the stated sample budget. The discussion does not establish cryptographic security for arbitrary rings or error parameters.

## 1. L1: transfer of a learning experiment

Let $`\theta`$ be any hidden parameter and let $`P_{a,\theta}`$ be its conditional label laws. Suppose a quantum algorithm $`\mathcal L`$ receives at most $`T`$ copies from a frozen source and produces an output $`Z`$. Pad a shorter adaptive run with unused registers so that it is a quantum channel acting on the full $`T`$-copy input.

Construct $`\mathcal L_{\rm cl}`$ by requesting exactly $`T`$ ordinary classical examples, running the [simulator](simulator.md), and applying $`\mathcal L`$. For every fixed $`\theta`$ and every event $`\mathcal E_\theta`$ on its output,

```math
\left|
\Pr[\mathcal L(\Omega_{T,\theta})\in\mathcal E_\theta]
-\Pr[\mathcal L_{\rm cl}\in\mathcal E_\theta]
\right|
\le
T\overline c_\theta+\binom{T}{2}\alpha.
```

This is **L1**, directly from S1 and trace-distance contractivity. It also holds after averaging over an arbitrary secret prior. The event may be exact secret recovery, successful prediction, or a verification test on a quantum output. The simulator itself is efficient and uses no information about the secret or conditional distributions.

For two decision experiments, apply the bound under each hypothesis. The change in distinguishing advantage is at most the sum of their two approximation errors. Defining a decision problem therefore requires specifying the quantum source under both hypotheses.

For refreshed examples, basis-state encoding of the classical data suffices and [F1](refreshed_sources.md) gives the appropriate fresh-source bound. None of these reductions replaces the quantum processor with a classical algorithm.

## 2. The established scalar endpoint

Let $`q`$ be prime, $`s\in\mathbb F_q^n`$, and let integer errors have support in $`[-B,B]`$, with $`B\ge1`$ and $`q\ge16B`$. A scalar graph state is

```math
|\psi_{s,E}\rangle
=q^{-n/2}\sum_{a\in\mathbb F_q^n}
|a\rangle|\langle a,s\rangle+E_a\bmod q\rangle.
```

The positive quantum-learning endpoint is due to [Grilo–Kerenidis–Zijlstra](../references/RELATED_WORK.md#gkz2019). The following elementary version makes the relevant parameters and frozen-table scope explicit. It is an exposition of their Fourier mechanism, not a new positive LWE algorithm.

Apply the Fourier transform on all registers and measure $`(x,y)\in\mathbb F_q^n\times\mathbb F_q`$. For any fixed bounded error table,

```math
\Pr[x=-ys,\,y]
=\frac1q\left|
q^{-n}\sum_a\exp(2\pi i yE_a/q)
\right|^2.
```

For $`1\le y\le\lfloor q/(8B)\rfloor`$, every phase has argument between $`-\pi/4`$ and $`\pi/4`$. The squared modulus of their average is at least $`1/2`$. There are at least $`q/(16B)`$ such nonzero values, so a Fourier measurement produces the correct candidate $`\widetilde s=-y^{-1}x`$ with probability at least $`1/(32B)`$. This lower bound is valid for every bounded table, independently of how it was drawn.

Candidates can be tested using additional measured examples. A correct candidate always satisfies the error bound. If $`\widetilde s\ne s`$, passing a test implies

```math
\langle a,s-\widetilde s\rangle\in[-2B,2B]\pmod q.
```

For uniform $`a`$, a nonzero linear form is uniform over $`\mathbb F_q`$, so the passing probability is at most $`(4B+1)/q<1/2`$. This conservative bound holds even for a fixed error table that depends on the address. Independent measurements of additional copies yield independent addresses. Repeating the candidate-generation and verification steps gives polynomial time and copy complexity when $`B,n,\log q`$ are polynomially bounded and the desired error is inverse exponential or inverse polynomial. Approximate Fourier transforms add their ordinary implementation error.

For independently randomized errors with law $`\chi`$, the exact averaged Fourier distribution is also informative. Set $`N=q^n`$ and

```math
\widehat\chi(y)=\sum_e\chi(e)\exp(2\pi i ye/q).
```

Then

```math
\Pr[x,y]
=\frac{1-|\widehat\chi(y)|^2}{Nq}
+\frac{|\widehat\chi(y)|^2}{q}\,
\mathbf1_{x=-ys}.
```

The output $`y`$ is uniform, and the total probability of the correct candidate with $`y\ne0`$ is

```math
c-\frac1q+\frac{1-c}{N},
\qquad c=\sum_e\chi(e)^2.
```

This follows from Fourier orthogonality and Parseval's identity. An inverse-polynomial $`c`$ is consistent with efficient scalar learning. A small upper simulation error is a sufficient obstruction; the converse assertion that large collision probability always makes learning easy is not part of the theorem.

## 3. Adding classically irrelevant labels

Append $`m`$ independent uniform bits to the label at each address. Draw a hidden random function $`Z_a\in\{0,1\}^m`$, independently across addresses and independently of $`E`$. The padded source is

```math
|\Psi_{s,E,Z}\rangle
=q^{-n/2}\sum_a
|a\rangle|\langle a,s\rangle+E_a\bmod q\rangle|Z_a\rangle.
```

Its ordinary classical data are exactly scalar LWE samples with independent uniform bits appended. A classical-input quantum algorithm can generate those bits itself, and deleting them recovers the original LWE distribution. The two classical statistical experiments therefore have the same computational power.

The quantum source has conditional label collision probability

```math
c_{\rm pad}=c_\chi\,2^{-m}.
```

By S1, a learner receiving copies from a frozen padded source can be simulated from exactly $`T`$ ordinary scalar LWE examples, with error at most

```math
\varepsilon_T
\le T c_\chi 2^{-m}
+\frac{T(T-1)}{2q^n}.
```

The simulator supplies the independent padding bits locally. For a fresh padded source, the error is at most $`T c_\chi2^{-m}(1-q^{-n})`$.

**L2.** Consider a scalar LWE family satisfying the bounded-error parameters in Section 2, with $`n,\log q,B,m`$ polynomially bounded in the security parameter $`\lambda`$, and assume that recovering its secret from ordinary classical examples is hard for quantum polynomial-time algorithms. If also $`m=\omega(\log\lambda)`$ and $`q^n`$ is superpolynomial in $`\lambda`$, then polynomially many padded quantum examples fail to permit efficient secret recovery under the same assumption. The unpadded quantum source has the established polynomial learner described above.

This is a source-access separation for classically equivalent data. The additional bits record a branch-dependent hidden function. They are not an independent quantum register tensor-multiplied onto the original example. Tracing them out can remove the coherence used by the scalar learner; [E1](label_erasure.md) gives a one-copy obstruction to universally deleting unknown output coordinates. S1 supplies the separate many-copy ensemble comparison.

The source circuits and copy-budget quantifiers are the same ones charged in [P1](source_preparation.md). Adding the uniform bits requires an additional finite-randomness sampler and output register, both of polynomial size when $`m`$ is polynomial.

## 4. Ring and module-valued labels

Fix an explicit family of polynomial rings

```math
R=\mathbb Z[X]/(\Phi(X)),
\qquad R_q=R/qR,
\qquad \deg\Phi=d,
```

with $`\Phi\in\mathbb Z[X]`$ monic and the degree-less-than-$`d`$ coefficient representation. Thus $`R_q`$ has exactly $`q^d`$ elements. A concrete common choice is $`\Phi(X)=X^d+1`$ for power-of-two $`d`$; no hardness claim is made for every monic polynomial. Let $`s\in R_q`$ have the chosen secret distribution. The classical sample is

```math
a\leftarrow R_q\text{ uniformly},
\qquad b=as+e,
\qquad e\sim\chi_R.
```

For coefficient-independent errors reduced modulo $`q`$,

```math
\chi_R=\chi_0^{\otimes d},
\qquad
c_R=\sum_{e\in R_q}\chi_R(e)^2
=\left(\sum_{z\in\mathbb Z_q}\chi_0(z)^2\right)^d
=c_0^d.
```

The collision probability is computed **after reduction modulo $`q`$**. Counting distinct integer errors as distinct labels when they coincide modulo $`q`$ would give the wrong value.

The full ring-valued quantum example is

```math
|\psi_{s,E}^{\rm ring}\rangle
=q^{-d/2}\sum_{a\in R_q}|a\rangle|as+E_a\rangle,
\qquad E_a\ \text{independently distributed as }\chi_R.
```

**L3.** Every $`T`$-copy learner for its frozen-table ensemble has a quantum simulation from exactly $`T`$ ordinary ring samples, with

```math
\varepsilon_T^{\rm ring}
\le1-\frac{(q^d)_T}{q^{dT}}(1-c_0^d)^T
\le T c_0^d+\frac{T(T-1)}{2q^d}.
```

For fresh ring examples, the bound is $`T c_0^d(1-q^{-d})`$. Thus, whenever $`dH_2(\chi_0)=\omega(\log\lambda)`$ and the input birthday term is negligible, quantum-example access adds only negligible power to quantum processing of ordinary classical ring samples.

For a module of rank $`k`$, take $`a,s\in R_q^k`$ and $`b=\sum_{j=1}^ka_js_j+e\in R_q`$. The input domain has size $`q^{dk}`$, while the single output polynomial still has $`d`$ noisy coefficients. Consequently the corresponding bound is

```math
\varepsilon_T^{\rm module}
\le T c_0^d+\frac{T(T-1)}{2q^{dk}}.
```

Module rank changes the input domain here; it does not create additional output-error coefficients. If the specified source emits several independently noisy output polynomials, their coefficient counts add in the exponent of $`c_0`$.

| Source | Input domain size | Conditional label collision probability |
|---|---:|---:|
| Scalar LWE | $`q^n`$ | $`c_0`$ |
| Scalar LWE with $`m`$ independent padding bits | $`q^n`$ | $`c_0 2^{-m}`$ |
| Ring-LWE, degree $`d`$ | $`q^d`$ | $`c_0^d`$ |
| Module-LWE, rank $`k`$, one output polynomial | $`q^{dk}`$ | $`c_0^d`$ |

## 5. Error laws and hardness assumptions

The theorem separates an explicit entropy calculation from a computational assumption. Examples of the first calculation include:

| Coefficient law, with no modular collisions | $`c_0`$ |
|---|---:|
| Uniform on $`K`$ residues | $`1/K`$ |
| Centered three-point law $`(1/4,1/2,1/4)`$ | $`3/8`$ |
| General finite law $`\chi_0`$ | $`\sum_z\chi_0(z)^2`$ |

These are entropy examples, not assertions that every listed law gives asymptotically hard LWE with arbitrary polynomially many samples. Small-support errors permit algebraic attacks whose costs depend on the support and sample count; [Arora–Ge](../references/RELATED_WORK.md#arorage2011) is a relevant warning. The exact hardness family must be stated separately.

A growing-width discrete Gaussian gives a useful conditional parameter regime. Let

```math
\chi_\sigma(z)
=\frac{\exp(-\pi z^2/\sigma^2)}{Z_\sigma},
\qquad
Z_\sigma=\sum_{z\in\mathbb Z}\exp(-\pi z^2/\sigma^2),
```

and let $`\chi_{\sigma,q}`$ be its reduction modulo $`q`$. For $`\sigma\ge4`$ and $`q\ge4\sigma`$,

```math
\sum_r\chi_{\sigma,q}(r)^2
\le\max_r\chi_{\sigma,q}(r)
\le\frac2\sigma.
```

To see the last inequality, choose the representative $`|r|\le q/2`$. Its folded numerator is at most

```math
1+2\sum_{j\ge1}
\exp\!\left[-\pi(j-1/2)^2(q/\sigma)^2\right]
<1.01,
```

while monotonicity of the Gaussian gives $`Z_\sigma\ge\sigma-1`$. Hence $`1.01/(\sigma-1)\le2/\sigma`$ for the stated range. For example, degree $`d`$, width $`\sigma=d`$ and any specified polynomial-size modulus $`q\ge d^3`$ yield

```math
\varepsilon_T^{\rm ring}
\le T(2/d)^d+\frac{T(T-1)}{2q^d}
\qquad(d\ge4).
```

This is an explicit negligibility calculation. To infer computational hardness, assume quantum hardness of the exact classical coefficient-Gaussian Ring-LWE family at the chosen modulus, secret prior and sample budget. The calculation itself is not a worst-case lattice reduction.

The canonical-embedding formulation and coefficient formulation require care. For power-of-two cyclotomics the embeddings are related by a scaled rotation, so spherical Gaussian coordinates can be matched after accounting for that scale. The [Lyubashevsky–Peikert–Regev reductions](../references/RELATED_WORK.md#lpr2013) also have important error-family and sample-count qualifications. This account does not replace those qualifications by an unrestricted claim about every fixed spherical or coefficient error law.

Finite source circuits use an explicitly truncated and finite-randomness approximation $`\widetilde\chi`$ when needed. If its total variation distance from the chosen classical error law is $`\delta`$, $`T`$ ordinary examples change by at most $`T\delta`$. Apply S1 directly to the implemented law and transfer a classical hardness assumption through that controlled error. [P1](source_preparation.md) separately bounds changes to the quantum frozen ensemble without union-bounding over exponentially many table entries.

## 6. What the lattice consequence establishes

The source simulator handles the complete output label. It avoids extracting a scalar coherent sample from a vector sample, which is precisely where discarded output coordinates become consequential. The [label-erasure analysis](label_erasure.md) and [related-work comparison](../references/RELATED_WORK.md#kimkim2024) explain the relationship to the published scalar-extraction argument.

The error values are independent across different full input addresses. A common error shared by all branches has another coherent action, and coherent evaluation or inverse access changes the problem. All learning hardness statements here concern random examples with the hidden seed inaccessible. Under those assumptions, the conclusion follows from a statistical simulation, not from a limitation of a particular Fourier algorithm.
