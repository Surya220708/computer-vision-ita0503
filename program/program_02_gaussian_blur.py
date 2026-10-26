"""
EXPERIMENT 2
Title: Convert an Image to Blur using Gaussian Blur
Aim: To read an image and apply Gaussian Blur using OpenCV in Python.
"""

import cv2
import os

image_path = "sample.jpg"
if not os.path.exists("input_image.jpg"):
    image_path = "image.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Apply Gaussian Blur with a 15x15 kernel
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
