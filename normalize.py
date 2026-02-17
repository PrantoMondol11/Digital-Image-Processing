import matplotlib.pyplot as plt
import numpy as np


img = plt.imread("images.jpeg").astype(np.float32)

height, width, channels = img.shape


log_img = np.zeros((height, width, channels), dtype=np.float32)


for i in range(height):
    for j in range(width):
        for c in range(channels):
            log_img[i, j, c] = np.log1p(img[i, j, c])


max_val = log_img.max()
for i in range(height):
    for j in range(width):
        for c in range(channels):
            log_img[i, j, c] = log_img[i, j, c] / max_val


plt.imshow(log_img)
plt.title("Log-transformed & Normalized Image")
plt.axis("off")
plt.show()
