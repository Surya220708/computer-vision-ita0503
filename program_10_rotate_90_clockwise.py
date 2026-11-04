"""
EXPERIMENT 10
Title: 90-degree Rotation Clockwise Along Y-Axis
Aim: To perform a 90-degree rotation clockwise along the Y-axis for the given image using OpenCV.
"""

import cv2
import os

image_path = "input.jpg"
if not os.path.exists(image_path):
    image_path = "sample.jpg"

img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Rotate 90 degrees clockwise
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display results
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated 90 Degrees Clockwise", rotated_img)
    cv2.imwrite("rotated_90.jpg", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
