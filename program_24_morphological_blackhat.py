"""
EXPERIMENT 24
Title: Morphological Black Hat Technique
Aim: To implement the Black Hat technique as a Morphological operation using OpenCV in Python.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp24_blackhat.jpg"
if not os.path.exists(image_path):
    image_path = "sample.jpg"
    if not os.path.exists(image_path):
        image_path = "image.jpg"

# Read in grayscale mode
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Define rectangular structuring element (5x5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Apply Black Hat operation (Closed image minus Original: isolates dark local elements)
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow("Black Hat Image", blackhat)
    cv2.imwrite("blackhat_image.jpg", blackhat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
