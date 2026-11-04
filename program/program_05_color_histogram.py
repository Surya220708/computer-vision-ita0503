"""
EXPERIMENT 5
Title: Analyze Histogram of Image based on Color Levels
Aim: To write a Python function to analyze the histogram of a given input image based on color levels using OpenCV.
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


image_path = resolve_path("sample.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("image.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    hist_canvas = np.ones((400, 500, 3), dtype=np.uint8) * 255
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, 350, cv2.NORM_MINMAX)
        pts = np.int32(np.column_stack((np.linspace(20, 480, 256), 380 - hist.flatten())))
        bgr = (255, 0, 0) if col == 'b' else ((0, 255, 0) if col == 'g' else (0, 0, 255))
        cv2.polylines(hist_canvas, [pts], False, bgr, 2)
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Histogram Distribution", hist_canvas)
    cv2.imwrite(get_output_path("color_histogram.jpg"), hist_canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
