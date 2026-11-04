"""
EXPERIMENT 31
Title: Image Segmentation based on Thresholding
Aim: To implement a segmentation algorithm using OpenCV to segment the given input image based on specified threshold values.
"""

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


def segment_image(image_path="sample_exp31_segment.jpg", threshold_value=127):
    image_file = resolve_path(image_path)
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Could not load image {image_file}")
        return

    _, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow(f"Segmented Image (Threshold = {threshold_value})", segmented_image)
    cv2.imwrite(get_output_path("segmented_image.jpg"), segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    segment_image()
