# Related work and scope of the contribution

The central question is when coherent examples carry information that cannot be reproduced by quantum processing of ordinary classical examples. The comparison concerns data access: the simulator and the learner may both perform quantum computation. It does not assert that arbitrary quantum computation is classically simulable.

For finite input and label alphabets, let $p_x$ be the input probabilities and $P_x(y)$ arbitrary conditional label laws. Independently draw one label $F(x)\sim P_x$ for each input, and prepare

$$
|\psi_F\rangle=\sum_x\sqrt{p_x}|x,F(x)\rangle.
$$

In the frozen model the same hidden table $F$ is used in all $T$ copies. Its operational state is therefore

$$
\Omega_T=\mathbb E_F[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}],
$$

which generally differs from the tensor power of the one-copy average. Define

$$
c_x=\sum_yP_x(y)^2,\qquad
\bar c=\sum_xp_xc_x,\qquad
\alpha=\sum_xp_x^2.
$$

Theorem S1 provides a quantum simulator using exactly $T$ independent classical examples from $p_xP_x(y)$, with

$$
\tfrac12\|\Omega_T-\operatorname{Sim}_T\|_1
\le 1-T!e_T\bigl(\{p_x(1-c_x)\}_x\bigr)
\le T\bar c+\binom T2\alpha.
$$

Here $e_T$ is the elementary symmetric polynomial. The simulator uses only the observed examples, not descriptions of the unknown laws or the hidden signal. The bound averages over the initial hidden table; it is not a closeness assertion for every realized pure state. The relevant contribution is this signal-preserving comparison for arbitrary conditional label laws, including the frozen joint ensemble.

<a id="gkz2019"></a>

## Noisy quantum examples and the LWE setting

Grilo, Kerenidis and Zijlstra [GKZ19] specify a quantum noisy-example source in Section II by preparing branch errors coherently and tracing out the randomness register. Equation (1) gives independent errors across the input branches. Independent calls are used in the amplification argument of Appendix B. This supports the refreshed-source interpretation; their paper does not separately define the frozen joint state above. Their scalar LWE Fourier learner, including Theorem IV.1 for bounded errors, supplies the positive scalar-output endpoint used here.

Section V.2 and Appendix C.2 discuss the Ring-LWE extension. Their source retains the full vector of ring coefficients. The coefficient representation and the multiplicative evaluation representation lead to different obstacles for their Fourier argument. They leave the independent-branch-noise extension open, while treating a common error shared by all branches separately. S1 addresses the independent-branch model when the full output error has sufficiently small collision probability. The resulting hardness statement is conditional on hardness for quantum algorithms receiving ordinary classical samples at the specified parameters. It is not a statement about all quantum encodings of Ring-LWE. [GKZ19]

<a id="caro2024"></a>

Caro, Hinsche, Ioannou, Nietner and Sweke [Caro24] give an explicit general distributional formulation of the refreshed model. Definition 8 of the full preprint samples a Boolean labeling function independently from the conditional label laws and then averages its superposition state. Their mixture-of-superpositions oracle returns a copy of that mixed state. Lemma 1 shows that computational-basis measurement recovers the original classical distribution. Their learning and verification results, and distribution-independent sample lower bounds, establish substantial prior work on the source model itself. The conditional laws in S1 generalize this formulation to arbitrary finite labels and add a joint-state simulation theorem for a table reused across copies. Binary labels have $c_x\ge 1/2$, so the small-$\bar c$ regime is not available for a single Boolean label. [Caro24]

Two applications distinguish output size from an arbitrary choice of classical encoding. For product errors over $d$ coefficients, the collision probability is $c_0^d$, giving an exponentially small simulation error when $c_0<1$ is fixed and the input collision term is also negligible. Alternatively, append independent random bit labels at every input address to a scalar noisy example. The classical experiment acquires independent auxiliary data, while the coherent graph source acquires additional independent labels. S1 applies to the enlarged label distribution. These labels are address-dependent random functions; a single independent tensor factor shared by every branch does not have the same effect. The positive scalar learning endpoint remains the result of [GKZ19].

<a id="kimkim2024"></a>

## The coefficient-erasure step in Kim and Kim

Kim and Kim [KK24] claim a Ring-LWE extension in Result 1. After a known linear transformation of the input, their displayed state still contains every noisy output coefficient. The next displayed transition, introduced by the phrase “Uncomputing irrelevant information,” keeps one scalar output coefficient and asserts the corresponding pure scalar LWE example. The paper does not supply an implementation of that transition from copies of the displayed source state.

The access distinction can be expressed without attributing a general impossibility to the article. For a state

$$
|\Phi\rangle=\sum_a\gamma_a|a_j\rangle|b_j(a)\rangle|b_{-j}(a)\rangle,
$$

discarding the last register gives

$$
\operatorname{Tr}_{-j}|\Phi\rangle\langle\Phi|
=\sum_{a,a'}\gamma_a\overline{\gamma_{a'}}
\mathbf1[b_{-j}(a)=b_{-j}(a')]
|a_j,b_j(a)\rangle\langle a'_j,b_j(a')|.
$$

Thus discarding unknown output coefficients does not generally yield the asserted coherent scalar state. Reversible computation of a known input transformation does not itself erase unknown noisy labels. An additional oracle implementing the required coherent operation would change the access model. The comparison here concerns this specific transition under copy-only access, not the paper's separate SIS or size-reduced-LWE results. Under an appropriate classical-input hardness assumption, S1 additionally rules out an efficient, sufficiently accurate scalarization followed by the known scalar learner. [KK24]

<a id="gmr2025"></a>

## Coherent permutation simulation is an established technique

Goyal, Malavolta and Roberts [GMR25], Theorems 3 and 4, prove an exact correspondence for coupon states with independent hidden random phases. For any fixed coupon support, averaging $T$ copies over one reused phase vector yields a mixture of normalized coherent superpositions of the permutations of $T$ ordinary sampled coupons. Their phases use a modulus larger than $T$; the state identity accommodates repeated coupons. Consequently, coherent permutation simulation and sample equivalence for a hidden ensemble of fixed pure states are prior techniques.

<a id="bbss2023"></a>

The same paper's Section 1.2 explicitly compares this construction with Behera, Brakerski, Sattath and Shmueli [BBSS23], Lemma 6, which uses related permutation states in its pseudorandom-state analysis. S1 does not claim a new symmetrizer. Its additional statement is that independent positive-amplitude graph labels produce a common positive semidefinite component of large weight with that simulator, without imposed phase randomization and while preserving arbitrary conditional laws. [GMR25]

<a id="giurgica2023"></a>
<a id="jeronimo2024"></a>

## Positive subset states and approximate moments

Giurgică-Tiron and Bouland [GTB23], Theorem 1, already establish that positive-amplitude random subset states can approximate Haar moments. A uniformly chosen $m$-element subset of a $D$-element computational basis has a $T$-copy moment within

$$
O(Tm/D+T^2/m)
$$

in trace distance of the Haar moment, in the stated parameter regime. Their analysis uses the symmetric group and the Johnson scheme. Jeronimo, Magrafta and Wu [JMW24], Theorem 1.1, independently establish a related bound

$$
O(T^2/D+T/\sqrt m+mT/D)
$$

in trace norm and identify the sharper concurrent bound of [GTB23]. These results are direct antecedents for the fact that random phases are unnecessary for uninformative high-order state moments. Neither that fact nor an entropy-plus-birthday form of error bound is claimed as new here.

The ensembles and comparison targets differ. A uniformly random global subset does not impose exactly one label at each input address. More importantly, arbitrary laws $P_x$ can retain a structured hidden signal, so the graph-source ensemble need not resemble Haar. S1 compares it to a simulator driven by its own classical joint distribution. In the special case of $N$ uniform input addresses and $K$ uniform labels, the analogy is close: graph support size $N$, ambient dimension $NK$, and $c=1/K$ reproduce the same two scales. The arbitrary conditional-law, signal-preserving statement is the distinction from these subset-state theorems.

<a id="zhandry2021qrf"></a>

## Random-output oracles and bounded independence

Zhandry's random-function work [Zha21] also establishes an important sample/oracle comparison. Theorem 1.1 of the inspected ECCC revision proves that efficiently distinguishing quantum oracles whose outputs are independently sampled from one common law $D_1$ or $D_2$ yields an efficient distinguisher using ordinary samples. Its proof uses polynomially many samples to construct an approximate small-range oracle. Appendix F, Lemma F.3, applies this to an oracle returning entire ordinary LWE samples.

S1 uses weaker access—copies of one source state—but preserves exactly the classical-example count and allows unknown input-dependent laws $P_x$. An oracle whose output is an entire random pair $(a,b)$, indexed by an unrelated query string, is distinct from a graph example whose input register is $a$ itself. The homogeneous-output oracle reduction therefore does not directly supply S1's conditional-law simulator. [Zha21]

<a id="zhandry2012ibe"></a>
<a id="joffe1974"></a>
<a id="vadhan2009notes"></a>

The finite-seed preparation construction is also based on established tools. Degree-$(k-1)$ polynomial evaluation over a finite field gives $k$-wise independence [Jof74]; Construction 3.29 and Proposition 3.30 in Vadhan's notes provide an explicit modern exposition [Vadhan09]. The quantum-query moment principle is due to Zhandry [Zha12]: $2Q$-wise independence reproduces the behavior of a $Q$-query quantum algorithm. It is restated as Fact 2 and Theorem 7.1 in the inspected revision of [Zha21]. A single example involves at most two branch labels in each density-matrix entry; $T$ copies involve at most $2T$. Pairwise or $2T$-wise compilation is thus a source-specific application of established bounded independence.

The preparation claim must retain its resource assumptions. The source holder can evaluate the signal and the noise sampler; the learner receives neither the hidden seed nor an inverse preparation oracle. A frozen $2T$-wise construction is tied to a declared $T$-copy budget. A fixed finite independence order does not automatically simulate a fully random table against every polynomial-copy learner. A computational pseudorandom-function replacement requires its own assumption and hybrid argument. None of these constructions provides the coherent source from ordinary LWE samples with an unknown secret.

<a id="regev2009"></a>

## Cryptographic assumptions and error distributions

Regev's LWE reduction [Reg09] and the Ring-LWE reductions of Lyubashevsky, Peikert and Regev [LPR13] justify particular parameterized hardness assumptions; they do not make every nontrivial error law hard. The transfer statement here fixes the ring, modulus, secret distribution, error distribution, sample budget and quantum running-time class, and then assumes hardness of that ordinary classical-input experiment. S1 transfers that assumption with its explicit statistical loss.

<a id="lpr2013"></a>

The error representation matters. Section 1.2 of the inspected LPR manuscript uses Gaussian error in the canonical embedding. For power-of-two cyclotomic rings, the canonical and coefficient embeddings differ by a scaled rotation, so spherical Gaussian error has independent coefficient coordinates after the appropriate rescaling. That statement alone does not identify every finite modular product law with a distribution covered by a worst-case reduction. LPR further distinguishes its bounded-sample fixed-spherical result, Theorem 5.2, from the separate fixed-spherical search assumption used in Theorem 5.3. A claim at specific coefficient parameters needs the corresponding reduction or an explicit assumption. [LPR13]

<a id="arorage2011"></a>
<a id="peikert2016"></a>

Small support is a separate concern. Arora and Ge [AG11], Section 3 and Theorem 3.3 of the inspected full version, use a polynomial vanishing on the error values and then linearize its monomials. Constant-size error support can therefore produce polynomial-degree algebraic attacks when enough ordinary samples are available and the field conditions hold. Such laws remain valid statistical examples for S1, but are not automatically suitable asymptotic hardness examples. The output collision entropy controls the simulation loss; it does not certify computational hardness. Peikert's survey [Pei16], Sections 4.2 and 4.4, supplies a broader account of the LWE and Ring-LWE assumptions and reductions.

The Ring-LWE consequence consequently concerns the fully specified independent-branch source and a separately stated hardness assumption. Common error shared across all input branches, coherent amplitude-noise encodings, exposed randomness, chosen-input evaluation queries and inverse preparation access are different models. The theorem gives no security claim for a complete deployed cryptosystem without specifying how its accessible data matches the source experiment.

<a id="pirnayseifert2026"></a>

## Outstanding comparison: Pirnay and Seifert

The official ACM PQQS 2026 accepted-paper list records Niklas Pirnay and Jean-Pierre Seifert, *On linearly derived quantum samples for LWE* [PS26]. The conference is scheduled for November 2–4, 2026. As of October 24, 2026, a bounded check of the official accepted list and program, the institutional publication entry, the author's site, and exact-title arXiv/ePrint searches did not locate a manuscript or abstract. The institutional file link points to the conference site.

No theorem-level comparison with this paper has therefore been made. Its title is insufficient to infer either overlap or separation. Any claim of priority or a complete resolution of the quantum Ring-LWE literature must remain pending access to that manuscript. The verified results above support the stated comparisons; they are not a claim that all potentially relevant literature has been excluded.

<a id="watrous2018"></a>

## Operator tools

The passage from trace-distance approximation to a guarantee for every measurement uses standard state-discrimination and contractivity facts. Watrous [Wat18], Chapter 2, Section 3.1.1 and Section 3.3, develops the relevant state, channel and norm framework. Section 7.1.1 gives the symmetric-subspace projector and permutation notation used in moment comparisons. These are mathematical foundations for the argument, not additional novelty claims.

<a id="bradler2010"></a>

## Hadamard channels and flagged capacity bounds

The [channel calculation](../science/channels.md) specializes established capacity tools. Brádler, Hayden, Touchette and Wilde [BHTW10], Section II.3.2, describe Hadamard channels through their entanglement-breaking complementary channels and explain why these channels are degradable; Sections III–IV develop their capacity regions. In C2, retention of the address gives a complementary channel that measures that address and prepares an environment state. This places the encoding channel within the existing framework.

<a id="yard2008"></a>

Yard, Hayden and Devetak [YHD08] prove concavity of coherent information for degradable channels in Section 7.3 of the inspected preprint. Together with the phase and permutation symmetries of the encoding channel after controlled subtraction of its known signal, concavity makes the maximally mixed input optimal. C2 then evaluates the complementary-output entropy through an explicit Choi spectrum. This is a calculation for a known memoryless channel with unrestricted coding operations, distinct from unknown-secret learning with source copies.

<a id="kianvash2022"></a>

Kianvash, Fanizza and Giovannetti [KFG22], Section 3 and Proposition 3.1, develop sufficient conditions for degradable flagged extensions and capacity bounds obtained by forgetting the flag. C2 uses the elementary orthogonal-flag case: its coherent branch preserves the input isometrically, while its other branch measures the address. The extension has capacity $c\log_2N$, and forgetting its binary flag loses at most $h_2(c)$ in coherent information at the chosen input. The resulting bounds and the exact uniform-noise value specialize these methods; neither degradability, coherent-information concavity nor the flagged-extension framework is claimed as a new tool.

## Primary sources

Bibliographic records, including publication titles and version notes, are in [references.bib](references.bib). Section and theorem references above use the following inspected versions.

| Citation | BibTeX key | Primary text used for comparison |
|---|---|---|
| GKZ19 | `gkz2019` | [arXiv:1702.08255v2](https://arxiv.org/html/1702.08255v2), §§II, IV, V.2, Appendices B and C.2 |
| Caro24 | `caro2024` | [arXiv:2306.04843v2](https://arxiv.org/html/2306.04843v2), Definition 8, Lemma 1; [ITCS publication](https://doi.org/10.4230/LIPIcs.ITCS.2024.24) |
| KK24 | `kimkim2024` | [arXiv:2404.03932v2](https://arxiv.org/html/2404.03932v2), Result 1 |
| GMR25 | `gmr2025` | [Published PDF](https://cic.iacr.org/p/2/1/5/pdf), §1.2 and Theorems 3–4 |
| BBSS23 | `bbss2023` | [Publication record](https://doi.org/10.1007/978-3-031-48624-1_5); the specific Lemma 6 comparison is attributed to GMR25 §1.2 |
| GTB23 | `giurgica2023` | [arXiv:2312.09206v1](https://arxiv.org/html/2312.09206v1), Theorem 1 |
| JMW24 | `jeronimo2024` | [arXiv:2312.15285v2](https://arxiv.org/html/2312.15285v2), Theorem 1.1 |
| Zha12 | `zhandry2012ibe` | [CRYPTO publication](https://doi.org/10.1007/978-3-642-32009-5_44); bounded-independence statement inspected in Zha21 Fact 2 |
| Zha21 | `zhandry2021qrf` | [ECCC TR12-140, revision 2, October 2013](https://eccc.weizmann.ac.il/report/2012/140/revision/2/download), Theorem 1.1, Fact 2, Theorem 7.1 and Lemma F.3; [journal publication](https://doi.org/10.1145/3450745) |
| Jof74 | `joffe1974` | [Publisher record](https://doi.org/10.1214/aop/1176996762); construction and attribution inspected in Vadhan09 |
| Vadhan09 | `vadhan2009notes` | [Author's Chapter 3](https://people.seas.harvard.edu/~salil/cs225/spring09/lecnotes/Chap3.pdf), Construction 3.29, Proposition 3.30 and historical notes |
| Reg09 | `regev2009` | [Author manuscript](https://cims.nyu.edu/~regev/papers/qcrypto.pdf), Theorem 1.1 |
| LPR13 | `lpr2013` | [Author manuscript, April 2012](https://cims.nyu.edu/~regev/papers/ideal-lwe.pdf), §1.2, Theorems 4.1, 5.2–5.3; [journal publication](https://doi.org/10.1145/2535925) |
| AG11 | `arorage2011` | [ECCC TR10-066, revision 1](https://eccc.weizmann.ac.il/report/2010/066/revision/1/download), §3, Theorem 3.3 |
| Pei16 | `peikert2016` | [Author's ePrint record](https://eprint.iacr.org/2015/939), §§4.2 and 4.4; [publication DOI](https://doi.org/10.1561/0400000074) |
| Wat18 | `watrous2018` | [Author book page](https://jhwatrous.github.io/books-and-courses.html), Chapters 2, 3 and 7 |
| BHTW10 | `bradler2010` | [arXiv:1001.1732v2](https://arxiv.org/html/1001.1732v2), §II.3.2 and §§III–IV; [APS publication](https://doi.org/10.1103/PhysRevA.81.062312) |
| YHD08 | `yard2008` | [arXiv:quant-ph/0501045v3](https://arxiv.org/html/quant-ph/0501045v3), §7.3; [IEEE publication](https://doi.org/10.1109/TIT.2008.924665), with published author order |
| KFG22 | `kianvash2022` | [arXiv:2008.02461v2](https://arxiv.org/html/2008.02461v2), §3 and Proposition 3.1; [Quantum publication](https://quantum-journal.org/papers/q-2022-02-09-647/) |
| PS26 | `pirnayseifert2026` | [Official accepted-paper list](https://acm-pqqs.github.io/pqqs2026/call-for/accepted-papers.html); title and authors only |

[GKZ19]: https://doi.org/10.1103/PhysRevA.99.032314
[Caro24]: https://doi.org/10.4230/LIPIcs.ITCS.2024.24
[KK24]: https://doi.org/10.1038/s41598-024-78386-3
[GMR25]: https://doi.org/10.62056/ayzoxrxqi
[BBSS23]: https://doi.org/10.1007/978-3-031-48624-1_5
[GTB23]: https://arxiv.org/abs/2312.09206
[JMW24]: https://arxiv.org/abs/2312.15285
[Zha12]: https://doi.org/10.1007/978-3-642-32009-5_44
[Zha21]: https://doi.org/10.1145/3450745
[Jof74]: https://doi.org/10.1214/aop/1176996762
[Vadhan09]: https://people.seas.harvard.edu/~salil/cs225/spring09/lecnotes/Chap3.pdf
[Reg09]: https://doi.org/10.1145/1568318.1568324
[LPR13]: https://doi.org/10.1145/2535925
[AG11]: https://doi.org/10.1007/978-3-642-22006-7_34
[Pei16]: https://doi.org/10.1561/0400000074
[PS26]: https://acm-pqqs.github.io/pqqs2026/call-for/accepted-papers.html
[Wat18]: https://doi.org/10.1017/9781316848142
[BHTW10]: https://doi.org/10.1103/PhysRevA.81.062312
[YHD08]: https://doi.org/10.1109/TIT.2008.924665
[KFG22]: https://doi.org/10.22331/q-2022-02-09-647
