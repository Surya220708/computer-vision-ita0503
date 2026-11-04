"""
EXPERIMENT 16
Title: Sobel Filter Edge Detection
Aim: To implement the Sobel algorithm using OpenCV to filter the input image and detect edges.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp16_sobel.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter in X and Y directions
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute absolute scale values
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine both gradient images (50% X + 50% Y)
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Combined Edges", sobel_combined)

    cv2.imwrite("sobel_x.jpg", sobel_x)
    cv2.imwrite("sobel_y.jpg", sobel_y)
    cv2.imwrite("sobel_combined.jpg", sobel_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
