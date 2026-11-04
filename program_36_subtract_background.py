"""
EXPERIMENT 36
Title: Subtract Background Based on Color Levels
Aim: To subtract the background of a given input image based on color levels using OpenCV.
"""

import cv2
import numpy as np
import os

def subtract_background(image_path="sample_exp36_bg_sub.jpg", lower_color=(0, 0, 180), upper_color=(180, 50, 255)):
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color bounds for background
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask for background color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert mask to keep the foreground
    mask_inv = cv2.bitwise_not(mask)

    # Extract foreground
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Background Mask", mask)
    cv2.imshow("Background Subtracted (Foreground Retained)", foreground)
    cv2.imwrite("bg_subtracted.jpg", foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp36_bg_sub.jpg" if os.path.exists("sample_exp36_bg_sub.jpg") else "sample.jpg"
    subtract_background(src)
