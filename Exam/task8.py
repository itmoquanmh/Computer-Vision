import numpy as np
from scipy.ndimage import label

I = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 1, 1]
])

# 8-connectivity: xét cả ngang, dọc, chéo
structure = np.ones((3, 3), dtype=int)

# Đếm vùng của pixel 1
labeled_1, num_1 = label(I == 1, structure=structure)

# Đếm vùng của pixel 0
labeled_0, num_0 = label(I == 0, structure=structure)

print("Labeled 1:")
print(labeled_1)
print("Number of components for 1:", num_1)

print("\nLabeled 0:")
print(labeled_0)
print("Number of components for 0:", num_0)

print("\nTotal components:", num_1 + num_0)