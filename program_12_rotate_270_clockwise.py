"""
EXPERIMENT 12
Title: 270-degree Rotation Clockwise Along Y-Axis
Aim: To perform a 270-degree rotation clockwise along the Y-axis for the given image using OpenCV in Python.
"""

import cv2
import os

image_path = "sample_exp12_rotate270.jpg"
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

    # 270 deg clockwise rotation is equivalent to 90 deg counter-clockwise
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 270-degree Clockwise Along Y-axis", rotated_image)
    cv2.imwrite("rotated_image_270.jpg", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
