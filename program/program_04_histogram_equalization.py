"""
EXPERIMENT 4
Title: Histogram Equalization
Aim: To implement histogram equalization on a given image and compare it with the original image using OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Display original and equalized images side by side or separately
    cv2.imshow("Original Grayscale Image", gray_image)
    cv2.imshow("Histogram Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
