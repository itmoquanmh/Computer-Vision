import numpy as np
import matplotlib.pyplot as plt

Im = np.array([
    [0, 1, 2, 3, 2],
    [1, 0, 1, 2, 3],
    [3, 2, 1, 0, 2],
    [2, 3, 1, 0, 1],
    [2, 1, 2, 3, 1]
])

result = Im.copy()

for i in range(1, 4):
    for j in range(1, 4):
        window = Im[i-1:i+2, j-1:j+2].flatten()
        result[i, j] = np.sort(window)[0]   # r = 1

print(result)

plt.figure(figsize=(5, 5))
plt.imshow(result, cmap="gray", vmin=0, vmax=3)

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        plt.text(j, i, str(result[i, j]), ha="center", va="center", fontsize=20)

plt.xticks([])
plt.yticks([])
plt.title("Rank filtering, r = 1, mask 3x3")
plt.savefig("rank_filter_r1_result.png", dpi=300, bbox_inches="tight")
plt.show()