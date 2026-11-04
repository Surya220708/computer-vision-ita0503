"""
EXPERIMENT 22
Title: Morphological Closing Technique
Aim: To implement the Closing technique as a Morphological operation using OpenCV in Python.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp22_closing.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply morphological closing (dilation followed by erosion)
    closed_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Closed Image", closed_image)
    cv2.imwrite("closed_image.jpg", closed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
