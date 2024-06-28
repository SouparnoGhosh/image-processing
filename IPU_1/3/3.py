import cv2
import numpy as np

# Loads the image
im = cv2.imread('spine.tiff', cv2.IMREAD_GRAYSCALE)

# Normalizes the image to the range 0-1
im = im / 255.0

# log transformation
c = 2.0
# log_image = c * np.log(1 + im)
log_image = c * np.log1p(im)

# power-law transformation
c = 1.0 
r = 0.6 
power_law_image = c * np.power(im, r)

# Scale the results back to the range 0-255
log_image = np.uint8(log_image * 255)
power_law_image = np.uint8(power_law_image * 255)

# Save the results
cv2.imwrite('log_spine.tiff', log_image)
cv2.imwrite('power_law_spine.tiff', power_law_image)