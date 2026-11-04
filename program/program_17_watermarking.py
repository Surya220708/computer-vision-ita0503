"""
EXPERIMENT 17
Title: Image Watermarking Technique
Aim: To design and implement a watermarking technique to insert a watermark into the original image using OpenCV.
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


image_path = resolve_path("sample_exp17_watermark.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("image.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    h, w = image.shape[:2]
    watermarked = image.copy()
    overlay = image.copy()
    banner_h = max(50, int(h * 0.12))
    cv2.rectangle(overlay, (0, h - banner_h), (w, h), (20, 20, 20), -1)
    text = "CONFIDENTIAL - CV LAB 2025"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = max(0.6, w / 1000.0)
    cv2.putText(overlay, text, (int(w * 0.05), h - int(banner_h * 0.35)),
                font, font_scale, (0, 220, 255), 2, cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.65, watermarked, 0.35, 0, watermarked)
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked)
    cv2.imwrite(get_output_path("watermarked_image.jpg"), watermarked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
