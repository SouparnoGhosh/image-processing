import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb_to_gray(rgb_image):
    return 0.2989 * rgb_image[:,:,0] + 0.5870 * rgb_image[:,:,1] + 0.1140 * rgb_image[:,:,2]

def highest_intensity(gray_image):
    unique, counts = np.unique(gray_image, return_counts=True)
    max_intensity_index = np.argmax(counts)
    return unique[max_intensity_index]

# Reads the image
img = mpimg.imread('tq.jpg')

# Converts the image to grayscale
gray_img = rgb_to_gray(img).astype(np.uint8)

# Displays the grayscale image
plt.imsave('tq_gray.jpg', gray_img, cmap='gray')

# Finds the highest intensity pixel
highest_intensity_pixel = highest_intensity(gray_img)
print(highest_intensity_pixel)