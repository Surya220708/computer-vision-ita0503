"""
EXPERIMENT 9
Title: Image Scaling (Bigger and Smaller)
Aim: To implement image scaling techniques to resize images to both bigger and smaller sizes using OpenCV.
"""

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


image_path = resolve_path("sample.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("image.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    smaller = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image (1.5x)", bigger)
    cv2.imshow("Smaller Image (0.5x)", smaller)
    cv2.imwrite(get_output_path("scaled_bigger.jpg"), bigger)
    cv2.imwrite(get_output_path("scaled_smaller.jpg"), smaller)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
