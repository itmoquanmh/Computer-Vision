import numpy as np
import matplotlib.pyplot as plt

# ===== Input =====
Im1 = np.array([
    [150, 180, 140],
    [110, 120, 90],
    [130, 80, 30]
], dtype=float)

Im2 = np.array([
    [70, 110, 120],
    [80, 90, 130],
    [60, 110, 140]
], dtype=float)

# ===== Step 1: scale 30% =====
Im1_scaled = 0.3 * Im1
Im2_scaled = 0.3 * Im2

# ===== Step 2: cộng =====
Im = Im1_scaled + Im2_scaled

# ===== Làm tròn cho đẹp =====
Im = np.round(Im).astype(int)

print("Result matrix:")
print(Im)

# ===== Hiển thị & xuất ảnh =====
plt.figure(figsize=(4,4))
plt.imshow(Im, cmap="gray")

# in số lên ảnh
for i in range(Im.shape[0]):
    for j in range(Im.shape[1]):
        plt.text(j, i, str(Im[i, j]),
                 ha='center', va='center',
                 color='red', fontsize=16)

plt.title("Result: 0.3*Im1 + 0.3*Im2")
plt.xticks([])
plt.yticks([])

# ===== Lưu file =====
plt.savefig("image_sum_result.png", dpi=300, bbox_inches='tight')
plt.show()