# Milestone map

The thirty milestones follow the dependencies of **Quantum Example Entropy**. John Watrous, *The Theory of Quantum Information*, is the sole educational anchor. [ANCHOR.md](ANCHOR.md) identifies the edition and author-posted text; [BRIDGE.md](BRIDGE.md) connects its verified sections to the project's definitions and proofs. Research papers remain sources for attribution, algorithms, and specialized results. They do not form a second textbook track.

The allocation follows the project. **M01–M12, background and preliminaries**, establish the finite-system model, positive operators, probabilistic mixtures, physical operations, distinguishability, error control, centered moments, and permutation symmetry. The phase ends by assembling these ingredients into the exact source experiment. **M13–M30, narrative and innovation**, move from the one-copy calculation to the frozen-source proof, its implementable simulator, finite-seed preparation, learning consequences, and channel companions. The final two milestones assess the limits of the claims and synthesize the complete argument.

Each phase moves from local objects to the joint operational statement. Dependencies indicate mathematical and conceptual prerequisites within this map; their order reflects the structure of the subject.

## Phase I — Background and preliminaries

<a id="m01"></a>

### M01 — Registers, encodings, and the tensor structure

**Central question.** What mathematical systems are present in one example and in a collection of examples?

**Understanding target.** Finite address and label alphabets determine orthonormal bases and separate registers. An example belongs to their tensor product, while $`T`$ examples occupy a further tensor power. A basis label, a vector, an operator, and a distribution have different mathematical roles. Register order and normalization remain explicit when expressions are rewritten.

**Dependencies and story role.** No earlier milestone is required. This establishes the notation needed to distinguish input addresses, output labels, private randomness, and receiver registers throughout the project.

**Conceptual connection.** A classical bit-string encoding becomes a quantum basis choice; retaining the address register makes different branches orthogonal even when their labels coincide.

**Sources.** Watrous, Chapter 1, §§1.1.1–1.1.2, and Chapter 2, §2.1.1; [model](../science/model.md), §1; [notation bridge](BRIDGE.md#notation).

<a id="m02"></a>

### M02 — Positive operators, traces, and operator order

**Central question.** What does it mean for two states to contain the same positive operator?

**Understanding target.** Positive semidefiniteness, spectral decomposition, trace, and the order relation $`A\succeq B`$ supply the language of the main proof. A positive operator can have trace below one without being a normalized state. If $`C\preceq\rho,\sigma`$, the two residuals are positive and their traces quantify the mass outside the shared component.

**Dependencies and story role.** Depends on [M01](#m01). It supplies the operator argument that will eventually turn a shared covariance component into a trace-distance bound.

**Conceptual connection.** A shared positive operator plays the role of common probability mass, while allowing coherence within that component.

**Sources.** Watrous, Chapter 1, §§1.1.2–1.1.3 and §1.2.1; [frozen sources](../science/frozen_sources.md), the centered-covariance and common-component proof; [covariance bridge](BRIDGE.md#covariance).

<a id="m03"></a>

### M03 — Conditional distributions and the two collision probabilities

**Central question.** Which classical probabilities control the quantum comparison?

**Understanding target.** The input law is $`p_a`$ and the conditional label law is $`P_a(y)`$. Their relevant quantities are $`c_a=\sum_yP_a(y)^2`$, $`\bar c=\sum_ap_ac_a`$, and $`\alpha=\sum_ap_a^2`$. Label agreement at a fixed address and repetition of an input address are different events. Product label laws multiply collision probabilities; reduction modulo a label alphabet must occur before collisions are counted.

**Dependencies and story role.** Depends on [M01](#m01). It identifies the two numerical terms that survive in the final simulation estimate.

**Conceptual connection.** Collision entropy is the logarithmic description of an agreement probability. Its operational meaning here comes from that probability, rather than from a general assertion that entropy implies hardness.

**Sources.** Watrous, Chapter 1, §1.2.2, for the probabilistic framework; [model](../science/model.md), §3, and [lattice examples](../science/lattice_examples.md), §§4–5, for the project's collision quantities.

<a id="m04"></a>

### M04 — Ensembles, density operators, and hidden choices

**Central question.** How can every realized example be pure while the receiver's experiment is mixed?

**Understanding target.** A hidden random table $`F`$ selects a pure graph state $`|\psi_F\rangle`$. The receiver's density operator averages over that undisclosed choice. This averaging is taken with the underlying conditional laws and secret fixed. The same density operator can have several ensemble decompositions, so a particular preparation description is additional information unless its record is supplied.

**Dependencies and story role.** Depends on [M01](#m01), [M02](#m02), and [M03](#m03). It fixes the quantifiers of every source comparison before multiple copies are introduced.

**Conceptual connection.** An ensemble average describes accessible observations without asserting that each realized pure state is individually close to that average.

**Sources.** Watrous, Chapter 2, §2.1.2; [model](../science/model.md), §§1–2; [interpretation](../science/interpretation.md), “Purity and repeated copies”; [experiment bridge](BRIDGE.md#experiment).

<a id="m05"></a>

### M05 — Partial trace and records of an input branch

**Central question.** What happens to interference when a correlated register is discarded?

**Understanding target.** Taking a partial trace weights an off-diagonal term by the inner product of the discarded branch records. For computational-basis records this becomes an equality indicator. A private randomness register can therefore determine the received mixed state, and an unused output coordinate can still matter physically. A pure reduced state requires the relevant purification to factor.

**Dependencies and story role.** Depends on [M04](#m04). It explains how the source model is obtained and prepares the later one-copy deletion obstruction.

**Conceptual connection.** Classical deletion removes a data field; quantum discarding also changes interference whenever that field identifies branches.

**Sources.** Watrous, Chapter 1, §1.1.2, and Chapter 2, §2.1.3; [label erasure](../science/label_erasure.md), §1; [model](../science/model.md), §1.

<a id="m06"></a>

### M06 — Isometries, channels, and physically allowed transformations

**Central question.** Which transformations of the example registers are valid quantum operations?

**Understanding target.** Isometries preserve inner products. Channels are completely positive and trace preserving, and their representations connect a circuit, an environment, and a density-operator map. A reversible computation can clear workspace when its inverse is available. The existence of a function on classical data does not automatically provide the corresponding coherent value circuit or inverse.

**Dependencies and story role.** Depends on [M02](#m02) and [M05](#m05). It supplies the language for both the valid simulator and the invalid universal deletion operation considered later.

**Conceptual connection.** A Stinespring environment records precisely the information that an output-only description omits; preservation of inner products constrains how that information can be removed.

**Sources.** Watrous, Chapter 2, §§2.2.1–2.2.2; [simulator](../science/simulator.md), “The label-register isometry”; [label erasure](../science/label_erasure.md), §2.

<a id="m07"></a>

### M07 — Measurements and the operational meaning of trace distance

**Central question.** Why does a state-distance estimate constrain every final decision?

**Understanding target.** Measurement probabilities arise from positive measurement operators. Half trace distance, $`D(\rho,\sigma)=\|\rho-\sigma\|_1/2`$, bounds the change in the probability of any event and characterizes optimal binary state discrimination. A proof about the complete density operator therefore controls more than a specified Fourier measurement or decoder.

**Dependencies and story role.** Depends on [M02](#m02), [M04](#m04), and [M06](#m06). It gives the eventual simulation bound its experimentally and computationally meaningful interpretation.

**Conceptual connection.** The positive part of a Hermitian difference identifies a distinguishing measurement; this links spectral calculations to observable advantage.

**Sources.** Watrous, Chapter 2, §§2.3.1–2.3.2, and Chapter 3, §3.1.1, especially Theorem 3.4; [model](../science/model.md), §3; [learning transfer](../science/lattice_examples.md), §1.

<a id="m08"></a>

### M08 — Overlaps, fidelity, and approximation error

**Central question.** How can a preparation approximation be converted into a bound on distinguishability?

**Understanding target.** Pure-state overlaps determine their trace distance, and fidelity relates overlaps of purifications to mixed-state comparisons. Convexity permits averaging a coupled collection of preparation errors. Tensor powers amplify an error in a controlled way, so the accuracy of a single emitted state and the accuracy of a full experiment must be distinguished.

**Dependencies and story role.** Depends on [M04](#m04) and [M07](#m07). It supplies the tools needed to charge finite sampling and circuit precision later.

**Conceptual connection.** A coupling of classical randomness can pair two quantum preparations; their overlaps can be more informative than demanding that every entry of a large random table agree.

**Sources.** Watrous, Chapter 3, §3.2; [source preparation](../science/source_preparation.md), “Finite sampling accuracy” and “Circuit precision”; [source-resources bridge](BRIDGE.md#source-resources).

<a id="m09"></a>

### M09 — Contractivity, hybrid arguments, and complete receivers

**Central question.** Why does replacing the supplied state remain valid after a complicated receiver acts on it?

**Understanding target.** Trace-norm contractivity under channels carries a preparation comparison through postprocessing. Telescoping replacements control tensor-product or sequential implementation errors. Quantum memory, adaptive processing, and a quantum-valued output can be included in one receiver channel, with a final event represented by a measurement.

**Dependencies and story role.** Depends on [M06](#m06), [M07](#m07), and [M08](#m08). It separates the source comparison from the details of the learning algorithm.

**Conceptual connection.** A statistical reduction remains useful precisely because the receiver cannot increase the distinguishability introduced at its input.

**Sources.** Watrous, Chapter 3, §3.3.2, Corollary 3.40 and Proposition 3.41; [lattice examples](../science/lattice_examples.md), §1; [source preparation](../science/source_preparation.md), “Circuit precision.”

<a id="m10"></a>

### M10 — Centered random vectors and covariance operators

**Central question.** How does ordinary probabilistic centering produce a useful positive quantum operator?

**Understanding target.** A random classical label is a random basis vector. Its mean has the probabilities $`P_a(y)`$ as amplitudes, and its covariance is $`K_a=\mathrm{diag}P_a-|\mu_a\rangle\langle\mu_a|\succeq0`$. The covariance trace is $`1-c_a`$. Independence makes an expectation vanish when a centered address variable appears without a matching dependence on the other side.

**Dependencies and story role.** Depends on [M02](#m02), [M03](#m03), and [M04](#m04). This is the local probabilistic mechanism from which the frozen-source proof will be built.

**Conceptual connection.** Variance positivity becomes operator positivity, while the squared norm of a mean vector becomes a classical collision probability.

**Sources.** Watrous, Chapter 1, §§1.1.2 and 1.2.2, for the operator and expectation framework; [frozen sources](../science/frozen_sources.md), “Centered label vectors”; [covariance bridge](BRIDGE.md#covariance).

<a id="m11"></a>

### M11 — Permutations and coherence between copies

**Central question.** Which structure survives when copies share the same hidden preparation?

**Understanding target.** Tensor-factor permutations act unitarily, and the symmetric subspace contains tensor powers of a pure state. The symmetric projector and a normalized coherent permutation state have different normalization roles. A swap measurement can distinguish two copies of one pure state from two independent copies of its mixed ensemble average.

**Dependencies and story role.** Depends on [M01](#m01), [M05](#m05), and [M06](#m06). It identifies the cross-copy coherence that the frozen-source simulator must preserve.

**Conceptual connection.** Exchange symmetry is an observable feature of the joint experiment even when every single-copy marginal is identical.

**Sources.** Watrous, Chapter 7, §§7.1.1–7.1.2, especially Proposition 7.1; [model](../science/model.md), §2; [simulator](../science/simulator.md), “The label-register isometry.”

<a id="m12"></a>

### M12 — Synthesis: the complete noisy-example experiment

**Central question.** What must be specified before a claim about quantum-example advantage has a definite meaning?

**Understanding target.** The connected model includes the input law, conditional labels, hidden table, delivered registers, source schedule, receiver, and comparison experiment. It distinguishes $`\rho^{\otimes T}`$ from $`\mathbb E_F[(|\psi_F\rangle\langle\psi_F|)^{\otimes T}]`$, and fixes which randomness is averaged and which parameter is held fixed. Data access, quantum computation, and source-preparation cost are separate parts of the claim.

**Dependencies and story role.** Synthesizes [M01](#m01)–[M11](#m11) and ends the preliminaries. The resulting experiment is the object analyzed in the second phase.

**Conceptual connection.** Probability, operator theory, and physical access combine into one statistical experiment; none alone determines what the learner has been supplied.

**Sources.** Watrous, Chapter 2, §§2.1.2–2.2.2, and Chapter 3, §3.1.1; [model](../science/model.md); [interpretation](../science/interpretation.md); [experiment bridge](BRIDGE.md#experiment).

## Phase II — Narrative and innovation

<a id="m13"></a>

### M13 — The exact one-copy operator difference

**Central question.** Which part of a refreshed noisy example differs from an encoded classical example?

**Understanding target.** Averaging diagonal address blocks produces the classical label densities. Averaging distinct-address blocks produces outer products of mean label vectors. Their difference factors through an isometry and a rank-one-minus-diagonal operator, with weights $`r_a=p_ac_a/\bar c`$. The calculation works for arbitrary conditional laws without assuming a linear function.

**Dependencies and story role.** Depends on [M10](#m10) and [M12](#m12). It begins the project argument with an exact local identity, before introducing any learning assumption.

**Conceptual connection.** The coherent excess of a stochastic graph source is determined by first label moments, while its measured data depend on the full diagonal label laws.

**Sources.** Watrous, Chapter 1, §§1.1.2–1.1.3, and Chapter 2, §2.1.2; [F1](../science/refreshed_sources.md), “Exact one-copy identity”; [covariance bridge](BRIDGE.md#covariance).

<a id="m14"></a>

### M14 — From the F1 spectrum to an exact distance

**Central question.** Why does one positive eigenvalue determine the one-copy trace distance?

**Understanding target.** The rank-one-minus-diagonal difference has zero trace and, on nontrivial support, one positive eigenvalue. Its half trace norm is that eigenvalue, characterized by the secular equation in F1. Uniform translated noise yields $`D=c(1-1/N)`$; nonuniform inputs require the reweighted distribution $`r`$. Collision probability controls the scale, while the address weights determine the exact spectral factor.

**Dependencies and story role.** Depends on [M02](#m02), [M07](#m07), and [M13](#m13). It turns the moment identity into a fully operational, exact statement.

**Conceptual connection.** Symmetry simplifies a general spectral problem, but the uniform formula does not replace the nonuniform theorem.

**Sources.** Watrous, Chapter 1, §1.1.3, and Chapter 3, §§3.1.1–3.2; [F1](../science/refreshed_sources.md); [finite verification](../verification/README.md), the spectrum and endpoint cases.

<a id="m15"></a>

### M15 — Why the frozen source needs another proof

**Central question.** Why is a small one-copy distance insufficient to justify the product classical simulator for frozen copies?

**Understanding target.** The averaging order changes joint moments. A frozen table produces repeated copies of one pure state, whereas a refreshed source produces independent mixed specimens. Their swap behavior can differ despite identical one-copy marginals. The appropriate simulation target must retain permutation coherence rather than merely reproduce each marginal separately.

**Dependencies and story role.** Depends on [M11](#m11), [M12](#m12), and [M14](#m14). It identifies the obstacle that distinguishes S1 from a tensor-product application of F1.

**Conceptual connection.** Hidden classical memory in the preparation generates quantum correlations across emissions, so source schedules are operational assumptions.

**Sources.** Watrous, Chapter 2, §§2.1.2–2.1.3, and Chapter 7, §7.1.1; [model](../science/model.md), §2; [interpretation](../science/interpretation.md), “Purity and repeated copies.”

<a id="m16"></a>

### M16 — The global centered component

**Central question.** Which positive part of the frozen state can be isolated without conditioning away repeated addresses?

**Understanding target.** Write the source vector as its mean plus centered blocks, then retain the all-centered tensor terms at distinct addresses. In a cross term, the $`T`$ distinct centered ket variables require $`T`$ matching centered bra variables. Every other term has an unmatched mean-zero factor. This proves global cross-term cancellation and $`\Omega_T\succeq C_T`$ directly.

**Dependencies and story role.** Depends on [M10](#m10) and [M15](#m15). This is the central structural step of the frozen-source proof.

**Conceptual connection.** Independence organizes a tensor expansion by which address variables it contains; the highest distinct-address component is orthogonal, in the required operator expectation, to the remainder.

**Sources.** Watrous, Chapter 1, §§1.1.2 and 1.2.2, for the underlying tensor and probability tools; [S1](../science/frozen_sources.md), “A positive component of the full frozen source”; [frozen-proof bridge](BRIDGE.md#frozen-proof).

<a id="m17"></a>

### M17 — Matching that component inside the simulator

**Central question.** Why does the same centered component occur in a state prepared from classical examples?

**Understanding target.** The distinct-address permutation map is an isometry on arbitrary label operators. Its factorial normalization reproduces the surviving address matchings exactly. Expanding each label density as $`K_a+|\mu_a\rangle\langle\mu_a|`$ places the all-covariance term inside the simulator as a positive component. Its trace is $`w_T=\sum_{\mathrm{distinct}\ \mathbf a}\prod_i p_{a_i}(1-c_{a_i})`$.

**Dependencies and story role.** Depends on [M06](#m06), [M11](#m11), and [M16](#m16). It connects the source's probabilistic decomposition to the constructive simulation target.

**Conceptual connection.** The same operator can be recognized through two different preparations: centered source fluctuations and coherent permutations of classical-record label densities.

**Sources.** Watrous, Chapter 2, §2.2.2, and Chapter 7, §§7.1.1–7.1.2; [S1](../science/frozen_sources.md), “The same positive component in the simulator”; [simulator](../science/simulator.md).

<a id="m18"></a>

### M18 — The full S1 comparison

**Central question.** How do the common positive component and the two collision events yield the general theorem?

**Understanding target.** Subtracting $`C_T`$ leaves two positive residuals of trace $`1-w_T`$, giving $`D\le1-w_T`$. The union bound yields $`1-w_T\le T\bar c+\binom{T}{2}\alpha`$. This is a complete-state statement with exactly $`T`$ classical examples, a collision fallback, and explicit zero-core behavior when too many addresses must repeat.

**Dependencies and story role.** Depends on [M07](#m07), [M09](#m09), [M16](#m16), and [M17](#m17). It completes the unconditional statistical theorem before computation and hardness enter.

**Conceptual connection.** Operator overlap gives the quantum comparison, while elementary collision events bound its missing mass. Both are needed for the final operational criterion.

**Sources.** Watrous, Chapter 1, §§1.1.3 and 1.2.2, and Chapter 3, §§3.1.1 and 3.3.2; [S1](../science/frozen_sources.md); [frozen-proof bridge](BRIDGE.md#frozen-proof).

<a id="m19"></a>

### M19 — Implementing the exact-T symmetrizer

**Central question.** How can the simulator prepare its coherent output without hidden data-loading or erasure resources?

**Understanding target.** Uniform permutation preparation, reversible scans of the supplied classical list, and inversion from distinct output addresses produce the symmetrized state. All received labels remain in the output. A duplicate address triggers a fixed fallback, and bounded local preparation retries contribute an explicit implementation error rather than additional example requests.

**Dependencies and story role.** Depends on [M06](#m06), [M17](#m17), and [M18](#m18). It supplies the computational content required to turn S1 into an efficient reduction.

**Conceptual connection.** Clearing a permutation register is possible because its inverse is computable from known distinct addresses. That property is an explicit resource, not a general ability to erase unknown records.

**Sources.** Watrous, Chapter 2, §§2.2.1–2.2.2, and Chapter 7, §7.1.1; [simulator and costs](../science/simulator.md); [simulator bridge](BRIDGE.md#simulator). The inherited permutation mechanism is credited to [GMR2025](../references/RELATED_WORK.md#gmr2025).

<a id="m20"></a>

### M20 — Finite independence and the declared source budget

**Central question.** How can the source reproduce the required experiment without storing an exponentially large random table?

**Understanding target.** A $`T`$-copy density-matrix entry depends on at most $`2T`$ distinct table values. A hidden polynomial seed giving $`2T`$-wise independence therefore realizes that frozen experiment exactly; a refreshed single-copy experiment needs only pairwise independence. The source holder must also supply the signal circuit, finite label sampler, and input-state preparation, all with their costs charged.

**Dependencies and story role.** Depends on [M03](#m03), [M12](#m12), and [M19](#m19). It establishes that the claimed source access has an explicit finite-budget realization.

**Conceptual connection.** Moment degree determines the required independence order. Equality of the received finite-copy state does not require equality of the complete table distributions.

**Sources.** Watrous, Chapter 1, §1.2.2, and Chapter 2, §§2.1.2 and 2.2.2, for the probability and state-preparation framework; [P1](../science/source_preparation.md), including its Vandermonde proof and [Joffe1974](../references/RELATED_WORK.md#joffe1974) attribution; [source-resources bridge](BRIDGE.md#source-resources).

<a id="m21"></a>

### M21 — Finite laws and a complete accuracy budget

**Central question.** Which approximation losses must be included when mathematical sources become finite circuits?

**Understanding target.** Label-law total variation, per-copy preparation error, and simulator error are separate terms. A coupling gives $`D(\Omega_T(P),\Omega_T(\widetilde P))\le\sqrt{2T\delta}`$ for the input-weighted label-law error $`\delta`$. Circuit errors add through tensor hybrids, and the collision probabilities of the implemented laws are tracked explicitly. No agreement of every entry of a large table is required.

**Dependencies and story role.** Depends on [M08](#m08), [M09](#m09), [M19](#m19), and [M20](#m20). It closes the precision gap between the exact statistical theorem and an implementable experiment.

**Conceptual connection.** Classical coupling controls a quantum overlap, which then controls complete-experiment distinguishability.

**Sources.** Watrous, Chapter 1, §1.2.2, and Chapter 3, §§3.2 and 3.3.2; [source preparation](../science/source_preparation.md), “Finite sampling accuracy” and “Circuit precision”; [simulator](../science/simulator.md), bounded-circuit preparation.

<a id="m22"></a>

### M22 — Learning transfer and the role of a hardness assumption

**Central question.** What computational conclusion follows from an efficient source simulator?

**Understanding target.** Composing the simulator with a receiver preserves every success event up to the stated trace-distance loss, for a fixed signal and then for any prior. A decision comparison uses an error bound under each hypothesis. The resulting algorithm still performs quantum computation but receives classical examples. Computational hardness enters only through an assumption about that precisely specified classical-input problem.

**Dependencies and story role.** Depends on [M09](#m09), [M18](#m18), and [M21](#m21). It converts the unconditional source theorem into the reduction used by the learning applications.

**Conceptual connection.** A statistical simulation and a complexity assumption have different logical roles: the first transfers a capability, and the second rules out the transferred capability in a chosen family.

**Sources.** Watrous, Chapter 3, §§3.1.1 and 3.3.2; [L1](../science/lattice_examples.md), §1; [learning-transfer bridge](BRIDGE.md#learning-transfer).

<a id="m23"></a>

### M23 — The established scalar Fourier endpoint

**Central question.** Why can a scalar noisy quantum example still reveal its hidden linear function efficiently?

**Understanding target.** Fourier transformation converts bounded scalar errors into phases whose average remains large on a suitable nonzero frequency range. The output yields a secret candidate, and additional measured examples test it. The bounded-table argument applies even when that table is frozen. This positive endpoint is the established Grilo–Kerenidis–Zijlstra mechanism, with its access and parameter conditions retained.

**Dependencies and story role.** Depends on [M01](#m01), [M06](#m06), [M07](#m07), and [M22](#m22). It supplies the concrete easy quantum-source endpoint against which the entropy-based obstruction is compared.

**Conceptual connection.** A Fourier interference pattern uses source coherence that ordinary measured examples do not provide directly.

**Sources.** Watrous, Chapter 1, §§1.1.1–1.1.2, and Chapter 2, §2.3.1, for the unitary and measurement framework; [scalar endpoint](../science/lattice_examples.md), §2; [GKZ2019](../references/RELATED_WORK.md#gkz2019). The LWE algorithm is research-specific content, not a theorem attributed to the textbook.

<a id="m24"></a>

### M24 — Auxiliary labels and classically equivalent data

**Central question.** Can additional labels leave classical learning unchanged while changing the coherent source's power?

**Understanding target.** Appending $`m`$ independent uniform bits at each address preserves the classical scalar-LWE experiment up to locally generable auxiliary data. In the coherent source, those bits are a hidden address-dependent function, and the collision probability becomes $`c_\chi2^{-m}`$. S1 then supplies the conditional hard endpoint under the same specified classical-input hardness assumption.

**Dependencies and story role.** Depends on [M20](#m20), [M21](#m21), [M22](#m22), and [M23](#m23). It turns the general criterion into a source-access separation for classically equivalent learning data.

**Conceptual connection.** Extra recorded labels can alter interference even when they carry no information about the secret in the classical experiment. An address-independent tensor factor has another effect.

**Sources.** Watrous, Chapter 2, §§2.1.3 and 2.2.1, and Chapter 3, §3.3.2; [L2](../science/lattice_examples.md), §3; [source preparation](../science/source_preparation.md), “Elementary finite samplers and padded labels.”

<a id="m25"></a>

### M25 — Ring and module outputs with explicit parameter scope

**Central question.** Which parts of a ring or module learning problem control the simulation loss?

**Understanding target.** Independent output-error coefficients multiply collision probabilities, giving $`c_0^d`$ for one degree-$`d`$ polynomial label. Module rank changes the input domain, while the number of independently noisy output coefficients determines the entropy factor. Modular folding, the chosen ring, secret prior, error law, sample budget, and quantum classical-input hardness assumption all belong to the application statement.

**Dependencies and story role.** Depends on [M03](#m03), [M18](#m18), [M21](#m21), and [M22](#m22). It applies the theorem to structured labels while preserving the distinction between an entropy calculation and cryptographic hardness.

**Conceptual connection.** Algebraic structure defines the classical learning task; the source simulation itself uses conditional-label statistics and does not require a ring Fourier decoder.

**Sources.** Watrous, Chapter 1, §1.2.2, and Chapter 3, §3.3.2, for the probabilistic and operational transfer tools; [L3 and error laws](../science/lattice_examples.md), §§4–6; [lattice references and qualifications](../references/RELATED_WORK.md#lpr2013).

<a id="m26"></a>

### M26 — The one-copy coherent-deletion obstruction

**Central question.** Why is universal exact deletion of an unknown output coordinate not supplied by one example state?

**Understanding target.** The three-state witness in E1 requires incompatible inner products for a Stinespring environment. A pure target output forces a product purification, making the contradiction explicit. The conclusion concerns a universal exact one-copy channel acting on those states. S1 is the separate many-copy statement about an averaged source ensemble; the finite witness does not prove a general collective-learning impossibility.

**Dependencies and story role.** Depends on [M05](#m05), [M06](#m06), [M17](#m17), and [M22](#m22). It identifies the missing access in a proposed scalar extraction and distinguishes it from the valid address-based uncomputation in the simulator.

**Conceptual connection.** Classical coordinate projection, physical partial trace, and coherent compute–copy–uncompute are different operations with different prerequisites.

**Sources.** Watrous, Chapter 2, §§2.1.3 and 2.2.2; [E1](../science/label_erasure.md); [published-claim comparison](../references/RELATED_WORK.md#kimkim2024).

<a id="m27"></a>

### M27 — The channel comparison with reference systems

**Central question.** What changes when the random-example source is promoted to a channel accepting a chosen quantum input?

**Understanding target.** For a common collision value $`c`$, the refreshed append channel differs from its address-measuring version by $`c\,\mathrm{Ad}_W\circ(\mathrm{Id}-\Delta)`$. The completely bounded trace norm gives the exact half diamond distance $`c(1-1/N)`$, including inputs entangled with references. This is a stronger input interface with a distinct operational interpretation.

**Dependencies and story role.** Depends on [M06](#m06), [M09](#m09), [M13](#m13), and [M14](#m14). It extends the one-copy mechanism to a reference-robust channel statement without changing the learning theorem's access model.

**Conceptual connection.** Stabilizing a norm by a reference system distinguishes state comparison from channel discrimination; the address-measuring comparison channel also exposes the loss of entanglement transmission.

**Sources.** Watrous, Chapter 2, §2.2.2, and Chapter 3, §§3.3.2–3.3.3; [C1](../science/channels.md); [channel-consequences bridge](BRIDGE.md#channel-consequences).

<a id="m28"></a>

### M28 — Known-channel capacity and its separate meaning

**Central question.** What does the refreshed additive channel transmit when its full law and signal function are known?

**Understanding target.** The retained address makes the complement reproducible from the output, giving degradability. Symmetry identifies the maximally mixed optimal input, and the normalized Choi spectrum gives the project's coherent-information formula. The uniform-$`K`$ noise case yields $`Q=(\log_2N)/K`$. The capacity theorem and degradable-channel properties are imported tools; the channel calculation assumes known memoryless uses and unrestricted coding, separately from unknown-secret learning.

**Dependencies and story role.** Depends on [M02](#m02), [M06](#m06), [M09](#m09), and [M27](#m27). It develops a physical transmission consequence and fixes the limit of its relevance to S1 and L1.

**Conceptual connection.** Collision mass controls a coherent branch, while entropy differences quantify its asymptotic transmission rate. Channel capacity and computational learnability answer different questions.

**Sources.** Watrous, Chapter 5, §§5.1.1 and 5.2.3; Chapter 8, §8.1.1, Definition 8.14 and Proposition 8.15, §§8.2.1–8.2.2, and §8.4, Exercise 8.3, where degradable-channel properties are posed. [C2 and its primary references](../science/channels.md) supply the specialized proof and imported degradability results; [channel bridge](BRIDGE.md#channel-consequences) records that textbook coverage distinction.

<a id="m29"></a>

### M29 — Sharpness, verification, and the boundaries of the contribution

**Central question.** Which conclusions are established by the bounds, the finite checks, and the literature comparison?

**Understanding target.** The lower-bound example concerns the specified permutation simulator, not every simulator that might know the label law. Finite enumeration tests spectra, positivity, normalization, source schedules, and implementation identities; it does not prove the all-dimension theorem, lattice hardness, or scientific priority. Established noisy-example models, symmetrizers, and limited-independence tools are distinguished from the project's conditional-label comparison.

**Dependencies and story role.** Depends on [M14](#m14), [M18](#m18), [M21](#m21), and [M24](#m24)–[M28](#m28). It fixes the strength and provenance of the claims before the final synthesis.

**Conceptual connection.** A useful sufficient bound, an optimality claim, a computational assumption, and a numerical consistency check require different kinds of evidence.

**Sources.** Watrous, Chapter 3, §§3.1.1 and 3.3.2, for operational comparison; [interpretation](../science/interpretation.md), the specified-simulator lower bound and scope; [finite verification](../verification/README.md); [related work](../references/RELATED_WORK.md); [claim-boundaries bridge](BRIDGE.md#claim-boundaries).

<a id="m30"></a>

### M30 — Synthesis: when label entropy removes extra source power

**Central question.** How do the local moment identities, joint-state simulation, source construction, and learning applications form one complete argument?

**Understanding target.** The full chain runs from conditional classical label laws to mean vectors and positive covariances, then to a common component of the frozen source and an efficient classical-data-driven quantum simulator. Finite-budget preparation and precision make the experiment concrete. Learning hardness transfers only under its stated classical-input assumption; the one-copy deletion obstruction and known-channel capacity remain separately scoped companions. Analytical proofs, finite checks, imported results, and the candidate contribution retain distinct roles.

**Dependencies and story role.** Synthesizes [M13](#m13)–[M29](#m29), using the operational model assembled in [M12](#m12). It ends the map with the global scientific account rather than a new isolated technique.

**Conceptual connection.** Quantum purity and large coherent registers do not alone determine an advantage. The complete source experiment—including hidden randomness, retained records, copy correlations, and access—determines what quantum data can add beyond quantum processing of classical data.

**Sources.** Watrous, Chapter 2, §§2.1.2–2.2.2, Chapter 3, §§3.1.1 and 3.3.2, and Chapter 8, §§8.1.1–8.2.2, for the foundational operational framework; [scientific account](../science/README.md), [model and claim index](../science/model.md), [interpretation](../science/interpretation.md), and [claim-boundaries bridge](BRIDGE.md#claim-boundaries).

## Anchor and source navigation

The authoritative textbook pointers, access information, and scope of the single anchor are in [ANCHOR.md](ANCHOR.md). The topic-by-topic correspondence to the scientific files is in [BRIDGE.md](BRIDGE.md). The project files remain authoritative for F1, S1, P1, L1–L3, E1, and C1–C2. Their primary references identify the established research ingredients and the assumptions used in each application.
