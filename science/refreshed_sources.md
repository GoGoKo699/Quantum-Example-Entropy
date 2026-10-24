# Refreshed sources: exact distance from classical examples

This page proves **F1**, the exact one-copy identity for independent labels, and the simulation bound for independently refreshed emissions. Alphabets and Hilbert spaces are finite. Trace distance means $`D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$.

## Model and notation

Let $`\mathcal A`$ be an address alphabet with $`|\mathcal A|=N`$ and input distribution $`p`$. The learner and simulator need not know $`p`$. At each address, independently draw $`Y_a\sim P_a`$ on a common label alphabet $`\mathcal Y`$, and prepare

```math
|\psi_Y\rangle=\sum_a\sqrt{p_a}\,|a,Y_a\rangle,
\qquad
\rho=\mathbb E_Y|\psi_Y\rangle\langle\psi_Y|.
```

A refreshed source draws a new independent table before every emission. The encoded classical example is

```math
\rho_{\mathrm{cl}}
=\sum_a p_a|a\rangle\langle a|\otimes\tau_a,
\qquad
\tau_a=\sum_yP_a(y)|y\rangle\langle y|.
```

Use the notation

```math
|\mu_a\rangle=\sum_yP_a(y)|y\rangle,\qquad
c_a=\|\mu_a\|^2=\sum_yP_a(y)^2,\qquad
\bar c=\sum_ap_ac_a,\qquad
\alpha=\sum_ap_a^2.
```

The mean vector $`|\mu_a\rangle`$ contains probabilities as amplitudes and is generally unnormalized. It is different from the square-root encoding $`\sum_y\sqrt{P_a(y)}|y\rangle`$.

## F1 — Exact one-copy identity

Define

```math
r_a=\frac{p_ac_a}{\bar c},\qquad
|u_r\rangle=\sum_a\sqrt{r_a}|a\rangle,\qquad
W|a\rangle=|a\rangle|\mu_a\rangle/\sqrt{c_a}.
```

Address orthogonality gives $`W^\dagger W=I`$. For a nonempty finite label law, $`c_a>0`$ and $`\bar c>0`$; zero-probability addresses may be omitted.

**Theorem F1.** The exact identities are

```math
\rho-\rho_{\mathrm{cl}}
=\bar c\,W\left(|u_r\rangle\langle u_r|-\operatorname{diag}r\right)W^\dagger,
```

```math
\boxed{D(\rho,\rho_{\mathrm{cl}})=\bar c\,\lambda(r).}
```

If $`r`$ has at least two positive entries, $`\lambda(r)`$ is the sole positive eigenvalue of $`|u_r\rangle\langle u_r|-\operatorname{diag}r`$, equivalently the unique positive solution of

```math
\sum_{a:r_a>0}\frac{r_a}{r_a+\lambda}=1.
```

For one-point support, set $`\lambda(r)=0`$. In particular,

```math
\bar c\left(1-\sum_ar_a^2\right)
\le D(\rho,\rho_{\mathrm{cl}})
\le\bar c\sqrt{1-\sum_ar_a^2}
\le\bar c.
```

### Proof

For distinct addresses, independence gives

```math
\mathbb E_Y|Y_a\rangle\langle Y_b|
=|\mu_a\rangle\langle\mu_b|.
```

The diagonal blocks average to $`\tau_a`$, so

```math
\rho-\rho_{\mathrm{cl}}
=\sum_{a\ne b}\sqrt{p_ap_b}\,
|a\rangle\langle b|\otimes|\mu_a\rangle\langle\mu_b|.
```

Substitution proves the operator identity, and isometric conjugation preserves its nonzero singular values. On the support of $`r`$,

```math
|u_r\rangle\langle u_r|-\operatorname{diag}r
=\operatorname{diag}(\sqrt r)(J-I)\operatorname{diag}(\sqrt r),
```

where $`J`$ is the all-ones matrix. For support size $`k\ge2`$, congruence preserves inertia: there is one positive and $`k-1`$ negative eigenvalues. The trace is zero, so the half trace norm equals the positive eigenvalue.

The matrix determinant lemma gives the secular equation. Its left-hand side decreases continuously from $`k`$ to zero, proving uniqueness. The Rayleigh quotient at $`|u_r\rangle`$ gives the lower bound. The squared fidelity between $`|u_r\rangle\langle u_r|`$ and $`\operatorname{diag}r`$ is $`\sum_ar_a^2`$; the pure-state fidelity bound on trace distance gives the upper bound. ∎

## Uniform additive errors

Let the labels lie in a finite abelian group $`G`$, with

```math
Y_a=f(a)+E_a,\qquad E_a\overset{\mathrm{ind}}{\sim}\chi.
```

Translation permutes probabilities, so $`c_a=c=\sum_e\chi(e)^2=2^{-H_2(\chi)}`$. Arbitrary inputs give $`D(\rho,\rho_{\mathrm{cl}})=c\lambda(p)`$. Uniform inputs give

```math
\boxed{D(\rho,\rho_{\mathrm{cl}})=c(1-1/N).}
```

The nonzero eigenvalues of the difference are $`c(1-1/N)`$ once and $`-c/N`$ with multiplicity $`N-1`$.

For product errors,

```math
\chi=\chi_0^{\otimes d}
\quad\Longrightarrow\quad
c=\left(\sum_z\chi_0(z)^2\right)^d.
```

This is a statistical factorization, not a computational hardness claim for a particular error family.

## Simulation of refreshed specimens

For $`T`$ independent emissions, the real state is $`\rho^{\otimes T}`$. Given exactly $`T`$ ordinary classical examples, a quantum simulator prepares their computational-basis encodings. Its state is $`\rho_{\mathrm{cl}}^{\otimes T}`$. A tensor-product hybrid gives

```math
D(\rho^{\otimes T},\rho_{\mathrm{cl}}^{\otimes T})
\le\min\{1,T\bar c\,\lambda(r)\}
\le\min\{1,T\bar c\}.
```

Contractivity makes this bound apply to every subsequent quantum computation, including adaptive processing and stopping after at most $`T`$ emissions. The simulator uses the supplied classical records; it does not need a description of $`P_a`$ or an evaluation procedure for $`f`$.

Only pairwise independence within one table is needed for F1. Independent refresh between emissions is needed to identify the joint state with $`\rho^{\otimes T}`$.

Repeated specimens of one frozen pure source have a different joint state. The [frozen-source theorem S1](frozen_sources.md) uses [coherent permutations of classical records](simulator.md). A SWAP test distinguishes frozen copies from independent copies of the averaged one-copy state, so the product simulator above cannot simply be reused.

## Scope and references

The model grants emitted states, not coherent chosen-address queries, a preparation unitary and its inverse, or a description of the hidden table. A computational consequence needs a hardness assumption for the exact classical distribution and sample budget.

The binary independent-label mixture-of-superpositions model appears in Caro et al., [*Classical Verification of Quantum Learning*](https://arxiv.org/abs/2306.04843), Definition 8. Grilo, Kerenidis, and Zijlstra analyze scalar noisy quantum examples in [*Learning-with-errors problem is easy with quantum samples*](https://doi.org/10.1103/PhysRevA.99.032314). See [Related work](../references/RELATED_WORK.md) for the comparison.

The [finite verification](../verification/README.md) averages all label tables for small alphabets and independently checks the resulting spectra and trace distances. These checks do not replace the proof.

