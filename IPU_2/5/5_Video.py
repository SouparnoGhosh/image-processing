import cv2
import numpy as np
from collections import deque

# Load the video
cap = cv2.VideoCapture("traffic.3gp")

# Initialize the deque to store the last N frames
N = 5
frames = deque(maxlen=N)

while True:
    return_flag, frame = cap.read()
    if not return_flag:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Add the frame to the deque
    frames.append(gray)

    # Calculate the mean and median frames
    mean_frame = np.mean(frames, axis=0)
    median_frame = np.median(frames, axis=0)

    # Calculate the absolute difference between the current frame and the mean and median frames
    mean_diff = cv2.absdiff(gray, mean_frame.astype(np.uint8))
    median_diff = cv2.absdiff(gray, median_frame.astype(np.uint8))

    # Apply a binary threshold to the difference images
    _, mean_thresh = cv2.threshold(mean_diff, 20, 255, cv2.THRESH_BINARY)
    _, median_thresh = cv2.threshold(median_diff, 20, 255, cv2.THRESH_BINARY)

    # Display the threshold images
    cv2.imshow("Mean Threshold", mean_thresh)
    cv2.imshow("Median Threshold", median_thresh)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
