# Finite verification

Run the checks from the repository root:

```bash
python -m pip install -r requirements.txt
python verification/run_all.py
```

The pinned dependency is NumPy 2.3.5, which requires Python 3.11 or newer. The recorded run used Python 3.12.14 and NumPy 2.3.5. The script writes [verified_results.json](verified_results.json), prints one status line per case, and exits nonzero if any check fails. To keep a separate result file:

```bash
python verification/run_all.py --output /tmp/quantum_example_entropy_results.json
```

These are deterministic **finite-dimensional consistency checks**, evaluated with floating-point linear algebra. They do not prove the theorems for arbitrary dimensions, establish cryptographic hardness, or benchmark a large-scale implementation. The proofs are in [F1](../science/refreshed_sources.md), [S1](../science/frozen_sources.md), and [C1–C2](../science/channels.md).

## What is constructed independently

The source density matrices are built by enumerating every label table in each finite example. For a table, the script constructs its pure specimen directly, tensors the specimen when testing a frozen source, and then averages with the actual table probability.

The classical-data simulator is built separately by enumerating exactly $`T`$ independent classical record tuples. On distinct addresses, it prepares the normalized coherent superposition of their permutations. On any duplicate address, it emits a fixed pure fallback state. It neither uses a hidden error table nor resamples until success.

For the channel checks, the script enumerates the isometries corresponding to all tables and applies their mixture directly. It separately computes the analytic spectral expressions for comparison.

## Coverage

| Cases | Scientific risk addressed |
|---|---|
| Uniform additive, nonuniform conditional, one-address, and deterministic-label sources | Normalization of the mean label vectors; the factor $`\bar c`$; the exact F1 spectrum and secular root; endpoint behavior |
| Label covariance in every fresh case | Positivity and trace of $`\operatorname{diag}P_a-|\mu_a\rangle\langle\mu_a|`$ |
| Frozen two- and three-copy ensembles, nonuniform inputs, product labels, and more copies than supported addresses | Global cross-term cancellation; positivity of both common-core remainders; correct core weight; permutation factorials; exact-$`T`$ collision fallback |
| Symmetrization isometries on arbitrary quantum label systems | The coherent-permutation map is an isometry on entangled or mixed label inputs when addresses are distinct |
| Frozen versus refreshed SWAP control | A frozen pure source cannot be replaced by independent copies of its one-copy average; the permutation simulator preserves the relevant copy coherence |
| Biased, uniform-support, and deterministic channel errors | C1 with reference systems; full Choi spectrum; exact C2 formula; uniform-input optimality on selected finite probes; uniform-support equality |
| Explicit Stinespring environment | The complementary channel is reproduced by measuring the retained output address and preparing its conditional environment state |
| Flagged channel calculation | The flagged coherent information is $`cS(\omega)`$; forgetting the flag costs between zero and $`h_2(c)`$ |
| Common additive-shift control | Common output noise is a different coherent channel and becomes identity tensor noise after the known function is undone |
| Finite-field hashes | Pairwise independence suffices for one emitted state, can fail for two frozen copies, and four-wise independence reproduces that two-copy moment |
| Scalar Fourier examples | Direct Fourier transforms of four bounded-error tables reproduce the stated success lower bound; exhaustive wrong-secret checks validate the conservative candidate-verification bound; independent table averaging reproduces the Fourier probability formula |
| Label-erasure witness | The required environment Gram matrix is not positive for the one-copy deletion task, while the corresponding two-copy matrix is positive; the finite witness is not mistaken for a many-copy impossibility theorem |
| Folded Gaussian examples | Direct modular sums check normalization, collision probability versus maximum point mass, and the stated $`2/\sigma`$ bound at three finite parameter choices |

The largest dense matrix in the selected cases has dimension 216; the largest pure-state Fourier array has 4,913 amplitudes. The small alphabets deliberately permit complete table enumeration; no table distribution is approximated by Monte Carlo sampling. The finite Gaussian sums truncate at eight times the width, with omitted mass below $`10^{-80}`$ in the selected cases; the general bound is proved analytically in [Lattice examples](../science/lattice_examples.md).

The channel reference and input probes use a fixed pseudorandom seed, recorded in the JSON. They check particular instances of the analytic identities. They do not numerically optimize the diamond norm or prove the uniform-input optimum.

## Limited-independence control

The hash check uses $`\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)`$. It evaluates all affine or cubic polynomials on the four field elements and applies the field trace to obtain binary labels.

All 16 affine seeds give pairwise-independent labels. Their one-copy averaged state agrees exactly, to numerical precision, with the fully independent table ensemble. Their two-copy frozen moment differs by trace distance 0.09375.

All 256 cubic seeds give four-wise-independent labels. Their two-copy frozen moment agrees with the fully independent ensemble. This negative control prevents accidentally using a pairwise-independent source realization where the frozen-source analysis needs four-wise independence.

The example checks one small family. The general bounded-copy construction and its resource accounting are in [Source preparation](../science/source_preparation.md).

## Recorded result

The stored run passed **18 cases and 321 numerical checks**. The absolute acceptance tolerance is $`5\times10^{-10}`$. The JSON records each residual or inequality, the selected parameters, software versions, run time, and the SHA-256 hash of the executed script.

Representative checks include:

- A biased ternary-label source with $`N=3`$ has $`c=0.46`$ and trace distance $`0.46(1-1/3)=0.306666\ldots`$, matching the entire predicted difference spectrum.
- The frozen SWAP-test acceptance is 1, whereas the refreshed-source acceptance in the control is 0.65625. The classical-data permutation simulator also has acceptance 1.
- Uniform noise on two outcomes has channel capacity $`(\log_2 3)/2`$ in the tested three-address channel.
- The pairwise-hash frozen two-copy mismatch is retained as an expected nonzero result, rather than hidden by a tolerance test.

A passing run supports the consistency of the stated formulas, normalizations, and implementation of the finite simulator. The general statements rely on their analytic proofs, and any lattice consequence relies on the explicitly stated classical hardness assumption.

