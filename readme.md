# lds

A drop-in replacement for `np.random`:

```python
import qm
import numpy as np

x_rng = np.random.uniform(0, 1, (10, 100))
x_lds = qp.halton.uniform(0, 1, (10, 100))
```

This library aims to make the low-discrepancy sequences (LDS) needed for quasi-monte carlo methods (QMC) more accessible. 

There are numerous libraries implementing various LDS. However, due to their nature, the API's they offer are dramatically different from a typical random number generator (particularly a multi-dimensional sampler like `np.random`), making implementing QMC far more tedious than it is often worth. 

Furthermore, for the using a multi-dimensional LDS is very error prone. 

## Implemented Sequences

The following sequences are implemented:

- Halton Sequences
- [TODO] Sobol Sequences

Supporting a wide variety of sequences is not the objective of this library, and the ones that have been included are there for a reason. 

Instead, it builds on these sequences to provide a more familiar interface for sampling from standard distributions in high-dimensions. 

## Implemented Distributions

Currently it supports:

Univariate Distributions:
- Uniform 
- Normal 
- Lognormal
- Exponential 
- Weibull
- Gamma
- Exponential

Multivariate Distributions:
- Normal
- [TODO] Student T