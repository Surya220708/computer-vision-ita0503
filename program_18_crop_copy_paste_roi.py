"""
EXPERIMENT 18
Title: Image Cropping, Copying and Pasting (Region of Interest - ROI)
Aim: To implement image cropping, copying, and pasting to select a region of interest (ROI) from the source image using OpenCV.
"""

import cv2
import os

image_path = "sample_exp18_roi.jpg"
if not os.path.exists(image_path):
    image_path = "image.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    h, w = image.shape[:2]
    # Define ROI bounding box (center region)
    y1, y2 = int(h * 0.25), int(h * 0.75)
    x1, x2 = int(w * 0.25), int(w * 0.75)

    # 1. Crop ROI
    roi = image[y1:y2, x1:x2].copy()

    # 2. Copy and Paste ROI into the top-left area
    result_image = image.copy()
    paste_y, paste_x = 10, 10
    roi_h, roi_w = roi.shape[:2]
    
    # Resize pasted ROI if needed to fit
    max_h = min(roi_h, h - paste_y - 10)
    max_w = min(roi_w, w - paste_x - 10)
    result_image[paste_y:paste_y + max_h, paste_x:paste_x + max_w] = roi[:max_h, :max_w]

    # Draw boxes: Green for original ROI, Red for pasted ROI
    cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(result_image, (paste_x, paste_y), (paste_x + max_w, paste_y + max_h), (0, 0, 255), 2)

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Pasted ROI Result", result_image)
    cv2.imwrite("roi_result.jpg", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
