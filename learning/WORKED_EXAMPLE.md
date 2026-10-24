# Two addresses, two labels: a worked quantum-example experiment

A source with two possible inputs and two possible labels is small enough to write out completely. It already shows why the same one-copy density operator can describe different repeated-copy experiments, and why a simulator supplied classical records may need to preserve quantum coherence between their permutations.

The [Watrous reading map](ANCHOR.md#reading-map) supplies the background on registers, density operators, trace norm and permutation symmetry. The [source-to-project bridge](BRIDGE.md) explains how those tools enter the general argument. The calculations below instantiate the repository's model; their labels contain no unknown signal, so they make no cryptographic hardness claim.

<a id="registers-and-tables"></a>

## 1. Registers and the four possible tables

Each example has an **address register** $`A`$ and a **label register** $`Y`$. Both are qubits, with basis values $`0`$ and $`1`$. The notation $`|a,y\rangle=|a\rangle_A\otimes|y\rangle_Y`$ names a basis vector of the combined four-dimensional space.

The address distribution is uniform. Independently choose the two table entries $`F(0),F(1)`$, each as a fair bit, and prepare

```math
|\psi_F\rangle
=\frac{|0,F(0)\rangle+|1,F(1)\rangle}{\sqrt2}.
```

There are four equally likely tables:

| Table entries $`(F(0),F(1))`$ | Conditional pure example |
|---|---|
| $`(0,0)`$ | $`(\lvert0,0\rangle+\lvert1,0\rangle)/\sqrt2`$ |
| $`(0,1)`$ | $`(\lvert0,0\rangle+\lvert1,1\rangle)/\sqrt2`$ |
| $`(1,0)`$ | $`(\lvert0,1\rangle+\lvert1,0\rangle)/\sqrt2`$ |
| $`(1,1)`$ | $`(\lvert0,1\rangle+\lvert1,1\rangle)/\sqrt2`$ |

Each row specifies a coherent superposition over addresses. The source chooses its row classically and keeps that choice hidden. A frozen source reuses the row for every emission. A refreshed source chooses a new independent row before each emission.

An ordinary classical example draws an address and a fresh fair-bit label. Its four possible records $`(a,y)`$ are equally likely. Encoding one such record as a basis state gives

```math
\rho_{\mathrm{cl}}
=\frac14\sum_{a,y\in\{0,1\}}|a,y\rangle\langle a,y|
=\frac{I_4}{4}.
```

The simulator receives independent classical draws of this distribution. In particular, two of its records can have the same address and different labels. A frozen table has only one label at each address. The simulator's collision branch will handle that difference.

The [model](../science/model.md) fixes these source and access conventions.

<a id="one-copy-average"></a>

## 2. Averaging one example

For one emission, the receiver sees the average over the four hidden tables,

```math
\rho=\frac14\sum_{f_0,f_1\in\{0,1\}}
|\psi_{f_0f_1}\rangle\langle\psi_{f_0f_1}|.
```

Use the ordered basis $`|0,0\rangle,|0,1\rangle,|1,0\rangle,|1,1\rangle`$. Direct averaging gives

```math
\rho
=\frac18
\begin{pmatrix}
2&0&1&1\\
0&2&1&1\\
1&1&2&0\\
1&1&0&2
\end{pmatrix}
=\frac14
\begin{pmatrix}
I_2&J_2/2\\
J_2/2&I_2
\end{pmatrix},
\qquad
J_2=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
```

The two-by-two blocks group entries by address. The diagonal entries are $`1/4`$, agreeing with the classical data. The off-diagonal address blocks retain coherence: every particular pair of labels occurs together in one quarter of the tables. Its matrix element in that table's pure state is $`1/2`$, giving $`1/8`$ after averaging.

The same-address off-diagonal entries vanish. A given table assigns only one label to that address; it never places both labels there in superposition.

This is the same one-copy average for fresh and frozen sources. Their difference appears when several emissions are considered together.

<a id="distance"></a>

## 3. Spectrum and the exact distance of one quarter

Define the two basis combinations

```math
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
```

The label matrix $`J_2`$ has eigenvalue $`2`$ on $`|+\rangle_Y`$ and eigenvalue zero on $`|-\rangle_Y`$. Consequently:

- On the label-$`|+\rangle`$ sector, the address matrix is $`\frac14\begin{pmatrix}1&1\\1&1\end{pmatrix}`$, with eigenvalues $`1/2`$ and zero.
- On the label-$`|-\rangle`$ sector, the address matrix is $`I_2/4`$, with eigenvalues $`1/4`$ and $`1/4`$.

Thus

```math
\mathrm{spec}(\rho)
=\left\{\frac12,\frac14,\frac14,0\right\}.
```

Because $`\rho_{\mathrm{cl}}=I_4/4`$, subtracting it shifts every eigenvalue by $`-1/4`$. The difference has spectrum $`\{1/4,0,0,-1/4\}`$. The trace norm of a Hermitian matrix is the sum of the absolute values of its eigenvalues, so the project's half trace distance is

```math
D(\rho,\rho_{\mathrm{cl}})
=\frac12\|\rho-\rho_{\mathrm{cl}}\|_1
=\frac12\left(\frac14+\frac14\right)
=\frac14.
```

For this label law, two independent labels agree with probability

```math
c=\left(\frac12\right)^2+\left(\frac12\right)^2=\frac12.
```

The result is exactly [F1](../science/refreshed_sources.md)'s uniform-input formula:

```math
D(\rho,\rho_{\mathrm{cl}})
=c\left(1-\frac1N\right)
=\frac12\left(1-\frac12\right)
=\frac14.
```

Operationally, $`1/4`$ is the largest possible difference between the acceptance probabilities of a binary measurement on these two states. This is a statement about the supplied states and all possible subsequent measurements.

<a id="two-copy-schedules"></a>

## 4. Two copies distinguish fresh from frozen

There are now two whole example registers, each containing an address and a label. The two source schedules produce

```math
\rho_{\mathrm{fresh},2}=\rho\otimes\rho,
\qquad
\Omega_2
=\frac14\sum_{f_0,f_1\in\{0,1\}}
\bigl(|\psi_{f_0f_1}\rangle\langle\psi_{f_0f_1}|\bigr)^{\otimes2}.
```

The **swap test** exchanges the two whole examples. If $`S`$ is that exchange operator, its acceptance operator is $`(I+S)/2`$. For two independent copies of a density operator,

```math
\Pr[\mathrm{accept}\mid\rho\otimes\rho]
=\frac{1+\mathrm{Tr}(\rho^2)}2.
```

The spectrum above gives

```math
\mathrm{Tr}(\rho^2)
=\left(\frac12\right)^2
 +\left(\frac14\right)^2
 +\left(\frac14\right)^2
=\frac38,
```

and hence

```math
\Pr[\mathrm{accept}\mid\mathrm{fresh}]
=\frac{1+3/8}{2}
=\frac{11}{16}.
```

For a frozen table, the conditional input is always $`|\psi_F\rangle\otimes|\psi_F\rangle`$. Swapping its two factors leaves it unchanged. Acceptance is therefore one for every table, and remains one after averaging:

```math
\Pr[\mathrm{accept}\mid\mathrm{frozen}]=1.
```

Averaging first and then taking a tensor product has discarded a correlation that the swap test detects. This explains why a simulator for frozen examples needs a joint output with the appropriate permutation coherence. The [bridge on source schedules](BRIDGE.md#experiment) and [S1](../science/frozen_sources.md) retain that distinction throughout.

<a id="simulator"></a>

## 5. A simulator using exactly two classical records

Draw exactly two ordinary records, $`(a_1,y_1)`$ and $`(a_2,y_2)`$. The simulator performs quantum operations on their known bit strings.

If the addresses differ, prepare

```math
\frac{
|a_1,y_1\rangle|a_2,y_2\rangle
+
|a_2,y_2\rangle|a_1,y_1\rangle
}{\sqrt2}.
```

The two summands are orthogonal because their addresses differ. A control qubit in $`|+\rangle`$ and a controlled swap create the two orders coherently. The first output address then identifies the order, allowing the control to be cleared using the known address list. No hidden table is needed.

If the addresses agree, output the fixed fallback

```math
|0,0\rangle^{\otimes2}.
```

The simulator requests no replacement records. It consumes its two supplied examples and emits an output on both branches.

For uniform binary addresses, the distinct-address and collision probabilities are each $`1/2`$. Write

```math
|S_{yz}\rangle
=\frac{
|0,y\rangle|1,z\rangle+
|1,z\rangle|0,y\rangle
}{\sqrt2}.
```

The simulator's complete averaged output is

```math
\sigma_2
=\frac12\bigl(|0,0\rangle\langle0,0|\bigr)^{\otimes2}
+\frac18\sum_{y,z\in\{0,1\}}
|S_{yz}\rangle\langle S_{yz}|.
```

Its trace is $`1/2+4/8=1`$. Every branch is unchanged by exchanging the two examples, including the fallback. The simulator therefore passes the swap test with probability one, just as the frozen source does.

Matching this test alone does not establish closeness under every measurement. The positive-operator argument supplies that stronger comparison. The [canonical simulator construction](../science/simulator.md) gives the general circuit and its costs.

<a id="common-component"></a>

## 6. A common positive component of weight one eighth

At either address, the random label is the basis vector $`|0\rangle`$ or $`|1\rangle`$, each with probability $`1/2`$. Its mean vector and second moment are

```math
|m\rangle=\frac{|0\rangle+|1\rangle}{2},
\qquad
B=\frac{I_2}{2}.
```

The mean vector has squared norm $`c=1/2`$; it is not normalized. The centered covariance is

```math
K_a=B-|m\rangle\langle m|
=\frac14
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
=\frac12|-\rangle\langle-|.
```

The same covariance occurs at each address $`a=0,1`$. Each $`K_a`$ is positive semidefinite, with eigenvalues $`1/2`$ and zero, and trace $`1/2=1-c`$.

For distinct addresses, let $`V`$ send label basis vectors $`|y,z\rangle`$ to the states $`|S_{yz}\rangle`$ above. These four images are orthonormal, so $`V`$ is an isometry. The common component used by S1 becomes

```math
C_2=\frac12\,V(K_0\otimes K_1)V^\dagger,
\qquad
\mathrm{Tr}C_2
=\frac12\left(\frac12\right)^2
=\frac18.
```

The leading $`1/2`$ is the probability of distinct addresses. The other two factors are the covariance traces for the two labels.

Independence and covariance positivity place this component inside both experiments. On the source side, center each random label by subtracting its mean. Independence makes cross terms between the fully centered, distinct-address contribution and its remaining terms vanish after averaging. On the simulator side, the identities $`B=K_a+|m\rangle\langle m|`$ expand $`B\otimes B`$ into positive terms, one of which is $`K_0\otimes K_1`$. The collision fallback adds another positive term. The [S1 proof](../science/frozen_sources.md) establishes these two inclusions:

```math
\Omega_2\succeq C_2,
\qquad
\sigma_2\succeq C_2.
```

Here positive order means that each difference is positive semidefinite. Its trace norm therefore equals its trace. Removing the common component leaves two positive remainders, each of trace $`7/8`$, giving

```math
D(\Omega_2,\sigma_2)
\le\frac12\left(
\mathrm{Tr}(\Omega_2-C_2)
+\mathrm{Tr}(\sigma_2-C_2)
\right)
=\frac78.
```

Equivalently, the theorem's weight is

```math
w_2=\frac{(2)_2}{2^2}(1-c)^2
=\frac{2\cdot1}{4}\left(\frac12\right)^2
=\frac18.
```

This small example gives a loose accuracy guarantee: address repetitions are frequent, and each label's centered covariance retains only half its second-moment weight. The simpler union bound would give $`2c+\alpha=3/2`$, reducing to the trivial bound of one, while the common-component expression gives $`7/8`$.

The bound concerns the specified distribution-independent simulator. Because the uniform label law is known in this example, a different procedure could sample a table locally and prepare repeated copies directly. The example illustrates the generic comparison without asserting that its error is unavoidable.

<a id="larger-parameters"></a>

## 7. A regime where the bound is small

Keep uniform addresses and independent uniform labels, but take

```math
N=2^{20},\qquad K=2^{16},\qquad T=32.
```

There are $`N`$ possible addresses and $`K`$ possible labels at each address. Uniform labels have collision probability $`c=1/K=2^{-16}`$, and uniform addresses have collision probability $`\alpha=1/N=2^{-20}`$.

The two terms in S1's simple bound are

```math
Tc=\frac{32}{65536}=\frac1{2048},
```

```math
\binom{T}{2}\alpha
=\frac{496}{1048576}
=\frac{31}{65536}.
```

Therefore

```math
D(\Omega_{32},\sigma_{32})
\le\frac{63}{65536}
=0.0009613037109375
<0.001.
```

The statement concerns the entire 32-copy experiment after averaging over the hidden table. Any final binary test, including a joint quantum measurement, changes its acceptance probability by less than $`0.001`$ under this replacement.

These numbers illustrate a statistical simulation bound. A learning consequence with an unknown signal additionally uses the assumptions specified in [L1–L3](../science/lattice_examples.md).

<a id="finite-seed"></a>

## 8. Realizing the 32-copy source with a finite seed

A table with $`2^{20}`$ entries need not be stored explicitly to reproduce this experiment. In [P1](../science/source_preparation.md), a matrix element of the 32-copy state depends on labels at at most 64 addresses: the addresses appearing on its ket and bra sides.

Uniform 16-bit labels use $`R=16`$ random bits per address. The address encoding uses $`L_A=20`$ bits. P1 chooses

```math
k=2T=64,
\qquad
b=\max\{L_A,R,\lceil\log_2(2T)\rceil,1\}
=\max\{20,16,6,1\}=20.
```

A polynomial of degree at most 63 over $`\mathbb F_{2^{20}}`$ has 64 coefficients. Independently sampling those coefficients uses

```math
kb=64\cdot20=1280
```

classical seed bits. Evaluate the polynomial at the encoded address and retain 16 fixed binary coordinates of its value as the label. Distinct sets of at most 64 addresses then receive independent uniform labels. After averaging over the hidden seed, the received 32-copy density operator is exactly the one used above.

The source selects its seed once and reuses it for these 32 emissions. The equality is tied to that declared copy budget. A fixed degree-63 polynomial does not reproduce fully independent tables for arbitrarily many copies.

The 1,280-bit figure counts the seed only. The source also needs its public finite-field representation, reversible polynomial evaluation, temporary workspace and the delivered registers. Here one example contains 20 address qubits and 16 label qubits. P1 accounts for hash evaluation with $`O(kb^2)`$ elementary gates and $`O(kb)`$ workspace, in addition to the stated input-preparation and label-sampler costs. The learner receives sample registers; it does not receive the seed or a value oracle.

The [resource bridge](BRIDGE.md#source-resources) separates this source construction from the classical-record simulator. The worked numbers make both constructions concrete, while the canonical proofs establish their general validity and accuracy conventions.

