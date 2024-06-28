import cv2
import numpy as np

def ImageBitQuantizer(im, k):
    # Calculates the quantization level
    level = 256 // (2 ** k)

    # Quantizing the image
    # Puts pixels in range [0, level-1]
    quantized_image = cv2.divide(im, level)
    # Multiplies the pixels by level
    quantized_image = cv2.multiply(quantized_image, level)
    # Converts the image to 8-bit
    quantized_image = np.uint8(quantized_image)

    return quantized_image

# Load the image
im = cv2.imread('pixel.jpg')

# Quantize the image to 3 bits
k = 3
quantized_image_gray = ImageBitQuantizer(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), k)
quantized_image_color = ImageBitQuantizer(im, k)

# Save the result
cv2.imwrite('quantized_image_color.jpg', quantized_image_color)
cv2.imwrite('quantized_image_gray.jpg', quantized_image_gray)