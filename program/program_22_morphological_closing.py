"""
EXPERIMENT 22
Title: Morphological Closing Technique
Aim: To implement the Closing technique as a Morphological operation using OpenCV in Python.
"""

import cv2
import numpy as np
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


image_path = resolve_path("sample_exp22_closing.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("image.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    closed_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Closed Image", closed_image)
    cv2.imwrite(get_output_path("closed_image.jpg"), closed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
