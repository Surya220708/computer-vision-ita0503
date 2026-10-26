"""
EXPERIMENT 5
Title: Analyze the Histogram of an Input Image Based on Color Levels
Aim: To write a Python function to analyze and display the histogram of an image based on color levels using OpenCV.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def analyze_histogram(image_path):
    if not os.path.exists(image_path):
        image_path = "sample.jpg"
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    color_channels = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))

    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")
        plt.xlim([0, 256])

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

if __name__ == "__main__":
    analyze_histogram("sample.jpg")
