import matplotlib.pyplot as plt
import numpy as np


img = plt.imread("images.jpeg").astype(np.float32)

height, width, channels = img.shape

gray_img = np.zeros((height, width), dtype=np.float32)

for i in range(height):
    for j in range(width):
        r = img[i, j, 0]
        g = img[i, j, 1]
        b = img[i, j, 2]
        gray_img[i, j] = 0.299*r + 0.587*g + 0.114*b   


log_img = np.zeros((height, width), dtype=np.float32)

for i in range(height):
    for j in range(width):
        log_img[i, j] = np.log1p(gray_img[i, j])  


max_val = log_img.max()

for i in range(height):
    for j in range(width):
        log_img[i, j] = log_img[i, j] / max_val


plt.imshow(log_img, cmap="gray")
plt.title("Grayscale Log-Transformed Image")
plt.axis("off")
plt.show()
