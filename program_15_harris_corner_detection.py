"""
EXPERIMENT 15
Title: Harris Corner Detection
Aim: To detect corners in an image using the Harris Corner Detection algorithm in OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp15_harris.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    output_image = image.copy()

    # Convert image to grayscale and float32
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Dilate corner points for better visibility
    harris_corners = cv2.dilate(harris_corners, None)

    # Mark detected corners in red [BGR: (0, 0, 255)]
    output_image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

    cv2.imshow("Original Image", image)
    cv2.imshow("Harris Corner Detection", output_image)
    cv2.imwrite("harris_corners.jpg", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
