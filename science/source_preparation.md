# Source preparation with a hidden finite seed

The sample model specifies a received quantum state; it does not make preparation of that state free. A source holder can realize the relevant finite-copy experiment without storing a label for every address. Limited independence suffices because a density-matrix element involving $`T`$ copies depends on at most $`2T`$ table entries.

This construction gives the source holder a known classical circuit for generating labels, together with any secret parameter used by that circuit. The receiver obtains sample registers. The label-generation circuit, its inverse, its randomness, and its seed are not additional receiver resources. The distinction is the one fixed in [the model](model.md).

## Preparation assumptions and costs

An address has an injective $`L_A`$-bit encoding and a label has an $`L_Y`$-bit encoding. The source holder has a deterministic classical sampler

```math
\mathsf{Lab}_s(a,r)\in\mathcal Y,
\qquad r\in\{0,1\}^{R},
```

where $`s`$ denotes its fixed private or public problem parameter. For uniform $`r`$, the exact induced conditional law is

```math
P_a(y)=2^{-R}
       \left|\{r:\mathsf{Lab}_s(a,r)=y\}\right|.
```

The reversible implementation cost of this sampler is charged explicitly. Let $`C_{\rm lab}`$ and $`W_{\rm lab}`$ bound its circuit size and workspace, including the computation of any secret-dependent noiseless label. These quantities need not be small for arbitrary conditional laws.

The source also needs a preparation of

```math
|p\rangle=\sum_a\sqrt{p_a}|a\rangle.
```

Its circuit size and workspace are denoted by $`C_p`$ and $`W_p`$. An arbitrary distribution is not assumed to admit an efficient amplitude preparation. Uniform addresses in a product of finite rings or fields do have elementary preparations; general $`p`$ requires an explicit circuit or a separately stated preparation resource. The statistical theorem S1 does not depend on whether the original source is inexpensive to prepare.

For uniform addresses in $`\prod_{j=1}^d\{0,\ldots,q_j-1\}`$, prepare each coordinate by a uniform binary register followed by a range test. Each attempt succeeds with probability greater than one half, or with certainty for a power-of-two range. Exact preparation has expected $`O(\sum_j\log q_j)`$ elementary bit-gate cost. Capping each coordinate at $`K`$ attempts gives an additional failure probability at most $`d2^{-K}`$ and costs $`O(K\sum_j\log q_j)`$ gates. Failure can be assigned a fixed output state and charged to the source error below. This covers the input superpositions used for scalar and coefficient-encoded ring examples.

## Theorem P1: exact finite-copy realization

Fix a copy budget $`T\ge1`$ and the finite-randomness label sampler above. There is a classically seeded family of polynomial-size source circuits such that, after averaging over the hidden seed, its $`T`$-copy density operator is exactly the frozen-table state $`\Omega_T`$ of [S1](frozen_sources.md), provided the input state $`|p\rangle`$ is prepared exactly.

Choose an integer

```math
b\ge\max\{L_A,R,\lceil\log_2(2T)\rceil,1\},
\qquad
Q=2^b,
\qquad
k=2T.
```

Use a public representation of $`\mathbb F_Q`$ and an efficiently computable injective encoding $`\iota:\mathcal A\to\mathbb F_Q`$. A padded address encoding is sufficient. Choose the $`k`$ coefficients of

```math
h_K(x)=K_0+K_1x+\cdots+K_{k-1}x^{k-1}
```

independently and uniformly from $`\mathbb F_Q`$. The seed $`K`$ contains $`kb`$ classical random bits. In a fixed binary basis of the field, let $`\operatorname{bits}_R`$ select $`R`$ coordinates and define the deterministic table

```math
F_K(a)=\mathsf{Lab}_s
       \bigl(a,\operatorname{bits}_R(h_K(\iota(a)))\bigr).
```

Reuse the same seed for the entire $`T`$-copy experiment. The source prepares

```math
|\Psi_K\rangle=\sum_a\sqrt{p_a}|a\rangle|F_K(a)\rangle
```

on each invocation. Then

```math
\mathbb E_K
 \left[\bigl(|\Psi_K\rangle\langle\Psi_K|\bigr)^{\otimes T}\right]
 =\Omega_T.
```

The finite-field polynomial construction is standard limited independence; see [Joffe1974](../references/RELATED_WORK.md#joffe1974). The exact equality here concerns the received finite-copy experiment, not equality of the complete table distributions.

### Independence of polynomial evaluations

For distinct field points $`x_1,\ldots,x_\ell`$, with $`\ell\le k`$, the map from the coefficient vector to
$`(h_K(x_1),\ldots,h_K(x_\ell))`$ is a surjective linear map over $`\mathbb F_Q`$. Its first $`\ell`$ columns form a Vandermonde matrix whose determinant is

```math
\prod_{1\le i<j\le\ell}(x_j-x_i)\ne0.
```

Uniform coefficients therefore give independent uniform evaluations at those points. Selecting $`R`$ fixed binary coordinates preserves independence and yields uniform $`R`$-bit strings. Applying the address-dependent deterministic sampler gives independent labels with the required laws $`P_{a_1},\ldots,P_{a_\ell}`$.

### Why 2T-wise independence is sufficient

A matrix element of the $`T`$-copy density operator is indexed by a ket address tuple $`(a_1,\ldots,a_T)`$ and a bra address tuple $`(b_1,\ldots,b_T)`$. Its random part depends only on the values of the table at addresses in their union, which contains at most $`2T`$ distinct elements. The polynomial family has exactly the same joint label distribution on every such union as a fully independent table. Every matrix element, including those with repeated addresses, therefore agrees. This proves P1.

The equality also covers any protocol receiving at most $`T`$ source copies and processing them adaptively, because such processing is a quantum channel acting on a prefix of this joint state. The source interface does not accept a receiver-chosen address or a superposition query.

## Reversible preparation and resource accounting

Conditional on a classical seed $`K`$, compute $`F_K(a)`$ reversibly in temporary registers, XOR the resulting label into a clean output register, and reverse the temporary computation. This implements

```math
|a\rangle|0\rangle|0\rangle_{\rm work}
 \longmapsto
|a\rangle|F_K(a)\rangle|0\rangle_{\rm work}.
```

The computation uses the source holder's known seed and label circuit. Applying it to $`|p\rangle`$ creates the desired pure graph state without leaving an address-dependent work register entangled with the delivered example.

Horner evaluation uses $`O(k)`$ field operations. Schoolbook binary-field multiplication and reduction have $`O(b^2)`$ reversible elementary-gate cost. Storing Horner intermediates, copying the result, and reversing the evaluation yields a conservative $`O(kb^2)`$ gate bound and $`O(kb)`$ work-bit bound for the hash computation. Thus one sample costs

```math
O\!\left(C_p+kb^2+C_{\rm lab}+L_Y\right)
```

elementary operations, with workspace bounded by

```math
O\!\left(L_A+L_Y+W_p+kb+W_{\rm lab}\right).
```

These bounds include the computation and its reversal. Generating $`T`$ copies with $`k=2T`$ has polynomial total cost when $`T`$, the encoding lengths, the sampler randomness, and the stated circuit costs are polynomial. The $`kb`$-bit seed is sampled once and stored classically for the frozen experiment. No random-access memory containing one entry per address is used.

The field representation is public, including its reduction polynomial, so field arithmetic is part of an ordinary uniform circuit specification. The construction requires such an efficiently supplied representation; it does not use the existence of a field as an unimplemented oracle.

The seed may remain in private classical storage at the source, or in an inaccessible purification register. After it is traced out, the receiver sees the density operator in P1. Revealing the seed, the table, or coherent evaluation access changes the experiment and is not covered by this equality.

## Fresh sources need only pairwise independence

For a source whose label table is refreshed independently on every emission, set $`k=2`$ and draw a new seed for each copy. A single-copy density-matrix element refers to at most two addresses, so pairwise-independent labels reproduce the exact refreshed-source density operator. Independent seeds then reproduce its tensor powers.

An affine polynomial $`h_K(x)=K_0+K_1x`$ therefore suffices for every fresh emission. Reusing that affine seed is a different source: pairwise independence alone does not reproduce an arbitrary frozen $`T`$-copy state. Conversely, the degree-$`(2T-1)`$ construction reproduces a specified frozen experiment without requiring a fresh seed per emission.

The budget dependence is explicit. For each prescribed finite $`T`$, P1 provides a circuit with a seed and running time polynomial in $`T`$. It does not assert that one fixed finite-degree generator reproduces fully independent tables for every possible polynomial number of copies.

## Finite sampling accuracy

The exact construction applies directly to every law generated by a finite uniform random string. Centered-binomial errors and uniform bit labels are examples. A target law with other probabilities can be replaced by an implemented law $`\widetilde P_a`$, but that replacement has a quantitative cost.

Let

```math
\delta_a=\operatorname{TV}(P_a,\widetilde P_a),
\qquad
\delta=\sum_ap_a\delta_a,
```

where total variation is half the classical $`\ell_1`$ distance. The classical one-example laws differ by exactly $`\delta`$. Their $`T`$-sample laws differ by at most $`T\delta`$. Collision probabilities satisfy

```math
|\widetilde c_a-c_a|\le2\delta_a,
\qquad
|\widetilde{\bar c}-\bar c|\le2\delta.
```

For example, couple two independent draws from each law optimally. The equality event used to define collision probability can change only if at least one of the two coupled draws changes, which has probability at most $`2\delta_a`$.

There is also a direct dimension-independent bound for the frozen quantum sources:

```math
D\!\left(\Omega_T(P),\Omega_T(\widetilde P)\right)
 \le\sqrt{1-(1-\delta)^{2T}}
 \le\sqrt{2T\delta}.
```

To prove it, couple $`F(a)`$ and $`\widetilde F(a)`$ optimally and independently across addresses. The overlap of the two conditional pure graph states is the nonnegative random variable

```math
U=\sum_a p_a\,\mathbf1\{F(a)=\widetilde F(a)\},
\qquad
\mathbb E U=1-\delta.
```

The trace distance between their $`T`$-fold tensor powers is $`\sqrt{1-U^{2T}}`$. Convexity of trace distance, concavity of the square root, and convexity of $`u\mapsto u^{2T}`$ give

```math
D\!\left(\Omega_T(P),\Omega_T(\widetilde P)\right)
 \le\mathbb E\sqrt{1-U^{2T}}
 \le\sqrt{1-\mathbb E U^{2T}}
 \le\sqrt{1-(1-\delta)^{2T}}.
```

Thus a desired state error $`\varepsilon`$ is ensured by $`\delta\le\varepsilon^2/(2T)`$. The argument weights changed table entries by their input probabilities; it does not require every entry of an exponentially large table to agree simultaneously.

P1 applied to the finite sampler reproduces $`\Omega_T(\widetilde P)`$ exactly at the distributional level. One can either apply S1 directly using $`\widetilde c_a`$, or use the displayed trace-distance bound to compare with a specified ideal law. Classical hardness assumptions transfer between negligibly close implemented and ideal example distributions by the usual $`T\delta`$ hybrid bound.

### Circuit precision

Suppose the implemented preparation produces a state within trace distance $`\varepsilon_{\rm src}`$ of the ideal conditional state for every seed, and the source emits independent copies conditional on that seed. Tensor telescoping and averaging add at most $`T\varepsilon_{\rm src}`$ to the $`T`$-copy distance. An input-amplitude preparation error is included in this term because subsequent reversible label evaluation preserves trace distance.

If the receiver is compared with the bounded simulator of [simulator.md](simulator.md), whose own error is $`\varepsilon_{\rm sim}`$, one valid complete budget relative to the ideal label laws is

```math
D(\widetilde\Omega_T,\widetilde\sigma_T)
 \le 1-w_T
      +\sqrt{2T\delta}
      +T\varepsilon_{\rm src}
      +\varepsilon_{\rm sim}.
```

Here $`\widetilde\sigma_T`$ is fed classical examples from the ideal laws used in $`w_T`$. If both the actual source and the classical examples use the same implemented finite laws, apply S1 to those laws instead and omit the label-law comparison term.

## Elementary finite samplers and padded labels

A uniform value in a range whose size is not a power of two can be approximated with a fixed random-string length. Divide the string into $`K`$ blocks of $`\lceil\log_2M\rceil`$ bits, accept the first block below $`M`$, and use a fixed value if every block fails. Each block succeeds with probability greater than one half. The induced law has total-variation distance at most $`2^{-K}`$ from the uniform law on the range. The entire routine is a deterministic bounded circuit in its random input, so it fits P1. A general target distribution still requires an explicit efficient finite sampler; the theorem does not provide one automatically.

For the padded scalar-LWE example in [lattice examples](lattice_examples.md), suppose the base error sampler uses $`R_0`$ random bits and induces the exact finite law $`\widetilde\chi`$. Reserve a further $`m`$ independent random bits for the additional label coordinates and set

```math
\mathsf{Lab}_s(a,r_0,z)
   =\bigl(a\cdot s+\mathsf{Err}(r_0)\bmod q,\ z\bigr),
\qquad z\in\{0,1\}^m.
```

The added labels have noiseless value zero and independent uniform bit errors at each address. They require $`m`$ additional output bits and no nontrivial sampling arithmetic. Taking $`R=R_0+m`$ in P1 gives the exact conditional collision probability

```math
c=\left(\sum_e\widetilde\chi(e)^2\right)2^{-m}.
```

For a frozen source, the same polynomial seed fixes these address-dependent labels throughout the copy budget. For a fresh source, independent affine seeds refresh them on each emission. This preparation is the address-dependent extra-label experiment used by the theorem; a single independent register tensored onto every source state would be a different preparation.
