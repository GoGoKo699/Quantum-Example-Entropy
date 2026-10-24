# Scientific account

The main question is when noisy quantum examples can be reproduced by a quantum circuit whose only data input is ordinary classical examples. The central theorem covers an arbitrary hidden conditional-label law and repeated copies of a single pure state selected by a hidden random table.

## A connected reading route

1. [Model and result index](model.md): define classical data, independently sampled labels, refreshed versus frozen sources, collision probabilities and the allowed access.
2. [Frozen sources](frozen_sources.md): prove the general simulation theorem by exhibiting a positive operator shared by the true source and the simulator.
3. [Simulator](simulator.md): prepare coherent permutations from exactly the supplied classical list, with a collision fallback and explicit finite-precision costs.
4. [Source preparation](source_preparation.md): compile the source using finite independence, including the copy-budget, input-preparation and sampler assumptions.
5. [Lattice examples](lattice_examples.md): transfer learning guarantees, contrast scalar and vector labels, and state the exact conditional LWE and Ring-LWE consequences.
6. [Label erasure](label_erasure.md): show why discarding unknown output coordinates does not implement coherent scalar extraction.
7. [Interpretation](interpretation.md): connect purity, collision entropy, source access and computational hardness.

Two companion topics can be read alongside that route. [Refreshed sources](refreshed_sources.md) gives an exact one-copy trace-distance identity and its nonuniform generalization. [Channels](channels.md) develops the reference-robust channel distance and known-channel capacity consequences.

## Proof dependencies

| Claim | Depends on |
|---|---|
| F1: exact refreshed-source distance | First and second label moments; rank-one minus diagonal spectrum |
| S1: frozen-source simulation | Independent centered label blocks; distinct-address sector; coherent-permutation isometry; a common positive operator |
| P1: finite source compilation | Explicit signal and input preparation; finite-randomness sampler; pairwise or $`2T`$-wise independence |
| L1: learning transfer | S1 or F1, efficient simulator, trace-distance contractivity |
| L2: auxiliary-label separation | L1, the established scalar Fourier learner, an explicit classical-input LWE hardness assumption |
| L3: ring/module consequence | L1 and product coefficient collision probability, with an explicit classical-input hardness assumption |
| E1: label deletion obstruction | Stinespring dilation and preservation of inner products |
| C1–C2: channel consequences | F1's moment decomposition, diamond-norm discrimination and established degradable-channel theory |

The [related work](../references/RELATED_WORK.md) identifies imported methods and comparisons at the theorem level. The [verification account](../verification/README.md) documents finite checks and their limits. The general claims are established by the proofs and their stated assumptions; numerical examples do not establish asymptotic hardness or novelty.
