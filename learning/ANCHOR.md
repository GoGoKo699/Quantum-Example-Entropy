# Educational anchor: Watrous, The Theory of Quantum Information

<a id="identity"></a>

## Source identity

The sole educational anchor is **John Watrous, The Theory of Quantum Information, Cambridge University Press, 2018**, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142).

Watrous provides the finite-dimensional operator language needed to understand the source states, the trace-distance comparison, and the channel companion. The project adds a particular randomized-label experiment and its proofs. The project results F1, S1, P1, L1–L3, E1 and C1–C2 are not statements attributed to the textbook.

The [source-to-project bridge](BRIDGE.md) explains those additions. The [milestone map](MILESTONES.md) organizes the material into foundations followed by the project argument. Research-paper citations remain in [Related work](../references/RELATED_WORK.md); they document the provenance of particular techniques and assumptions rather than introduce additional textbook prerequisites.

<a id="access-and-version"></a>

## Access and version

The primary access point is [Watrous's books and courses page](https://jhwatrous.github.io/books-and-courses.html), under the heading for this book. It links both the complete manuscript and individual chapters.

| Resource | Exact source and use |
|---|---|
| Published book | [Cambridge record and DOI](https://doi.org/10.1017/9781316848142), 2018 publication |
| Author manuscript | [Standard-layout complete PDF](https://jhwatrous.github.io/TQI.pdf); its front matter identifies a 2018 pre-publication draft, with a January 2018 preface |
| Chapter files | The standard-layout PDFs linked in the reading map below; these retain printed book-page numbers |
| Corrections | [Author's errata](https://jhwatrous.github.io/TQI.errata.pdf), dated **July 23, 2025** in the version inspected |

The pointers below were verified against the author-posted standard-layout files on **October 24, 2026**. Page numbers mean the numbers printed on the pages, not the PDF viewer's page counter. Section and numbered-result identifiers are the main locators; compact-layout and published copies may paginate differently. The author's errata concern the published book and explain that the online manuscript can contain additional minor typographical errors.

The author makes the manuscript available for personal use and prohibits its sale or redistribution. This repository links to those source files and supplies its own explanatory material.

<a id="reading-map"></a>

## Verified reading map

The direct route to S1 uses selected material from Chapters 1–3 and Section 7.1.1. Entropy and capacity material is needed for the channel companion, not for the centered-covariance proof of S1.

| Role in this project | Watrous location in the inspected manuscript | Project connection |
|---|---|---|
| Finite spaces, basis vectors, tensors | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.1.1, p. 1 | Address and label registers |
| Operators, adjoints, positive order, partial trace | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.1.2, p. 8 | Covariance operators and discarded records |
| Spectra and trace norm | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.1.3, p. 24 | Positive residuals and F1 |
| Convexity and probability | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §§1.2.1–1.2.2, pp. 35 and 47 | Hidden-table averaging, independent addresses and collision bounds |
| Density operators and reductions | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3, pp. 61 and 67 | Pure conditional states versus the receiver's mixed ensemble |
| Channels and dilations | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.2.1–2.2.2, pp. 72 and 77; Theorem 2.22, p. 82 | Quantum processing, Stinespring representations and E1 |
| Measurements | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.3.1–2.3.2, pp. 100 and 105 | Final tests on a learner's output |
| State distinguishability | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1.1, p. 125; Theorem 3.4 | Operational meaning of half trace distance |
| Fidelity conventions | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §§3.2.1–3.2.3, pp. 140–155 | Pure-state comparison and preparation accuracy |
| Contractivity and channel norms | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.3.2, p. 166; Corollary 3.40, p. 168, and Proposition 3.41, p. 169; §3.3.3, p. 175 | L1 and the separate diamond-distance statement C1 |
| Permutation symmetry | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.1, p. 391; Proposition 7.1, p. 392 | Coherent permutations of distinct classical records |
| Optional symmetry context | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.2, p. 400 | Distinguishing invariant vectors from invariant operators; S1 does not require Haar integration |
| Entropy definitions and inequalities | [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf), §5.1.1, p. 250; §§5.2.1–5.2.3, pp. 265–276; Theorem 5.36, pp. 281–282 | C2's entropy calculation and loss of a classical flag |
| Separability and measure–prepare channels | [Chapter 6](https://jhwatrous.github.io/TQI.6.pdf), §6.1.1, p. 310; Exercise 6.1, p. 384 | Why the address-measuring comparison channel is entanglement breaking |
| Coherent information | [Chapter 8](https://jhwatrous.github.io/TQI.8.pdf), §8.1.1; Definition 8.14, p. 474, and Proposition 8.15, p. 475 | C2's objective and its decrease under output processing |
| Quantum capacity | [Chapter 8](https://jhwatrous.github.io/TQI.8.pdf), §§8.2.1–8.2.2, pp. 512 and 521; Theorem 8.55, p. 537 | The regularized capacity formula |
| Degradable channels | [Chapter 8](https://jhwatrous.github.io/TQI.8.pdf), §8.4, Exercise 8.3, pp. 556–557 | Concavity and additivity that simplify C2 |

Exercise 8.3 **poses** the relevant degradability results; it is not a worked theorem proof in the book. The project gives its degrading map explicitly and cites the primary literature for the established capacity framework. Exercise 6.1 likewise supplies a textbook pointer to the characterization of entanglement-breaking channels.

<a id="scope"></a>

## What the anchor supplies, and what the project adds

The assumed mathematics is finite-dimensional linear algebra and elementary probability: bases, inner products, tensor products, eigenvalues, conditional probabilities and independence. Chapter 1 is a reference for this language. The bridge translates Watrous's operator notation into the ket notation used by the repository, including the normalization of trace distance and Choi operators.

The additional project content is the independently randomized label table; the distinction between fresh and frozen emissions; the common positive component in S1; the exact-count simulator; and the finite-seed implementation with its copy-budget and precision accounting. The LWE applications also require a specified classical-input hardness assumption. These are developed in the repository rather than inferred from a generic textbook theorem.

The channel companion uses another interface: a known memoryless map with chosen inputs and unrestricted encoding and decoding. Its capacity calculation therefore has a different meaning from secret recovery using random examples. The [bridge's claim boundaries](BRIDGE.md#claim-boundaries) keep these conclusions separate.
