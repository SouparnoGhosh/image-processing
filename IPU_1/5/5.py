import cv2

# Read the image
image = cv2.imread('clown.png', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian smoothing
sigma = 1  # sigma - standard deviation of the Gaussian distribution
multiple = 1  # multiple - multiple of sigma
ksize = (2 * int(multiple * sigma) + 1, 2 *
         int(multiple * sigma) + 1)  # ksize - size of the kernel
smoothed = cv2.GaussianBlur(image, ksize, sigma)

# Apply Canny edge detection
edges_canny = cv2.Canny(smoothed, 100, 200)

# Apply Laplacian filter
# cv2.CV_64F is used to represent the output image depth as 64-bit floating point
edges_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Apply Sobel filter
# ksize = kernel size
edges_sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
edges_sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = edges_sobelx + edges_sobely

# Save the images
cv2.imwrite('clown_canny.png', edges_canny)
cv2.imwrite('clown_laplacian.png', edges_laplacian)
cv2.imwrite('clown_sobel.png', edges_sobel)
