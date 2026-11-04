"""
EXPERIMENT 36
Title: Subtract Background Based on Color Levels
Aim: To subtract the background of a given input image based on color levels using OpenCV.
"""

import cv2
import numpy as np
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


def subtract_background(image_path="sample_exp36_bg_sub.jpg", lower_color=(0, 0, 160), upper_color=(180, 60, 255)):
    image_file = resolve_path(image_path)
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Could not load image {image_file}")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted (Foreground Retained)", foreground)
    cv2.imwrite(get_output_path("bg_subtracted.jpg"), foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    subtract_background()
