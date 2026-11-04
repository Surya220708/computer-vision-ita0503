"""
EXPERIMENT 34
Title: Draw Circle on White Canvas
Aim: To write a Python function to create a white image of user-entered size and draw a circle using OpenCV.
"""

import numpy as np
import cv2
import os

def resolve_path(filename):
    """Find file in current dir, parent dir, or script dir."""
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else "."
    for p in [filename, os.path.join("..", filename),
             os.path.join(base_dir, "..", filename),
             os.path.join(base_dir, filename)]:
        if os.path.exists(p):
            return p
    return filename

def get_output_path(filename):
    """Return path inside output folder if available."""
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else "."
    for d in ["output", os.path.join("..", "output"),
             os.path.join(base_dir, "..", "output")]:
        if os.path.isdir(d):
            return os.path.join(d, filename)
    return filename


def create_circle_image(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    cv2.circle(image, center, radius, (0, 0, 255), 2)
    cv2.imshow("Circle Image", image)
    cv2.imwrite(get_output_path("circle_image.jpg"), image)
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
