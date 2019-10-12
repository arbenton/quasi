import numpy as np

from quasi.distributions import Halton
import matplotlib.pyplot as plt

halton = Halton(2)

n_samples = 500

plt.figure(figsize=(6, 10))

lds = halton.uniform(size=(2, n_samples))
rnd = np.random.uniform(size=(2, n_samples))
plt.subplot(4, 2, 1)
plt.axis('off')
plt.title("RNG")
plt.ylabel("Uniform")
plt.scatter(rnd[0, :], lds[1, :], s=1)
plt.subplot(4, 2, 2)
plt.axis('off')
plt.title("LDS")
plt.scatter(lds[0, :], lds[1, :], s=1)

lds = halton.normal(size=(2, n_samples))
rnd = np.random.normal(size=(2, n_samples))
plt.subplot(4, 2, 3)
plt.axis('off')
plt.ylabel("Normal")
plt.scatter(rnd[0, :], lds[1, :], s=1)
plt.subplot(4, 2, 4)
plt.axis('off')
plt.scatter(lds[0, :], lds[1, :], s=1)

lds = halton.exponential(size=(2, n_samples))
rnd = np.random.exponential(size=(2, n_samples))
plt.subplot(4, 2, 5)
plt.axis('off')
plt.ylabel("Exponential")
plt.scatter(rnd[0, :], lds[1, :], s=1)
plt.subplot(4, 2, 6)
plt.axis('off')
plt.scatter(lds[0, :], lds[1, :], s=1)

lds = halton.lognormal(size=(2, n_samples))
rnd = np.random.lognormal(size=(2, n_samples))
plt.subplot(4, 2, 7)
plt.axis('off')
plt.ylabel("Lognormal")
plt.scatter(rnd[0, :], lds[1, :], s=1)
plt.subplot(4, 2, 8)
plt.axis('off')
plt.scatter(lds[0, :], lds[1, :], s=1)

plt.savefig("distributions.pdf")