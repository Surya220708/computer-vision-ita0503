"""
EXPERIMENT 19
Title: Morphological Erosion Technique
Aim: To implement the Erosion Morphological operation using OpenCV in Python.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp19_erosion.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Define 5x5 structuring element
    kernel = np.ones((5, 5), np.uint8)

    # Apply morphological erosion
    eroded = cv2.erode(binary, kernel, iterations=1)

    cv2.imshow("Original Binary Image", binary)
    cv2.imshow("Morphological Erosion", eroded)
    cv2.imwrite("morph_erosion.jpg", eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
