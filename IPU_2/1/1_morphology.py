import cv2
from plotter import custom_plot

image = cv2.imread("line.bmp", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))
# OPENING = EROSION -> DILATION
opened_img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

num_labels, labels = cv2.connectedComponents(opened_img)
# 1 label is for the background
print(f"Num of circles = {num_labels - 1}")

custom_plot(image, opened_img, rows=1, cols=2)
