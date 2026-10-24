# From Watrous's operator language to quantum-example simulation

This bridge explains the steps between the [selected Watrous anchor](ANCHOR.md) and the repository's results. The textbook provides the state, channel, norm and symmetry tools. The project supplies the randomized source, the common-component argument and the learning applications. The linked science files are the authoritative statements and proofs.

<a id="notation"></a>

## 1. Translating notation

Watrous uses vectors and matrices without Dirac notation. The repository often uses kets, but the underlying finite-dimensional objects are the same.

| Watrous notation or convention | Repository notation and meaning |
|---|---|
| A complex Euclidean space $\mathcal X=\mathbb C^\Sigma$ | A finite Hilbert space with computational basis indexed by an alphabet, such as $\mathcal A$ or $\mathcal Y$ |
| A standard basis vector $e_a$ | The ket $\lvert a\rangle$ |
| The adjoint $u^*$; the operator $uv^*$ | The bra $\langle u\rvert$; the outer product $\lvert u\rangle\langle v\rvert$ |
| $\mathrm{Pos}(\mathcal X)$; $\mathrm{D}(\mathcal X)$ | Positive semidefinite operators; positive operators of trace one |
| $X\ge Y$ in positive order | $X\succeq Y$, meaning $X-Y$ is positive semidefinite |
| $\mathrm{C}(\mathcal X,\mathcal Y)$ | Completely positive, trace-preserving maps, called quantum channels |
| $\lVert X\rVert_1$ | The trace norm; for $X\succeq0$ it equals $\mathrm{Tr}X$ |
| The completely bounded trace norm $\lVert\!\lVert\!\lVert\Phi\rVert\!\rVert\!\rVert_1$ | The diamond norm $\lVert\Phi\rVert_\diamond$ |
| $H(\rho)$ for a quantum state's entropy | Usually $S(\rho)$ in the channel page; logarithms there are base two |

The project defines **half trace distance**

$$
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
$$

This factor is part of every error bound. A bound on the full trace norm must be divided by two before being used as the project's event-probability bound. Watrous's fidelity is the unsquared quantity $\|\sqrt\rho\sqrt\sigma\|_1$; a squared fidelity is a different numerical convention. These definitions are located in Chapters 1–3 as listed in the [reading map](ANCHOR.md#reading-map).

Two further conventions matter for the channel and symmetry calculations. Watrous's Choi operator is

$$
J(\Phi)=\sum_{a,b}\Phi(|a\rangle\langle b|)
                   \otimes |a\rangle\langle b|,
$$

with output register first. For a channel on an $N$-dimensional input its trace is $N$. The normalized Choi state in C2 is $J(\Phi)/N$, up to exchanging the input-reference and output order. That exchange leaves its spectrum unchanged. In Chapter 7, Watrous's permutation operator uses $\pi^{-1}$ to move tensor factors. Summing over every permutation makes that convention equivalent to the indexing used in the simulator.

<a id="experiment"></a>

## 2. A density operator describes the receiver's experiment

**Textbook tools:** reductions, purifications and channels in §§2.1.3 and 2.2.  
**Project definition:** [model.md](../science/model.md).

Ordinary data consist of an address $a$ drawn from $p$ and a label drawn from $P_a$. The conditional laws may contain an unknown secret. To define the coherent source, independently choose one classical label $F(a)$ at every address, then prepare

$$
|\psi_F\rangle=\sum_a\sqrt{p_a}\,|a,F(a)\rangle.
$$

The state is pure conditional on the table. The receiver does not receive the table, its seed or a purification of that random choice. Averaging over the missing classical record therefore gives the density operator relevant to the receiver's success probabilities.

The same one-copy average can lead to different joint experiments. Fresh tables give

$$
\rho^{\otimes T},
\qquad \rho=\mathbb E_F|\psi_F\rangle\langle\psi_F|,
$$

whereas one reused table gives

$$
\Omega_T=\mathbb E_F
\bigl[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}\bigr].
$$

The second expression retains correlations across emissions. In particular, two conditional copies always lie in the symmetric subspace. A swap test sees this even though the table is hidden. One-copy closeness to a diagonal state therefore does not justify replacing a frozen experiment by a tensor product of diagonal states.

This use of averaging fixes a quantifier: S1 holds for every fixed collection of laws $P_a$, after averaging over the independently drawn table. It does not assert closeness separately for each disclosed or adversarially selected table. Nor does a source-state description automatically supply a unitary for evaluating that table.

<a id="covariance"></a>

## 3. The collision quantity comes from a mean vector

**Textbook tools:** positive operators, expectations and spectra in §§1.1–1.2.  
**Project calculations:** [refreshed_sources.md](../science/refreshed_sources.md) and [frozen_sources.md](../science/frozen_sources.md).

At one address the random object is a basis vector $|F(a)\rangle$, not a coherent sum over all possible labels. Consequently its mean and second moment are

$$
|m_a\rangle=\sum_yP_a(y)|y\rangle,
\qquad
B_a=\sum_yP_a(y)|y\rangle\langle y|.
$$

The probabilities themselves are amplitudes of the mean vector. Its squared norm is the collision probability

$$
c_a=\langle m_a|m_a\rangle=\sum_yP_a(y)^2.
$$

For comparison, the coherent conditional sampler $\sum_y\sqrt{P_a(y)}|y\rangle$ is normalized and describes another source. Substituting that vector for $m_a$ would change the proof and the experiment.

Define the centered covariance

$$
K_a=B_a-|m_a\rangle\langle m_a|.
$$

For every vector $u$,

$$
\langle u|K_a|u\rangle
=\mathbb E|\langle u|F(a)\rangle|^2
 -|\mathbb E\langle u|F(a)\rangle|^2\ge0.
$$

Thus $K_a$ is positive and has trace $1-c_a$. Small collision probability means that the centered part contains nearly all the second-moment weight. It does not mean that every realized graph state is almost diagonal.

For fresh samples, independence immediately determines all off-diagonal address blocks. With uniform addresses and additive errors of law $\chi$, F1 gives the exact result

$$
D(\rho,\rho_{\rm cl})=c(1-1/N),
\qquad c=\sum_e\chi(e)^2.
$$

Independent fresh copies then admit a tensor-product hybrid bound. Frozen copies require the additional construction below.

The entropy $H_2(\chi)=-\log_2c$ is a property of the **conditional label law**. It is not the von Neumann entropy of a realized pure example, and it is not the marginal entropy of the entire observed label. A noiseless hidden signal can have a large marginal label entropy while every $c_a$ equals one.

<a id="frozen-proof"></a>

## 4. What must be added to obtain S1

**Textbook tools:** positive order and trace norm from §1.1; permutation operators from §7.1.1.  
**Project theorem:** [frozen_sources.md](../science/frozen_sources.md).

An elementary operator observation isolates the goal. If two states $\omega,\sigma$ contain the same positive operator $C$,

$$
\omega\succeq C,\qquad \sigma\succeq C,
$$

then their remaining positive parts each have trace $1-\mathrm{Tr}C$. The triangle inequality gives

$$
D(\omega,\sigma)
\le\frac12\bigl(\|\omega-C\|_1+\|\sigma-C\|_1\bigr)
=1-\mathrm{Tr}C.
$$

Neither commutativity nor simultaneous diagonalization is required. The project-specific work is to find a sufficiently large common operator inside the frozen source and an efficiently preparable simulator.

Write

$$
|M\rangle=\mathbb E_F|\psi_F\rangle,
\qquad
|\zeta_F\rangle=|\psi_F\rangle-|M\rangle.
$$

Let $\Pi_{\rm distinct}$ project onto address tuples with no repeated address, and put

$$
|v_F\rangle=\Pi_{\rm distinct}|\zeta_F\rangle^{\otimes T},
\qquad
C_T=\mathbb E_F|v_F\rangle\langle v_F|.
$$

This projection selects **distinct addresses**, not the symmetric subspace. These are different conditions.

Each ket term in $v_F$ contains centered variables at $T$ distinct addresses. In its cross term with another expanded source tensor, an expectation vanishes unless every one of those addresses also appears as a centered bra factor. The bra has only $T$ available factors. Survival therefore forces all of them to be centered and to match precisely those addresses. Those terms already belong to $v_F$. As a result,

$$
\mathbb E_F|v_F\rangle
\bigl(\langle\psi_F|^{\otimes T}-\langle v_F|\bigr)=0,
\qquad
\Omega_T\succeq C_T.
$$

This is the essential independent-label cancellation. Generic permutation symmetry alone does not establish it.

The trace of the component is

$$
w_T=\mathrm{Tr}C_T
=\sum_{\substack{a_1,\ldots,a_T\\\text{distinct}}}
  \prod_{i=1}^T p_{a_i}(1-c_{a_i}).
$$

For a fixed distinct address tuple, the coherent-permutation map $V_{\mathbf a}$ is an isometry on its label registers. In that representation, the source component uses $\bigotimes_iK_{a_i}$, whereas the simulator's distinct-address branch uses $\bigotimes_iB_{a_i}$. Because

$$
B_a=K_a+|m_a\rangle\langle m_a|
$$

is a sum of positive operators, expansion of the tensor product shows that the simulator also contains $C_T$. Its collision fallback is an additional positive component. Hence

$$
D(\Omega_T,\sigma_T)\le1-w_T
\le T\bar c+\binom T2\alpha,
\qquad
\bar c=\sum_ap_ac_a,\quad \alpha=\sum_ap_a^2.
$$

The final inequality is a union bound: a centered contribution may be lost at any of the $T$ positions, and an address collision may occur at any of the $\binom T2$ pairs. It is a sufficient simulation bound. Its becoming large does not prove that a learning task is easy.

<a id="simulator"></a>

## 5. Symmetry must become an executable simulator

**Textbook tool:** the symmetric-subspace projector, Proposition 7.1.  
**Project implementation:** [simulator.md](../science/simulator.md).

The simulator receives exactly $T$ ordinary classical records. On distinct addresses it prepares

$$
|\mathrm{Sym}(\mathbf a,\mathbf y)\rangle
=\frac1{\sqrt{T!}}\sum_{\pi\in S_T}
 \bigotimes_{i=1}^T|a_{\pi(i)},y_{\pi(i)}\rangle.
$$

The normalization follows because distinct addresses make all permutation strings orthogonal, even if some labels coincide. A repeated address leads to a fixed fallback state. The procedure requests no replacement examples and does not condition its overall output on success.

The textbook's projector formula does not by itself provide an efficient circuit or authorize postselection. The implementation uses a reversible encoding of permutations, writes the supplied records by scanning the known classical list, and clears the permutation register by recovering each record's original index from its address. Distinct addresses make that inverse well defined.

This is valid uncomputation because the required inverse depends on the observed address list. It never erases an unknown noisy label. That distinction is also the point of [E1](../science/label_erasure.md): a universal exact one-copy deletion channel fails for the stated three-table witness. E1 is not a theorem excluding every collective transformation using additional copies.

The list has polynomial length and can be scanned with ordinary controlled gates. No QRAM or unseen table lookup is assumed. The implementation page accounts separately for bounded preparation of the uniform permutation and its additional error. S1's density-operator identity describes the ideal simulator; a finite circuit adds its stated approximation loss.

<a id="source-resources"></a>

## 6. Preparing the original source is a separate resource claim

**Textbook tools:** channels, dilations and hidden registers in Chapter 2; norm bounds in Chapter 3.  
**Additional construction:** [source_preparation.md](../science/source_preparation.md), P1.

An abstract table on exponentially many addresses need not be stored explicitly. For a declared $T$-copy budget, each matrix element of the received joint density operator depends on labels at at most $2T$ addresses: the union of its ket and bra address tuples. A $2T$-wise-independent family therefore reproduces the full joint operator exactly.

P1 realizes that family by a degree-$(2T-1)$ polynomial over a sufficiently large finite field, followed by a deterministic finite-randomness label sampler. Vandermonde independence is the extra classical algebraic fact. It is proved in the source page and credited in [Related work](../references/RELATED_WORK.md#joffe1974). It is not an algorithm supplied by Watrous.

There are two distinct holders of information. The source holder knows the signal circuit and its private seed, so it can compute the label, copy it into the delivered register, and reverse its temporary work. The learner receives the resulting sample registers. Giving the learner the same circuit or seed would define a stronger interface.

The accounting also includes preparation of $\sum_a\sqrt{p_a}|a\rangle$, label-sampler time and workspace, the public finite-field representation, seed length and finite precision. An arbitrary amplitude distribution is not free. The uniform finite-group inputs used by the lattice examples have explicit preparations.

Fresh emissions require only pairwise independence within each newly drawn table. Frozen emissions require the order appropriate to their declared budget. One fixed polynomial of finite degree does not reproduce fully independent tables against every possible polynomial-copy learner.

Approximate sampling is controlled on the received state rather than by demanding agreement at every address. If the input-weighted total variation error of the conditional laws is $\delta$, P1 proves

$$
D\bigl(\Omega_T(P),\Omega_T(\widetilde P)\bigr)
\le\sqrt{1-(1-\delta)^{2T}}
\le\sqrt{2T\delta}.
$$

The comparison couples the labels address by address and uses the overlap of the resulting graph states. This avoids a union bound over an exponentially large domain. The corresponding ordinary $T$-sample distributions differ by at most $T\delta$.

<a id="learning-transfer"></a>

## 7. From an operator bound to LWE consequences

**Textbook tools:** state discrimination in §3.1.1 and contractivity in §3.3.2.  
**Project reductions:** [lattice_examples.md](../science/lattice_examples.md), L1–L3.

Let a learner perform any quantum processing of at most $T$ supplied examples. A shorter or adaptive run can be represented by a channel on a fixed $T$-copy input with unused registers. Replacing its input by $\sigma_T$ changes the probability of every final event by at most the S1 error. A quantum output can be included by treating a subsequent verification measurement as part of that final event.

The replacement learner first receives ordinary classical examples, runs a quantum simulator, and then runs the original quantum learner. Its computational power remains quantum. Thus the unconditional theorem compares **data access**. To conclude computational hardness, the exact classical-input problem must already be assumed hard against efficient quantum algorithms.

For scalar bounded-error LWE, the positive quantum-example endpoint uses the established Fourier mechanism of Grilo, Kerenidis and Zijlstra. The project records its parameters and verification argument. Fourier learning, the choice of LWE parameters and cryptographic hardness reductions are additional research content, not material claimed to follow from Watrous.

The auxiliary-label construction makes the comparison particularly direct. Appending $m$ independent uniform bits to each address's label leaves the ordinary classical experiment equivalent to the original LWE data: those bits can be generated or deleted locally. The coherent source instead records an address-dependent random function, and

$$
c_{\rm padded}=c_\chi\,2^{-m}.
$$

S1 therefore transfers classical-input hardness to the padded source when its loss is negligible, even though the unpadded scalar source has the established quantum learner. An independent register tensored onto the whole example would not produce this effect.

For a ring output with $d$ independently noisy coefficient residues,

$$
c_R=c_0^d,
\qquad
D(\Omega_T^{\rm ring},\sigma_T^{\rm ring})
\le Tc_0^d+\frac{T(T-1)}{2q^d}.
$$

Collision probabilities are computed after reduction modulo $q$. Module rank changes the input-domain size when the output remains one polynomial; it does not increase the number of noisy output coefficients. Neither the factorization nor the entropy bound establishes hardness of every coefficient law. In particular, fixed small support and a large sample budget can enable algebraic attacks. L3 fixes the exact ring, modulus, secret prior, error law and sample budget before making a conditional hardness inference.

<a id="channel-consequences"></a>

## 8. The channel companion uses a different interface

**Textbook tools:** §§2.2.2, 3.3.2–3.3.3, 5.2 and 8.2; Definition 8.14 and Exercise 8.3.  
**Project specialization:** [channels.md](../science/channels.md), C1–C2.

The refreshed append map takes an arbitrary address input $\omega$ and emits its noisy label. This is stronger access than receiving one fixed random-example state. When every address has collision probability $c$, its difference from the address-measuring channel factors as

$$
\mathcal E-\mathcal E\circ\Delta
=c\,\mathrm{Ad}_W\circ(\mathrm{Id}-\Delta).
$$

The definition of the diamond norm ensures that a correlated reference register is included. C1 evaluates the norm exactly:

$$
\frac12\|\mathcal E-\mathcal E\circ\Delta\|_\diamond
=c(1-1/N).
$$

This is an identity for maps, proved separately from S1. A random-input state comparison alone would not imply it.

C2 further assumes a **known, memoryless additive-error channel** with fresh independent noise on every use. Its output retains the address. Tracing that output removes off-diagonal address terms from the complementary channel, which therefore measures the address and prepares an environment state. Reading the retained address at the output simulates this complement. That is the explicit degrading map.

Watrous's quantum-capacity theorem normally requires a regularization over many channel uses. For degradable channels, additivity reduces it to a one-use optimization, and concavity permits symmetry averaging. The book poses these degradability results in Exercise 8.3; the project's [channel references](../references/RELATED_WORK.md#bradler2010) supply their established primary framework.

After undoing the known signal, permutation and phase symmetries make the maximally mixed input optimal. Its output entropy and normalized Choi spectrum then give C2. With

$$
\tau=\mathrm{diag}\chi,\qquad
|\mu\rangle=\sum_e\chi(e)|e\rangle,\qquad
A=\tau-|\mu\rangle\langle\mu|,\qquad
B_N=\frac{\tau+(N-1)|\mu\rangle\langle\mu|}{N},
$$

the complementary-output spectrum consists of $B_N$ once and $A/N$ repeated $N-1$ times. Therefore

$$
Q(\mathcal E)
=\log_2N+H(\chi)-S(B_N)-(N-1)S(A/N).
$$

Here $S(X)=-\mathrm{Tr}X\log_2X$ is also used for the displayed subnormalized blocks; it is not the entropy of a separately normalized state.

Attaching a classical flag to the coherent and address-measuring branches gives an established type of degradable extension. Its capacity is $c\log_2N$. Forgetting a binary flag costs at most $h_2(c)$ in coherent information at the chosen input, so

$$
\max\{0,c\log_2N-h_2(c)\}
\le Q(\mathcal E)\le c\log_2N.
$$

Uniform noise on $K$ outcomes makes the branches orthogonal and yields $Q=(\log_2N)/K$. These statements assume unrestricted coding operations and knowledge of the channel. They are not efficient unknown-secret decoders, and they do not describe a frozen channel with temporal memory.

<a id="claim-boundaries"></a>

## 9. The logical boundaries

| Established statement | Additional conclusion that needs its own argument |
|---|---|
| Two supplied states are close in trace distance | Their preparation circuits, hidden seeds or chosen-input oracles are interchangeable |
| A frozen ensemble is simulable after averaging over its table | Every realized pure state is close to the same classical mixture |
| A covariance operator has trace $1-c_a$ | Its tensor moment automatically lies inside the full source; S1's cross-term cancellation is required |
| A symmetric projector exists | Its action is an efficient normalized deterministic preparation; the simulator circuit supplies this separately |
| Conditional collision entropy is large | The underlying classical inference task is computationally hard |
| A known memoryless channel has small quantum capacity | Learning its unknown signal from random examples is hard |

The [canonical proof pages](../science/README.md) establish the needed steps under their stated models. The [related-work account](../references/RELATED_WORK.md) distinguishes inherited techniques from the conditional-label comparison. Watrous supplies the mathematical language in which those distinctions can be checked precisely.
