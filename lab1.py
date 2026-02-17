import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# Read the image
img1 = mpimg.imread('images.jpeg')

img = np.array(img1)
img2=np.copy(img)
for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            img[i][j][k]=img2[(len(img2)-i-1)][len(img[i])-j-1][k]

print(img.size)  # Print the shape of the image


print(img)  # Print the pixel values of the image

plt.imshow(img)
plt.axis('off')  # Turn off axis numbers and ticks  

plt.show()  # Display the image