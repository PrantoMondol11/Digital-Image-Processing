import numpy as np
import matplotlib.pyplot as plt
from skimage import color
import cv2

# Load images
source = cv2.imread("source.jpg")
reference = cv2.imread("ref.jpg")

# Check if images loaded
if source is None or reference is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)

# Convert to grayscale
source = color.rgb2gray(source)
reference = color.rgb2gray(reference)

# Convert to uint8
source = (source * 255).astype(np.uint8)
reference = (reference * 255).astype(np.uint8)

# Step 1: Calculate histograms
src_hist = np.zeros(256)
ref_hist = np.zeros(256)

for pixel in source.flatten():
    src_hist[pixel] += 1

for pixel in reference.flatten():
    ref_hist[pixel] += 1

# Step 2: Calculate PDF
src_pdf = src_hist / np.sum(src_hist)
ref_pdf = ref_hist / np.sum(ref_hist)

# Step 3: Calculate CDF
src_cdf = np.zeros(256)
ref_cdf = np.zeros(256)

src_cdf[0] = src_pdf[0]
ref_cdf[0] = ref_pdf[0]

for i in range(1, 256):
    src_cdf[i] = src_cdf[i-1] + src_pdf[i]
    ref_cdf[i] = ref_cdf[i-1] + ref_pdf[i]

# Step 4: Create mapping
lookup = np.zeros(256, dtype=np.uint8)

for i in range(256):
    diff = np.abs(ref_cdf - src_cdf[i])
    lookup[i] = np.argmin(diff)

# Step 5: Apply mapping
matched = np.zeros_like(source)

rows, cols = source.shape
for r in range(rows):
    for c in range(cols):
        matched[r, c] = lookup[source[r, c]]

# Display results
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Source Image")
plt.imshow(source, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Reference Image")
plt.imshow(reference, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Matched Image")
plt.imshow(matched, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
