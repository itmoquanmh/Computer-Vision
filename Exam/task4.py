import numpy as np
import matplotlib.pyplot as plt

H, W = 31, 41
origin_y, origin_x = 15, 20

img1 = np.zeros((H, W), dtype=np.uint8)
img2 = np.zeros((H, W), dtype=np.uint8)

def rect(img, x1, x2, y1, y2):
    """
    x: trái -> phải
    y: dưới -> trên
    fill rectangle = 1
    """
    r1 = origin_y - y2
    r2 = origin_y - y1
    c1 = origin_x + x1
    c2 = origin_x + x2
    img[r1:r2, c1:c2] = 1

# ===== Image 1: hình bên trái =====
# cột trắng chính
rect(img1, -6, 0, -11, 11)

# nhánh trên bên phải
rect(img1, 0, 8, 5, 11)

# nhánh dưới bên phải
rect(img1, 0, 8, -11, -5)

# nhánh giữa bên trái
rect(img1, -13, -6, -2, 3)

# ===== Image 2: hình bên phải =====
# khung trắng ngoài
rect(img2, -10, 10, -11, 11)

# khoét lỗ đen bên trong
rect(img2, -7, 7, -8, 8)
img2[origin_y-8:origin_y+8, origin_x-7:origin_x+7] = 0

# ===== XOR =====
result = np.logical_xor(img1, img2).astype(np.uint8)

# ===== Vẽ =====
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

titles = ["Image 1", "Image 2", "XOR Result"]
images = [img1, img2, result]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
    ax.axhline(origin_y, color="red", linestyle="--", linewidth=1)
    ax.axvline(origin_x, color="red", linestyle="--", linewidth=1)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.savefig("xor_result_correct.png", dpi=300, bbox_inches="tight")
plt.show()