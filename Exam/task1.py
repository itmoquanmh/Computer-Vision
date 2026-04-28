import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

A = np.zeros((15, 25), dtype=bool)

# A giống đề hơn
A[8:13, 2:23] = 1      # đáy dài
A[3:8, 8:16] = 1       # cột giữa rộng hơn

# B = origin + right + up
B = np.zeros((3, 3), dtype=bool)
B[1, 1] = 1   # origin
B[1, 2] = 1   # right
B[0, 1] = 1   # up

origin = (0, 0)

dilation = ndimage.binary_dilation(A, structure=B, origin=origin)
erosion = ndimage.binary_erosion(A, structure=B, origin=origin)
opening = ndimage.binary_dilation(
    ndimage.binary_erosion(A, structure=B, origin=origin),
    structure=B, origin=origin
)
closing = ndimage.binary_erosion(
    ndimage.binary_dilation(A, structure=B, origin=origin),
    structure=B, origin=origin
)

def show_img(ax, img, title):
    ax.imshow(img, cmap="gray_r", interpolation="nearest")
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True, color="lightgray", linewidth=0.5)

fig, axes = plt.subplots(2, 3, figsize=(13, 8))

show_img(axes[0,0], A, "A")
show_img(axes[0,1], B, "B: origin + right + up")
show_img(axes[0,2], dilation, "a) Dilation A ⊕ B")
show_img(axes[1,0], erosion, "b) Erosion A ⊖ B")
show_img(axes[1,1], opening, "c) Opening")
show_img(axes[1,2], closing, "d) Closing")

plt.tight_layout()
plt.savefig("morphology_corrected.png", dpi=300, bbox_inches="tight")
plt.show()