# Frozen noisy sources

A source can reuse the same noisy label table while emitting many copies of a pure quantum example. The copies then retain correlations that are absent when the table is refreshed. Theorem S1 accounts for those correlations: a quantum simulator can reproduce the entire received state, up to an explicit trace-distance bound, using the same number of ordinary classical examples.

The theorem concerns the sample access defined in [the model](model.md). The simulator is a quantum algorithm whose input consists of classical examples. It does not turn a quantum learner into a classical computation.

## Distributions and states

Let $`\mathcal A`$ and $`\mathcal Y`$ be finite address and label alphabets. Write $`p_a`$ for the address probabilities, with $`\sum_a p_a=1`$, and $`P_a(y)`$ for the conditional label distribution at address $`a`$. Draw a random table $`F`$ by choosing the variables $`F(a)\sim P_a`$ independently across addresses. Conditional on this table, the source emits the normalized pure state

```math
|\Psi_F\rangle
   =\sum_{a\in\mathcal A}\sqrt{p_a}\,|a\rangle|F(a)\rangle.
```

The table is chosen once and reused for all $`T`$ copies. A receiver without the table sees

```math
\Omega_T
   =\mathbb E_F\left[
       \bigl(|\Psi_F\rangle\langle\Psi_F|\bigr)^{\otimes T}
     \right].
```

The ordinary classical example distribution is $`\Pr[A=a,Y=y]=p_aP_a(y)`$. Its examples use independent draws of this joint distribution. These classical examples can disagree at a repeated address; the simulator explicitly handles that event.

Define the conditional label collision probabilities, the address collision probability, and the averaged label collision probability by

```math
c_a=\sum_{y\in\mathcal Y}P_a(y)^2,
\qquad
\alpha=\sum_a p_a^2,
\qquad
\bar c=\sum_a p_ac_a.
```

Throughout, $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Let $`\mathcal I_T`$ be the set of ordered $`T`$-tuples of pairwise distinct addresses, and set

```math
w_T
   =\sum_{(a_1,\ldots,a_T)\in\mathcal I_T}
        \prod_{i=1}^T p_{a_i}(1-c_{a_i}).
```

An empty sum is zero. In particular, $`w_T=0`$ whenever $`T`$ exceeds the number of addresses with positive probability.

## Theorem S1: simulation from exactly T classical examples

For every choice of $`p_a`$, $`P_a`$, and integer $`T\ge1`$, there is a quantum simulator using exactly $`T`$ independent classical examples whose output $`\sigma_T`$ satisfies

```math
D(\Omega_T,\sigma_T)
   \le 1-w_T
   \le \min\!\left\{1,
          T\bar c+\binom{T}{2}\alpha
        \right\}.
```

The simulator does not require a description of the distributions or of the hidden table. If the received addresses are distinct, it prepares the uniform coherent superposition of all permutations of the received examples. If any address repeats, it outputs a fixed state of the appropriate dimension. It never requests replacement examples.

The simulator has polynomial cost in $`T`$ and the encoded length of an example. [The simulator construction](simulator.md) gives the normalization, reversible circuit, and finite-accuracy costs. A bounded circuit implementation within trace distance $`\varepsilon_{\rm sim}`$ of the ideal simulator obeys the same bound with $`\varepsilon_{\rm sim}`$ added.

## Proof

### Centered label vectors

For each address, define the mean label vector, the diagonal label density operator, and its centered covariance:

```math
|m_a\rangle=\sum_yP_a(y)|y\rangle,
\qquad
B_a=\sum_yP_a(y)|y\rangle\langle y|,
\qquad
K_a=B_a-|m_a\rangle\langle m_a|.
```

The covariance is positive. Indeed, for any vector $`|u\rangle`$,

```math
\langle u|K_a|u\rangle
 =\mathbb E\bigl[|\langle u|F(a)\rangle|^2\bigr]
  -\bigl|\mathbb E\langle u|F(a)\rangle\bigr|^2
 \ge0.
```

The relevant traces are

```math
\langle m_a|m_a\rangle=c_a,
\qquad
\mathrm{Tr}B_a=1,
\qquad
\mathrm{Tr}K_a=1-c_a.
```

Write the source vector as its mean plus independent centered address blocks:

```math
|M\rangle=\mathbb E_F|\Psi_F\rangle
   =\sum_a\sqrt{p_a}|a\rangle|m_a\rangle,
\qquad
|\zeta_F\rangle=|\Psi_F\rangle-|M\rangle.
```

Thus the random label vector at address $`a`$ in $`\zeta_F`$ is
$`|\xi_a\rangle=|F(a)\rangle-|m_a\rangle`$, with $`\mathbb E|\xi_a\rangle=0`$ and $`\mathbb E|\xi_a\rangle\langle\xi_a|=K_a`$.

### A positive component of the full frozen source

Let $`\Pi_T`$ project onto the subspace in which the $`T`$ address registers are pairwise distinct. Define

```math
|v_F\rangle=\Pi_T|\zeta_F\rangle^{\otimes T},
\qquad
|w_F\rangle=|\Psi_F\rangle^{\otimes T}-|v_F\rangle,
\qquad
C_T=\mathbb E_F|v_F\rangle\langle v_F|.
```

The operator cross term vanishes:

```math
\mathbb E_F|v_F\rangle\langle w_F|=0.
```

To verify this identity, expand the bra of $`(|M\rangle+|\zeta_F\rangle)^{\otimes T}`$. Every ket term in $`v_F`$ contains centered random variables at $`T`$ distinct addresses. A nonzero expectation requires each of these addresses to occur as a centered variable in the bra. If an address occurs only through a deterministic mean vector in the bra, its centered ket factor still has zero expectation. Since the bra contains at most $`T`$ centered factors, survival forces exactly $`T`$ centered factors at precisely those distinct addresses. Those are exactly the terms retained in $`v_F`$ and removed from $`w_F`$. Independence across addresses proves the cancellation, including bra terms with repeated addresses.

It follows globally, without conditioning on distinct addresses, that

```math
\Omega_T
 =C_T+\mathbb E_F|w_F\rangle\langle w_F|
 \succeq C_T.
```

Orthogonality of different address strings and independence of the table entries give

```math
\mathrm{Tr}C_T
 =\sum_{\mathbf a\in\mathcal I_T}
      \prod_{i=1}^T
        p_{a_i}\,\mathbb E\langle\xi_{a_i}|\xi_{a_i}\rangle
 =w_T.
```

### The same positive component in the simulator

For an ordered tuple $`\mathbf a=(a_1,\ldots,a_T)\in\mathcal I_T`$, define an isometry on label registers by

```math
V_{\mathbf a}|y_1,\ldots,y_T\rangle
 =\frac1{\sqrt{T!}}
    \sum_{\pi\in S_T}
       |a_{\pi(1)},y_{\pi(1)}\rangle\otimes\cdots\otimes
       |a_{\pi(T)},y_{\pi(T)}\rangle.
```

Distinct addresses make different permutation strings orthogonal. In the inner product of two such outputs, only equal permutations survive, so $`V_{\mathbf a}^{\dagger}V_{\mathbf a}=I`$. This remains true for arbitrary quantum label inputs, not only computational basis labels.

The covariance expression for $`C_T`$ is

```math
C_T
 =\sum_{\mathbf a\in\mathcal I_T}
       \left(\prod_{i=1}^Tp_{a_i}\right)
       V_{\mathbf a}
          \left(\bigotimes_{i=1}^T K_{a_i}\right)
       V_{\mathbf a}^{\dagger}.
```

For completeness, a matrix element on the left vanishes unless its two address tuples are permutations of one another: otherwise an unmatched centered variable has zero mean. For matching tuples, each shared address contributes $`K_a`$. On the right, the $`T!`$ possible ordered representatives of the same distinct-address set cancel the factor $`1/T!`$ from the two isometry amplitudes. The weights $`\prod_i p_{a_i}`$ are invariant under permutation. This proves the identity with its stated normalization.

Let $`r_T=\sum_{\mathbf a\in\mathcal I_T}\prod_i p_{a_i}`$ be the probability of distinct addresses and let $`\tau_{\rm fail}`$ be the fixed fallback density operator. The actual simulator state is

```math
\sigma_T
 =\sum_{\mathbf a\in\mathcal I_T}
       \left(\prod_{i=1}^Tp_{a_i}\right)
       V_{\mathbf a}
          \left(\bigotimes_{i=1}^T B_{a_i}\right)
       V_{\mathbf a}^{\dagger}
   +(1-r_T)\tau_{\rm fail}.
```

Each $`B_a=K_a+|m_a\rangle\langle m_a|`$ is a sum of positive operators. Expanding the tensor product shows that its all-$`K`$ term is a positive component. Consequently $`\sigma_T\succeq C_T`$. Both $`\Omega_T`$ and $`\sigma_T`$ have trace one, and their residuals after subtracting $`C_T`$ are positive with trace $`1-w_T`$. Therefore

```math
\frac12\|\Omega_T-\sigma_T\|_1
 \le\frac12\left(
       \|\Omega_T-C_T\|_1+\|\sigma_T-C_T\|_1
     \right)
 =1-w_T.
```

### Collision bound and boundary cases

Draw $`A_1,\ldots,A_T`$ independently from $`p`$. Conditional on those addresses, introduce independent auxiliary failure events with probabilities $`c_{A_i}`$. Then $`w_T`$ is the probability that the addresses are distinct and none of these failures occurs. A union bound gives

```math
1-w_T
 \le\sum_{i=1}^T\mathbb E c_{A_i}
     +\sum_{1\le i<j\le T}\Pr[A_i=A_j]
 =T\bar c+\binom{T}{2}\alpha.
```

If $`T`$ exceeds the support size of $`p`$, the simulator always takes its fallback branch, $`C_T=0`$, and the theorem reduces to $`D\le1`$. No distinct-address isometry needs to be constructed on an impossible branch. For $`T=1`$, the bound is $`D\le\bar c`$; the sharper exact single-copy expression is given by [Theorem F1](refreshed_sources.md). With the empty-tensor convention, the zero-copy case has identical outputs and distance zero.

## Uniform additive noise

Suppose addresses are uniform on a set of size $`N`$ and labels have the form $`f(a)+E_a`$ in a finite abelian group, where $`E_a`$ has distribution $`\chi`$. Translation leaves collision probability unchanged:

```math
c_a=c=\sum_e\chi(e)^2,
\qquad
\bar c=c,
\qquad
\alpha=\frac1N.
```

For $`T\le N`$,

```math
w_T=\frac{(N)_T}{N^T}(1-c)^T,
\qquad
D(\Omega_T,\sigma_T)
 \le1-\frac{(N)_T}{N^T}(1-c)^T
 \le Tc+\frac{T(T-1)}{2N}.
```

Set $`(N)_T=0`$ for $`T>N`$. The function $`f`$ need not be linear. Product error laws give $`c=\prod_j\sum_e\chi_j(e)^2`$, with collisions computed on the actual encoded label alphabet. [Lattice examples](lattice_examples.md) apply this statement to scalar and ring learning problems.

## Operational meaning

Any receiver using at most $`T`$ source copies can be supplied with the simulator output instead. Trace-distance contractivity bounds the change in every output event by the theorem's right-hand side, including joint measurements, quantum memory, and adaptive processing between sample arrivals. A receiver that stops early can be padded to $`T`$ copies. This is a statement about sample delivery; it does not supply a coherent value-query oracle, its inverse, the random table, or a seed register.

For a family indexed by a security or learning parameter, negligible $`\bar c`$ and negligible $`\alpha`$ make the simulation error negligible for every polynomial copy budget. Efficient learning from these quantum examples would then give efficient quantum learning from ordinary classical examples. Low collision probability is a sufficient simulation condition, not a necessary-and-sufficient criterion for learnability.

Coherent permutation simulation for fixed random-phase coupon states was established by Goyal, Malavolta, and Roberts [GMR2025, Theorem 3](../references/RELATED_WORK.md#gmr2025). The present comparison uses the common positive centered-covariance component of stochastic classical labels. The inherited symmetrization mechanism and the distinction between the source models are discussed in [related work](../references/RELATED_WORK.md). [Source preparation](source_preparation.md) gives finite-seed realizations of the present experiment and bounds their approximation error.
