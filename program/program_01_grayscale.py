"""
EXPERIMENT 1
Title: Convert an Image to Grayscale
Aim: To read an image and convert it to grayscale using OpenCV in Python.
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
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
