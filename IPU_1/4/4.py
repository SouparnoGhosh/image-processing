import cv2
import numpy as np

def apply_filter(im, filter):
    # Get the dimensions of image and filter to calculate padding
    height, width = im.shape
    f_height, f_width = filter.shape
    pad_height, pad_width = f_height // 2, f_width // 2

    # Pad the image with reflection
    padded_im = np.pad(im, ((pad_height, pad_height), (pad_width, pad_width)), mode='reflect')

    # Apply the filter
    filtered_im = np.zeros_like(im)
    for i in range(height):
        for j in range(width):
            filtered_im[i, j] = np.sum(padded_im[i:i+f_height, j:j+f_width] * filter)
    return filtered_im.astype(np.uint8)

def apply_median_filter(im, kernel_size):
    # Getting pad size
    height, width = im.shape
    pad_size = kernel_size // 2

    padded_im = np.pad(im, pad_size, mode='reflect')
    filtered_im = np.zeros_like(im)

    for i in range(height):
        for j in range(width):
            filtered_im[i, j] = np.median(padded_im[i:i+kernel_size, j:j+kernel_size])
    return filtered_im.astype(np.uint8)


if __name__ == '__main__':
    im = cv2.imread('noise.tiff', cv2.IMREAD_GRAYSCALE)

    avg_filter = np.ones((3, 3)) / 9
    weighted_avg_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

    avg_im = apply_filter(im, avg_filter)
    weighted_avg_im = apply_filter(im, weighted_avg_filter)

    median_im_3x3 = apply_median_filter(im, 3)
    median_im_5x5 = apply_median_filter(im, 5)
    median_im_optimum = apply_median_filter(im, 5)

    cv2.imwrite('avg_im.tiff', avg_im)
    cv2.imwrite('weighted_avg_im.tiff', weighted_avg_im)
    cv2.imwrite('median_im_3x3.tiff', median_im_3x3)
    cv2.imwrite('median_im_5x5.tiff', median_im_5x5)
    cv2.imwrite('median_im_optimum.tiff', median_im_optimum)