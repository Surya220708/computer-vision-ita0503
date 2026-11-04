"""
EXPERIMENT 37
Title: Subtract Foreground Based on Color Levels
Aim: To remove the foreground of an input image based on color levels using OpenCV.
"""

import cv2
import numpy as np
import os

def subtract_foreground(image_path="sample_exp37_fg_sub.jpg", lower_color=(15, 80, 80), upper_color=(35, 255, 255)):
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color bounds for foreground object
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask for foreground
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert mask to retain only background
    mask_inv = cv2.bitwise_not(mask)
    background = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Mask", mask)
    cv2.imshow("Foreground Subtracted (Background Retained)", background)
    cv2.imwrite("fg_subtracted.jpg", background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp37_fg_sub.jpg" if os.path.exists("sample_exp37_fg_sub.jpg") else "sample.jpg"
    subtract_foreground(src)
