"""
EXPERIMENT 13
Title: Affine Transformation
Aim: To perform Affine Transformation on the given image using Python and OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp13_affine.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    rows, cols, ch = image.shape

    # Define 3 source points and their corresponding destination points
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Compute affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine warp
    transformed_image = cv2.warpAffine(image, matrix, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", transformed_image)
    cv2.imwrite("affine_transformed.jpg", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
