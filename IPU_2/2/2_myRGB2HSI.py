import cv2
import numpy as np
import matplotlib.pyplot as plt

def Myrgb2hsi(img):
    # Normalize to [0, 1]
    img = img / 255
    R, G, B = cv2.split(img)
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B) * (G - B))
    theta = np.arccos(num / (den + 1e-8))
    H = theta
    H[B > G] = 2*np.pi - H[B > G]
    H = H / (2 * np.pi)
    num = np.minimum(np.minimum(R, G), B)
    den = R + G + B
    den[den == 0] = 1e-8
    S = 1 - 3.0 * num / den
    I = (R + G + B) / 3.0
    return H, S, I

# Load the image
img = cv2.imread('ball.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert the image to HSI
H, S, I = Myrgb2hsi(img)

# Convert the image to HSI using OpenCV
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
H_opencv, S_opencv, V_opencv = cv2.split(img_hsv)
# Normalize to [0, 1]
H_opencv = H_opencv / 255
S_opencv = S_opencv / 255
V_opencv = V_opencv / 255

# Create a new figure
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

# Display the H, S, I images
axs[0, 0].imshow(H, cmap='gray')
axs[0, 0].set_xlabel('Hue')

axs[0, 1].imshow(S, cmap='gray')
axs[0, 1].set_xlabel('Saturation')

axs[0, 2].imshow(I, cmap='gray')
axs[0, 2].set_xlabel('Intensity')

# Display the H, S, V images from OpenCV
axs[1, 0].imshow(H_opencv, cmap='gray')
axs[1, 0].set_xlabel('Hue (OpenCV)')

axs[1, 1].imshow(S_opencv, cmap='gray')
axs[1, 1].set_xlabel('Saturation (OpenCV)')

axs[1, 2].imshow(V_opencv, cmap='gray')
axs[1, 2].set_xlabel('Value (OpenCV)')

# Display the difference images
axs[2, 0].imshow(np.abs(H - H_opencv), cmap='gray')
axs[2, 0].set_xlabel('Difference in Hue')

axs[2, 1].imshow(np.abs(S - S_opencv), cmap='gray')
axs[2, 1].set_xlabel('Difference in Saturation')

axs[2, 2].imshow(np.abs(I - V_opencv), cmap='gray')
axs[2, 2].set_xlabel('Difference in Intensity')

# Adjust the spacing between the subplots
plt.subplots_adjust(wspace=0.4, hspace=0.6)

plt.show()