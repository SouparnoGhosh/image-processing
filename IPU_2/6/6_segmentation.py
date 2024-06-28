import cv2
import numpy as np
from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt

def segment_buildings(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to RGB (OpenCV uses BGR by default)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply SLIC and convert to grayscale
    # Superpixel segmentation
    segments = slic(img_rgb, n_segments=500, compactness=100)
    segments_rgb = label2rgb(segments, img_rgb, kind='avg')

    # Display the original and segmented images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    axs[1].imshow(segments_rgb)
    axs[1].set_title('Superpixel Segmented Image')
    axs[1].axis('off')

    plt.subplots_adjust(wspace=0.2)
    plt.show()

# Usage
segment_buildings('city.jpg')