"""
EXPERIMENT 11
Title: 180-degree Rotation Clockwise Along Y-Axis
Aim: To perform a 180-degree rotation clockwise along the Y-axis for the given image using OpenCV in Python.
"""

import cv2
import os

image_path = "sample_exp11_rotate180.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Flip along the Y-axis (flip code = 1 mirrors along Y-axis)
    flipped_image = cv2.flip(image, 1)

    # Rotate 180 degrees
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_180)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 180-degree Clockwise Along Y-axis", rotated_image)
    cv2.imwrite("rotated_image_180.jpg", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
