import matplotlib.pyplot as plt

from quasi.engines import halton_seq

seed = 1
n = 500

x = halton_seq(n, seed, 2)

y_right_base_right_seed = halton_seq(n, seed, 3)
y_wrong_base_right_seed = halton_seq(n, seed, 2)
y_right_base_wrong_seed = halton_seq(n, seed + n, 3)
y_wrong_base_wrong_seed = halton_seq(n, seed + n, 2)

plt.subplot(2, 2, 1)
plt.scatter(x, y_right_base_right_seed, s=2)
plt.title("Different Base, Same Seed (Correct)")
plt.subplot(2, 2, 2)
plt.scatter(x, y_right_base_wrong_seed, s=2)
plt.title("Different Base, Different Seed (Incorrect)")
plt.subplot(2, 2, 3)
plt.scatter(x, y_wrong_base_right_seed, s=2)
plt.title("Same Base, Same Seed (Very Incorrect)")
plt.subplot(2, 2, 4)
plt.scatter(x, y_wrong_base_wrong_seed, s=2)
plt.title("Same Base, Different Seed (Incorrect)")
plt.show()
