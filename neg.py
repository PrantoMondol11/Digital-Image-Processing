import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("images.jpeg").copy()


original = img.copy()

height, width, channels = img.shape

for i in range(height):
    for j in range(width):
        for c in range(channels):
            img[i, j, c] = 255 - img[i, j, c]


plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(original)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img)
plt.title("Negative")
plt.axis("off")

plt.show()
