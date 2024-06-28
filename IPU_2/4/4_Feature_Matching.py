import cv2


def sift_feature_matching(query_image, train_image):
    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(query_image, None)
    kp2, des2 = sift.detectAndCompute(train_image, None)

    # Initialize brute-force matcher
    bf = cv2.BFMatcher()

    # Match descriptors
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.5 * n.distance:
            good_matches.append(m)

    # Draw matches - None - no output image provided to draw matches upon
    matched_img = cv2.drawMatches(query_image, kp1, train_image, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return matched_img


# Load images
query_image = cv2.imread("query.jpg", cv2.IMREAD_GRAYSCALE)
train_image = cv2.imread("train.jpg", cv2.IMREAD_GRAYSCALE)

# Perform feature matching
matched_img = sift_feature_matching(query_image, train_image)

# Display the matched image
cv2.imshow("Feature Matching Result", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
