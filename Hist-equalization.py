import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv2.imread("input.jpg", 0)

# Step 1: Calculate Histogram
hist = np.zeros(256)

for pixel in image.flatten():
    hist[pixel] += 1

# Step 2: Calculate PDF
pdf = hist / np.sum(hist)

# Step 3: Calculate CDF
cdf = np.zeros(256)
cdf[0] = pdf[0]

for i in range(1, 256):
    cdf[i] = cdf[i-1] + pdf[i]

# Step 4: Create transformation function
L = 256
transform = np.round((L - 1) * cdf).astype(np.uint8)

# Step 5: Map new pixel values
equalized = np.zeros_like(image)

rows, cols = image.shape
for r in range(rows):
    for c in range(cols):
        equalized[r, c] = transform[image[r, c]]

# Display Original vs Equalized
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Equalized Image")
plt.imshow(equalized, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
