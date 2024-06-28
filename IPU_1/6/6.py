import cv2
import numpy as np

# Loads the main image and the template
main_img = cv2.imread('hills.jpeg')
template = cv2.imread('template.png')

# results = list to store the results of template matching at each scale
results = []

# Gets the aspect ratio of the template to match the red rectangle to the template
orig_h, orig_w = template.shape[:-1]
aspect_ratio = orig_w / orig_h

# Iterate over scales from 0.5 to 2.5 in steps of 0.1
for scale in np.arange(0.5, 2.5, 0.1):
    # Resize the template according to the scale while maintaining aspect ratio
    new_h = int(orig_h * scale)
    new_w = int(new_h * aspect_ratio)
    resized_template = cv2.resize(template, (new_w, new_h))

    # Skip this iteration if the resized template is larger than the main image
    if main_img.shape[0] < new_h or main_img.shape[1] < new_w:
        continue

    # Performs template matching
    res = cv2.matchTemplate(main_img, resized_template, cv2.TM_CCOEFF_NORMED)

    # Finds the location of the maximum correlation (top left corner of the best match rectangle)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Store the result
    results.append((max_val, max_loc, new_w, new_h))

# Find the result with the highest correlation
max_val, max_loc, w, h = max(results, key=lambda x: x[0])

# Draws a rectangle at the location of the maximum correlation
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
# Draws a red rectangle around the detected template with a thickness of 2 pixels
cv2.rectangle(main_img, top_left, bottom_right, (0, 0, 255), 2)

# Save the result
cv2.imwrite('result.jpg', main_img)