"""
EXPERIMENT 33
Title: Draw Rectangle on White Canvas
Aim: To write a Python function to create a white image of user-entered size and draw a rectangle using OpenCV.
"""

import numpy as np
import cv2

def create_rectangle_image(image_size=(400, 500)):
    height, width = image_size

    # Create white canvas
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Coordinates for centered rectangle
    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)

    # Draw rectangle (Color: Blue [255, 0, 0], Thickness: 2)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

    cv2.imshow("Rectangle Image", image)
    cv2.imwrite("rectangle_image.jpg", image)
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

    create_rectangle_image((user_height, user_width))
