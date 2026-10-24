# The classical-sample simulator

The simulator in [Theorem S1](frozen_sources.md) receives exactly $`T`$ independent classical examples. It prepares a quantum state from that finite list and supplies the state to the original receiver. All quantum computation remains available to the receiver. The replacement concerns access to examples, not the receiver's computational model.

Let an address and a label use $`L_A`$ and $`L_Y`$ bits, and put $`L=L_A+L_Y`$. Encodings are injective. The simulator uses the received list of $`T`$ records as classical circuit data; it has no access to the hidden table or an exponentially large memory.

## Exact-T procedure

Read $`(a_1,y_1),\ldots,(a_T,y_T)`$ and test whether the addresses are pairwise distinct. On a repeated address, output a fixed density operator $`\tau_{\rm fail}`$ on the $`T`$-example register. The all-zero state in the encoded register space is one choice. On distinct addresses, output

```math
|\mathrm{Sym}(\mathbf a,\mathbf y)\rangle
 =\frac1{\sqrt{T!}}\sum_{\pi\in S_T}
      |a_{\pi(1)},y_{\pi(1)}\rangle\otimes\cdots\otimes
      |a_{\pi(T)},y_{\pi(T)}\rangle.
```

The $`T!`$ summands are orthogonal because their address strings differ, even when some labels are equal. The state is therefore normalized as written. The failure branch consumes no additional examples. Internal randomness used to prepare the permutation register is separate from the classical example supply.

For $`T=1`$, the output is simply the single classical example encoded in the computational basis. If $`T`$ exceeds the number of possible positive-probability addresses, the failure branch is always taken. The construction is still defined, and the theorem gives its corresponding trivial distance bound.

## A uniform permutation register

A uniform permutation can be encoded by the Fisher–Yates choices

```math
R_j\in\{1,\ldots,j\},\qquad j=T,T-1,\ldots,2.
```

Starting with the list $`(1,\ldots,T)`$, swap positions $`j`$ and $`R_j`$ at step $`j`$. The map from the choice string to the final permutation is a bijection. There are $`\prod_{j=2}^Tj=T!`$ choice strings, and each permutation determines its choices by locating the required tags successively. Both directions are computable in polynomial time.

Prepare the independent registers

```math
|u_j\rangle=\frac1{\sqrt j}\sum_{r=1}^j|r\rangle.
```

Their tensor product is uniform over the choice strings. Reversibly compute the permutation, copy its encoding to a clean register, and clear the choice and work registers using the efficiently computable inverse map. The resulting register is

```math
\frac1{\sqrt{T!}}\sum_{\pi\in S_T}|\pi\rangle.
```

This change of encoding is an ordinary reversible computation with a known inverse. It does not require an operation that erases an unknown function value.

### Exact expected-time and bounded-circuit versions

There is a simple exact preparation of $`|u_j\rangle`$ using Hadamard gates, reversible comparisons, and measurements on local preparation registers. Set $`b_j=\lceil\log_2j\rceil`$, prepare a uniform $`b_j`$-bit string in superposition, and test whether its value is below $`j`$. Conditional on acceptance, the state is exactly uniform on the desired range. Acceptance probability is $`j/2^{b_j}>1/2`$ unless the range already fills the register, in which case it is one. A rejected register can be reset and retried before it interacts with the examples. Fewer than two attempts are needed in expectation.

For a deterministic gate budget, allow at most $`K`$ attempts for each of the $`T-1`$ choice registers. If any preparation fails, output $`\tau_{\rm fail}`$. The probability of this additional failure is at most

```math
(T-1)2^{-K}.
```

Conditional on success, every choice register is exactly uniform, so the successful branch produces the exact target permutation state. Choosing

```math
K=\left\lceil\log_2\frac{T-1}{\varepsilon_{\rm sim}}\right\rceil
```

for $`T>1`$ and $`0<\varepsilon_{\rm sim}<1`$ makes the simulator's implementation error at most $`\varepsilon_{\rm sim}`$ in trace distance. This gives a bounded circuit with an explicit error budget using a finite exact gate set. No rotation with an unspecified precision is hidden in the preparation. The case $`T=1`$ needs no permutation register or retry procedure.

## Writing the examples and clearing the permutation

Let $`\pi=(\pi(1),\ldots,\pi(T))`$ be the chosen encoding. Because the list of received examples is classical, the simulator can implement the reversible computation

```math
|\pi\rangle|0\rangle
 \longmapsto
|\pi\rangle
 |a_{\pi(1)},y_{\pi(1)},\ldots,a_{\pi(T)},y_{\pi(T)}\rangle.
```

For each output position, a circuit can scan all $`T`$ list entries, compare the index against the stored index, and conditionally XOR the corresponding record into the output. The list supplies ordinary classical constants to this circuit. A linear scan is sufficient; quantum random-access memory is unnecessary.

The original list of distinct addresses gives an efficient inverse on the image of this computation. For each output address, compare it with $`a_1,\ldots,a_T`$ and recover its unique original index. These recovered indices determine $`\pi`$. Compute them coherently from the output addresses, XOR them into the permutation register, and clear the inverse-computation workspace. The permutation register is left in its fixed zero state. The output alone is the desired coherent permutation state.

The inverse uses only the distinct address strings, not the labels or a hidden function. Every received noisy label is retained in the output. The procedure therefore does not assume that unknown noisy output coordinates can be uncomputed.

## The label-register isometry

For the proof of S1, fix a distinct address tuple $`\mathbf a`$ and regard the labels as arbitrary quantum inputs. Define

```math
V_{\mathbf a}|y_1,\ldots,y_T\rangle
  =|\mathrm{Sym}(\mathbf a,\mathbf y)\rangle.
```

For two computational basis label tuples $`\mathbf y`$ and $`\mathbf z`$,

```math
\langle\mathbf z|
   V_{\mathbf a}^{\dagger}V_{\mathbf a}
 |\mathbf y\rangle
 =\frac1{T!}\sum_{\pi,\sigma\in S_T}
      \prod_{i=1}^T
         \langle a_{\sigma(i)}|a_{\pi(i)}\rangle
         \langle z_{\sigma(i)}|y_{\pi(i)}\rangle
 =\prod_{i=1}^T\delta_{z_i,y_i}.
```

Distinct addresses force $`\sigma=\pi`$, proving $`V_{\mathbf a}^{\dagger}V_{\mathbf a}=I`$. Consequently the map $`X\mapsto V_{\mathbf a}XV_{\mathbf a}^{\dagger}`$ preserves trace and positivity on all label operators. This is the property needed when the proof decomposes label densities into centered covariances and mean outer products.

An implementation on arbitrary quantum label registers can initialize the fixed address registers, apply a permutation coherently to the address-label pairs, and clear the permutation using the same address inverse. No label is copied or measured in that implementation. The classical-record implementation above is sufficient for the actual simulator.

## State formula and the collision branch

Using the notation of S1, let

```math
B_a=\sum_yP_a(y)|y\rangle\langle y|,
\qquad
r_T=\sum_{\mathbf a\in\mathcal I_T}\prod_i p_{a_i}.
```

The ideal output is exactly

```math
\sigma_T
 =\sum_{\mathbf a\in\mathcal I_T}
       \left(\prod_i p_{a_i}\right)
       V_{\mathbf a}\left(\bigotimes_iB_{a_i}\right)
       V_{\mathbf a}^{\dagger}
   +(1-r_T)\tau_{\rm fail}.
```

There is no division by $`r_T`$: the simulator is not conditioned on a successful address draw. The distinct branch has trace $`r_T`$, and the fallback has trace $`1-r_T`$. This normalization is why S1 uses exactly $`T`$ classical examples and incurs only the collision term already present in its bound.

## Circuit and storage costs

Pairwise address comparison takes $`O(T^2L_A)`$ classical bit operations. Straightforward scans for the forward and inverse record maps take $`O(T^2(L+\log T))`$ reversible elementary operations. A reversible implementation of the permutation encoding and its inverse also has polynomial cost; a direct list implementation fits the same quadratic scan bound. The bounded preparation of the uniform choice registers adds $`O(T\log T\log(T/\varepsilon_{\rm sim}))`$ elementary operations. These are conservative unoptimized bounds.

The received classical list has size $`TL`$ bits, and the quantum output has size $`TL`$ qubits. The permutation and reversible work registers require polynomial additional space; a direct implementation uses at most $`O(TL+T^2\log T)`$ quantum bits including the output. The gate count includes reading the polynomial-size received list. It assumes neither constant-time access to a large unseen database nor free preparation of the original source.

All circuit choices depend on the received examples, their encodings, $`T`$, and the requested accuracy. They do not depend on the hidden secret, the unobserved table, or a description of the example distribution. The construction therefore gives a uniform quantum simulation whenever example lengths and the receiver's copy budget are polynomially bounded.

## Relation to the inherited symmetrizer

Goyal, Malavolta, and Roberts [GMR2025, Theorem 3](../references/RELATED_WORK.md#gmr2025) establish a classical-sample simulation for coupon states with fixed hidden random phases using coherent permutation states. The present simulator uses that symmetrization mechanism on the distinct-address branch. Its comparison with a stochastic-label source is established by the positive common component in [S1](frozen_sources.md), rather than by assuming random phases in the source. The finite-budget source that S1 simulates is constructed separately in [source preparation](source_preparation.md).
