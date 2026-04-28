import numpy as np
import matplotlib.pyplot as plt

# ===== Các điểm nằm trên đường ngang =====
# points = [(1, 3), (2, 3), (3, 3), (4, 3)]
points = [(1, 4), (2, 4), (3, 4), (4, 4)]
# ===== Không gian tham số =====
theta = np.linspace(0, np.pi, 200)
plt.figure(figsize=(6,5))

# ===== Vẽ các đường sin trong Hough space =====
for (x, y) in points:
    rho = x * np.cos(theta) + y * np.sin(theta)
    plt.plot(theta, rho)

# ===== Đánh dấu giao điểm (đường y = 3) =====
theta0 = np.pi/2
rho0 = 4
plt.scatter(theta0, rho0, color='red', s=100, label='Detected line')

# ===== Trang trí =====
plt.title("Hough Transform (Parameter Space)")
plt.xlabel("theta")
plt.ylabel("rho")
plt.legend()
plt.grid(True)

# ===== Lưu file =====
plt.savefig("hough_transform_result.png", dpi=300)
plt.show()