# Learning Quantum Example Entropy

A noisy quantum example can be pure while the source's hidden randomness still limits what a receiver can learn. The learning route connects that observation to an operational result: under a collision-probability condition, a quantum circuit fed ordinary classical examples reproduces the entire received experiment up to an explicit error, including correlations between copies.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [anchor guide](ANCHOR.md) identifies the source edition and focused readings. The book supplies the mathematical foundations; the project's own pages supply the conditional-label argument, source constructions and learning consequences.

## Choose a reading route

| Reader's purpose | Route |
|---|---|
| See the mechanism in a small complete example | [Two addresses and noisy labels](WORKED_EXAMPLE.md), then [the Watrous bridge](BRIDGE.md) |
| Build the conceptual picture systematically | [The 30-milestone map](MILESTONES.md), using the [anchor](ANCHOR.md) and [bridge](BRIDGE.md) beside the scientific pages |
| Read the main proof directly | [Model](../science/model.md), [frozen-source theorem S1](../science/frozen_sources.md), and [simulator construction](../science/simulator.md) |
| Understand the LWE consequence | [Learning transfer and lattice examples](../science/lattice_examples.md), [label deletion](../science/label_erasure.md), and [related work](../references/RELATED_WORK.md) |
| Reproduce finite instances | [Verification guide](../verification/README.md) |

## The common 30-milestone map

The map has two phases. **M01–M12** connect finite registers, probabilities, operator order, quantum states and channels, distinguishability, independence and permutations into a precise source-access model. **M13–M30** build the fresh-source identity and frozen-source proof, make the simulator and source construction explicit, and connect them to lattice learning, coherent label deletion and channel transmission.

This allocation follows the project's scientific dependencies. Each phase moves from individual objects and mechanisms to an integrated account. The milestones give every reader the same conceptual targets and source pointers; the canonical science contains the detailed proofs and specialist qualifications.

The [worked example](WORKED_EXAMPLE.md) makes the first bridge concrete: two addresses already distinguish fresh emissions from copies of a frozen pure state. The [source-to-project bridge](BRIDGE.md) then explains how centered label covariances and coherent permutations turn the textbook tools into the general result.

## Keep the operational question in view

The comparison changes the **source of examples**, while keeping quantum computation available. Its frozen-source distance averages over the hidden table chosen at the beginning of an experiment. Its lattice consequences assume quantum hardness of the specified ordinary classical-input problem. Its capacity companion concerns a known memoryless channel. These distinctions are part of the result and remain visible throughout the route.

Return to the [scientific entrypoint](../science/README.md) for the authoritative claim map, or to the [repository overview](../README.md) for the principal conclusions.
