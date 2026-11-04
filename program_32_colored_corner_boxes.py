"""
EXPERIMENT 32
Title: Canvas with Four Colored Corner Boxes
Aim: To create a white image of user-specified size and draw 4 boxes of Black, Blue, Green, and Red at each corner (size: 1/10th of image).
"""

import numpy as np
import cv2

def create_colored_corner_boxes(image_size=(400, 500)):
    height, width = image_size

    # Create a white canvas (3D array of ones scaled to 255 for BGR)
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Size of each colored corner box is 1/10th of image dimensions
    box_h = max(1, height // 10)
    box_w = max(1, width // 10)

    # Fill corner boxes in BGR format:
    image[:box_h, :box_w] = [0, 0, 0]        # Top-left: Black
    image[:box_h, -box_w:] = [255, 0, 0]     # Top-right: Blue
    image[-box_h:, :box_w] = [0, 255, 0]     # Bottom-left: Green
    image[-box_h:, -box_w:] = [0, 0, 255]    # Bottom-right: Red

    cv2.imshow("Colored Corners Image", image)
    cv2.imwrite("colored_corners.jpg", image)
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

    create_colored_corner_boxes((user_height, user_width))
