"""
EXPERIMENT 14
Title: Perspective Transformation
Aim: To perform Perspective Transformation on the given image using Python and OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp14_perspective.jpg"
if not os.path.exists(image_path):
    image_path = "input.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    rows, cols, ch = image.shape

    # Define 4 corner points in the source image and their mapped points
    pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
    pts2 = np.float32([[10, 80], [cols - 80, 20], [80, rows - 20], [cols - 20, rows - 80]])

    # Calculate perspective transform matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed_image)
    cv2.imwrite("perspective_transformed.jpg", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
