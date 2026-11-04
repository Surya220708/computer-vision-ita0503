"""
EXPERIMENT 20
Title: Morphological Dilation Technique
Aim: To implement the Dilation technique as a Morphological operation to dilate foreground regions based on OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp20_dilation.jpg"
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

    # Apply morphological dilation
    dilated = cv2.dilate(binary, kernel, iterations=1)

    cv2.imshow("Original Binary Image", binary)
    cv2.imshow("Morphological Dilation", dilated)
    cv2.imwrite("morph_dilation.jpg", dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
