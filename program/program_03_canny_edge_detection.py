"""
EXPERIMENT 3
Title: Convert an Image to Show Outline using Canny Edge Detection
Aim: To read an image and apply edge detection using the Canny function in OpenCV.
"""

import cv2
import os

image_path = "sample.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detector (thresholds: 100, 200)
    edges = cv2.Canny(gray_image, 100, 200)

    # Display original and edge detected images
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detected Image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
