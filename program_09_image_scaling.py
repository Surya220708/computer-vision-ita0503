"""
EXPERIMENT 9
Title: Image Scaling (Bigger and Smaller)
Aim: To implement image scaling techniques to resize images to both bigger and smaller sizes using OpenCV.
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
    # Resize to a bigger size (2x scaling)
    bigger_image = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

    # Resize to a smaller size (0.5x scaling)
    smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image (2x Scaling)", bigger_image)
    cv2.imshow("Smaller Image (0.5x Scaling)", smaller_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
