"""
EXPERIMENT 10
Title: 90-degree Rotation Clockwise Along Y-Axis
Aim: To perform a 90-degree rotation clockwise along the Y-axis for the given image.
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
    flipped_image = cv2.flip(image, 1)
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 90-degree Clockwise Along Y-axis", rotated_image)
    cv2.imwrite(get_output_path("rotated_90.jpg"), rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
