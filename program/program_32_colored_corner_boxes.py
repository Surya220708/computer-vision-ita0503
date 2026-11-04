"""
EXPERIMENT 32
Title: Canvas with Four Colored Corner Boxes
Aim: To create a white image of user-specified size and draw 4 boxes of Black, Blue, Green, and Red at each corner (size: 1/10th of image).
"""

import numpy as np
import cv2
import os

def resolve_path(filename):
    """Find file in current dir, parent dir, input dir, or script dir."""
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else "."
    search_paths = [
        filename,
        os.path.join("input", filename),
        os.path.join("..", "input", filename),
        os.path.join(base_dir, "..", "input", filename),
        os.path.join(base_dir, "input", filename),
        os.path.join("..", filename),
        os.path.join(base_dir, "..", filename),
        os.path.join(base_dir, filename),
    ]
    for p in search_paths:
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


def create_colored_corner_boxes(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    box_h = max(1, height // 10)
    box_w = max(1, width // 10)
    image[:box_h, :box_w] = [0, 0, 0]        # Top-left: Black
    image[:box_h, -box_w:] = [255, 0, 0]     # Top-right: Blue
    image[-box_h:, :box_w] = [0, 255, 0]     # Bottom-left: Green
    image[-box_h:, -box_w:] = [0, 0, 255]    # Bottom-right: Red

    cv2.imshow("Colored Corners Image", image)
    cv2.imwrite(get_output_path("colored_corners.jpg"), image)
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
