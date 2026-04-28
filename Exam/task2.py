import numpy as np
import matplotlib.pyplot as plt

Im = np.array([
    [0, 1, 2, 3, 2],
    [1, 0, 1, 2, 3],
    [3, 2, 1, 0, 2],
    [2, 3, 1, 0, 1],
    [2, 1, 2, 3, 1]
])

M = np.array([
    [1, 2, 1],
    [2, 3, 2],
    [1, 2, 1]
])

result = Im.copy()

for i in range(1, 4):
    for j in range(1, 4):
        values = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                values += [Im[i + di, j + dj]] * M[di + 1, dj + 1]
        result[i, j] = int(np.median(values))

print(result)

plt.figure(figsize=(6, 4))
plt.imshow(result, cmap="gray", vmin=0, vmax=3)

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        plt.text(j, i, str(result[i, j]), ha="center", va="center", fontsize=18)

plt.title("Result of median filtering")
plt.xticks([])
plt.yticks([])
plt.savefig("median_filter_result.png", dpi=300, bbox_inches="tight")
plt.show()