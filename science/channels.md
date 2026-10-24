# The refreshed encoding channel

This page proves **C1**, an exact diamond distance to an address-measuring channel, and **C2**, a quantum-capacity formula for a known memoryless additive-error channel. Random-example learning and chosen-input channel access are distinct resources.

All capacity logarithms are base two. Trace distance is $`D=\|\cdot\|_1/2`$.

## Definition

For a label table $`Y`$, define

```math
V_Y|a\rangle=|a,Y_a\rangle,\qquad
\mathcal E(\omega)=\mathbb E_YV_Y\omega V_Y^\dagger.
```

The labels are independent across addresses, with laws $`P_a`$. Write

```math
\tau_a=\mathrm{diag}P_a,\qquad
|\mu_a\rangle=\sum_yP_a(y)|y\rangle,\qquad
c_a=\|\mu_a\|^2.
```

Let $`\Delta`$ dephase the input address and set

```math
\mathcal C=\mathcal E\circ\Delta,\qquad
\mathcal C(\omega)=\sum_a\omega_{aa}|a\rangle\langle a|\otimes\tau_a.
```

The channel $`\mathcal C`$ measures the address and prepares its conditional output, so it is entanglement breaking.

## C1 — Exact diamond distance

Assume $`c_a=c`$ for every address; additive shifts of a common error law satisfy this condition. Let $`W|a\rangle=|a\rangle|\mu_a\rangle/\sqrt c`$.

**Theorem C1.** On all operators, including inputs entangled with any reference,

```math
\mathcal E-\mathcal C
=c\,\mathrm{Ad}_W\circ(\mathrm{Id}-\Delta).
```

Thus, for $`N=|\mathcal A|`$,

```math
\boxed{\frac12\|\mathcal E-\mathcal C\|_\diamond=c(1-1/N).}
```

### Proof

Diagonal matrix units have identical images. For $`a\ne b`$, independence gives

```math
\mathcal E(|a\rangle\langle b|)
=|a\rangle\langle b|\otimes|\mu_a\rangle\langle\mu_b|
=cW|a\rangle\langle b|W^\dagger.
```

Linearity proves the identity. Isometric output conjugation preserves diamond norm.

Number the addresses $`0,\ldots,N-1`$ and put $`Z|a\rangle=e^{2\pi ia/N}|a\rangle`$. For $`N\ge2`$,

```math
\Delta=\frac1N\sum_{k=0}^{N-1}\mathrm{Ad}_{Z^k},
```

```math
\mathrm{Id}-\Delta
=\left(1-\frac1N\right)
\left(\mathrm{Id}
-\frac1{N-1}\sum_{k=1}^{N-1}\mathrm{Ad}_{Z^k}\right).
```

A difference of channels has diamond norm at most two. This proves the upper bound with arbitrary reference systems. The uniform input $`|+\rangle`$ attains it: $`Z^k|+\rangle`$ for nonzero $`k`$ is orthogonal to $`|+\rangle`$. For $`N=1`$, both sides are zero. ∎

High conditional collision entropy therefore places this channel close to an entanglement-breaking channel. This chosen-input statement is not itself a standard-LWE hardness reduction; classical chosen-input access can be more informative than random examples.

## Positive decomposition

The label covariance matrix is

```math
A_a=\tau_a-|\mu_a\rangle\langle\mu_a|\succeq0.
```

Indeed, weighted Cauchy–Schwarz gives $`|\sum_yP_a(y)\overline{z_y}|^2\le\sum_yP_a(y)|z_y|^2`$. Its trace is $`1-c`$. For $`c<1`$, define $`\sigma_a=A_a/(1-c)`$. Then

```math
\mathcal E(\omega)=cW\omega W^\dagger
+(1-c)\sum_a\omega_{aa}|a\rangle\langle a|\otimes\sigma_a.
```

The first branch preserves the quantum input isometrically. The second measures it in the address basis. The branches need not be distinguishable at the output.

## C2 — Memoryless additive-error capacity

### Assumptions

Let $`G`$ be a finite abelian group, with

```math
P_a(y)=\chi(y-f(a)),\qquad
Y_a=f(a)+E_a,\qquad E_a\overset{\mathrm{ind}}{\sim}\chi.
```

A fresh independent table is drawn on each use. We calculate ordinary asymptotic **unassisted quantum capacity**, in qubits per use, for a **known memoryless channel**. Encoders and decoders know the channel and can perform unrestricted quantum operations. No polynomial-time implementation is asserted. In particular, controlled subtraction of the known function $`f`$ is allowed for channel equivalence.

This capacity is not the performance of an unknown-secret learner or a frozen channel with temporal memory.

Set

```math
\tau=\mathrm{diag}\chi,\quad
|\mu\rangle=\sum_e\chi(e)|e\rangle,\quad
c=\sum_e\chi(e)^2,\quad
A=\tau-|\mu\rangle\langle\mu|,\quad
B_N=\frac{\tau+(N-1)|\mu\rangle\langle\mu|}{N}.
```

For a positive, possibly subnormalized matrix, use $`S(X)=-\mathrm{Tr}X\log_2X`$, with $`0\log_20=0`$.

**Theorem C2.** The exact capacity is

```math
\boxed{
Q(\mathcal E_f)=\log_2N+H(\chi)-S(B_N)-(N-1)S(A/N).
}
```

It satisfies

```math
\boxed{
\max\{0,c\log_2N-h_2(c)\}
\le Q(\mathcal E_f)\le c\log_2N.
}
```

If $`\chi`$ is uniform on any $`K`$ distinct outcomes,

```math
\boxed{Q(\mathcal E_f)=(\log_2N)/K.}
```

### Degradability and the optimal input

In a Stinespring isometry, the output retains $`a`$ exactly. Tracing that output removes every off-diagonal input matrix element from the environment. A complementary channel has the form

```math
\mathcal E^c(\omega)=\sum_a\omega_{aa}\eta_a
```

for fixed environment states $`\eta_a`$. Measuring the retained output address and preparing $`\eta_a`$ reproduces the complement. Hence $`\mathcal E`$ is degradable; its complement is entanglement breaking, so it is a Hadamard channel. Standard degradable-channel theory makes its capacity the maximum one-use coherent information.

Controlled output subtraction of $`f(a)`$ converts $`\mathcal E_f`$ to $`\mathcal E_0`$ without changing capacity. The latter is covariant under input permutations and diagonal phase unitaries. Coherent information is invariant under these transformations and concave for a degradable channel. Averaging an input over phases and then permutations produces $`I/N`$ without decreasing coherent information. Thus $`I/N`$ is optimal.

### Choi spectrum

The output at $`I/N`$ is $`I/N\otimes\tau`$, with entropy $`\log_2N+H(\chi)`$. The normalized Choi state, restricted to the subspace spanned by $`|a\rangle_R|a\rangle_A`$, is unitarily equivalent to

```math
\frac1N I_N\otimes A
+|+\rangle\langle+|\otimes|\mu\rangle\langle\mu|.
```

Decompose the address space into the span of $`|+\rangle`$ and its orthogonal complement. The nonzero spectrum consists of $`B_N`$ once and $`A/N`$ repeated $`N-1`$ times. Its entropy is the complementary-output entropy at $`I/N`$. Subtracting gives the stated capacity formula.

### Flagged bounds and uniform noise

Attach a classical output flag to the two branches of the positive decomposition, giving $`\mathcal F`$. Its complement is simulated by reading the flag and, in the measurement branch, the address, so $`\mathcal F`$ is degradable.

For every input $`\omega`$, the measurement branch has equal output and environment entropy. The isometric branch contributes $`S(\omega)`$ to their difference. Thus

```math
I_c(\omega,\mathcal F)=cS(\omega),
\qquad Q(\mathcal F)=c\log_2N.
```

Forgetting the flag gives $`\mathcal E`$, proving the upper bound by data processing. At maximally mixed input, forgetting a classical flag $`F`$ loses $`I(R:F\mid B)\le H(F)=h_2(c)`$ in coherent information. Here $`H(F\mid BR)\ge0`$ because $`F`$ is classical. This proves the lower bound. The endpoint $`c=1`$ is an isometry.

For uniform $`K`$-outcome noise,

```math
|\mu\rangle=K^{-1/2}|u_K\rangle,\qquad
A=K^{-1}(\Pi_K-|u_K\rangle\langle u_K|).
```

The branches have orthogonal label subspaces, so their flag is recoverable without disturbance. Equivalently, the Choi spectrum is $`1/K`$ once and $`1/(NK)`$ with multiplicity $`N(K-1)`$. Both arguments yield $`Q=(\log_2N)/K`$.

## Interpretation and limits

For product errors, $`c=c_0^d`$ gives the upper bound $`Q\le c_0^d\log_2N`$; uniform product noise attains it exactly. This statistical statement does not establish computational hardness of a fixed-width or fixed-support lattice error family.

Independent errors indexed by the full address are part of the model. A common additive shift on all branches defines a different channel: after undoing the known function it is $`\omega\mapsto\omega\otimes\tau`$, preserving the full input capacity. Identical classical transition laws do not determine a unique coherent implementation.

## Primary references

- Brádler, Hayden, Touchette, and Wilde, [*Trade-off capacities of the quantum Hadamard channels*](https://arxiv.org/abs/1001.1732), Physical Review A 81, 062312 (2010): the Hadamard capacity framework.
- Yard, Hayden, and Devetak, [*Capacity Theorems for Quantum Multiple-Access Channels: Classical-Quantum and Quantum-Quantum Capacity Regions*](https://arxiv.org/html/quant-ph/0501045v3), IEEE Transactions on Information Theory 54, 3091–3113 (2008): concavity of coherent information for degradable channels; the linked preprint proves this in Section 7.3 and lists the earlier author order Yard, Devetak, Hayden.
- Kianvash, Fanizza, and Giovannetti, [*Bounding the quantum capacity with flagged extensions*](https://arxiv.org/abs/2008.02461), Quantum 6, 647 (2022): flagged extensions.

The calculation specializes these established tools to the encoding channel above. See [Related work](../references/RELATED_WORK.md) and the [finite verification](../verification/README.md). Finite calculations check the channel identity, reference inputs, Choi spectrum, degradability, and capacity formula; the all-dimension statements follow from the proofs.

