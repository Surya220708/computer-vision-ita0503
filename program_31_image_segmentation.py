"""
EXPERIMENT 31
Title: Image Segmentation based on Thresholding
Aim: To implement a segmentation algorithm using OpenCV to segment the given input image based on specified threshold values.
"""

import cv2
import os

def segment_image(image_path="sample_exp31_segment.jpg", threshold_value=127):
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

    # Read image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    # Apply binary thresholding for segmentation
    _, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display original and segmented images
    cv2.imshow("Original Grayscale Image", image)
    cv2.imshow(f"Segmented Image (Threshold = {threshold_value})", segmented_image)
    cv2.imwrite("segmented_image.jpg", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp31_segment.jpg" if os.path.exists("sample_exp31_segment.jpg") else "sample.jpg"
    segment_image(src, threshold_value=127)
