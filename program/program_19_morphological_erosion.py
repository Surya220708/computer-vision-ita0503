"""
EXPERIMENT 19
Title: Morphological Erosion Technique
Aim: To implement the Erosion Morphological operation using OpenCV in Python.
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


image_path = resolve_path("sample_exp19_erosion.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("image.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(binary, kernel, iterations=1)
    cv2.imshow("Original Binary Image", binary)
    cv2.imshow("Morphological Erosion", eroded)
    cv2.imwrite(get_output_path("morph_erosion.jpg"), eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
