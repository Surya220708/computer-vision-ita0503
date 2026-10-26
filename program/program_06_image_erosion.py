"""
EXPERIMENT 6
Title: Image Erosion using Erode Function
Aim: To perform morphological erosion on an image using the cv2.erode function in OpenCV.
Note: Corrects the copy-paste placeholder in the lab manual.
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
    # Define a 5x5 rectangular structuring element kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display original and eroded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
