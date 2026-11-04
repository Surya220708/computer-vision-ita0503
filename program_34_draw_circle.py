"""
EXPERIMENT 34
Title: Draw Circle on White Canvas
Aim: To write a Python function to create a white image of user-entered size and draw a circle using OpenCV.
"""

import numpy as np
import cv2

def create_circle_image(image_size=(400, 500)):
    height, width = image_size

    # Create white canvas
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define circle center and radius
    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    # Draw circle (Color: Red [0, 0, 255], Thickness: 2)
    cv2.circle(image, center, radius, (0, 0, 255), 2)

    cv2.imshow("Circle Image", image)
    cv2.imwrite("circle_image.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        w_in = input("Enter image width (press Enter for default 500): ").strip()
        h_in = input("Enter image height (press Enter for default 400): ").strip()
        user_width = int(w_in) if w_in else 500
        user_height = int(h_in) if h_in else 400
    except Exception:
        user_width, user_height = 500, 400

    create_circle_image((user_height, user_width))
