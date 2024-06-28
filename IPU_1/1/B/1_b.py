import cv2
import numpy as np

# Load the foreground image
foreground = cv2.imread('foreground.jpg')

# Load the background image
background = cv2.imread('background.jpg')

# Resize background to match the size of foreground image
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

# Convert the images to HSV color space
hsv_foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)

# Define range of green color in HSV
# Hue - Color Type (0 - Red, 60 - Green, 120 - Blue)
# Saturation - (0 - White, 255 - Pure Color)
# Value - (0 - Black, 255 - Bright)
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Threshold the HSV image to get only green colors (These colors become white 255, rest becomes black 0)
mask = cv2.inRange(hsv_foreground, lower_green, upper_green)

# Invert the mask (black becomes white, white becomes black)
mask_inv = cv2.bitwise_not(mask)

# Bitwise-AND mask and original image
foreground_img = cv2.bitwise_and(foreground, foreground, mask=mask_inv)
background_img = cv2.bitwise_and(background, background, mask=mask)

# Add the two images
merged = cv2.add(foreground_img, background_img)

# Save the result
cv2.imwrite('merged.jpg', merged)