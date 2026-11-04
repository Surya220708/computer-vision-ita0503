"""
EXPERIMENT 14
Title: Perspective Transformation
Aim: To perform Perspective Transformation on the given image using Python and OpenCV.
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


image_path = resolve_path("sample_exp14_perspective.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("input.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    rows, cols, ch = image.shape
    pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
    pts2 = np.float32([[10, 80], [cols - 80, 20], [80, rows - 20], [cols - 20, rows - 80]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed_image)
    cv2.imwrite(get_output_path("perspective_transformed.jpg"), transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
