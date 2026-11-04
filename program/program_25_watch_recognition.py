"""
EXPERIMENT 25
Title: Recognize Watch from Image by Object Recognition
Aim: To recognize a watch in a given image using general object recognition techniques in OpenCV.
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


image_path = resolve_path("sample_exp25_watch.jpg")
if not os.path.exists(image_path):
    image_path = resolve_path("watch.jpg")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected = False

    cascade_file = resolve_path("watch_cascade.xml")
    if hasattr(cv2, 'CascadeClassifier') and os.path.exists(cascade_file):
        watch_cascade = cv2.CascadeClassifier(cascade_file)
        watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in watches:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Watch", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            detected = True

    if not detected:
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                   param1=50, param2=30, minRadius=20, maxRadius=250)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            best_circle = circles[0, 0]
            cx, cy, r = best_circle[0], best_circle[1], best_circle[2]
            cv2.circle(image, (cx, cy), r, (0, 255, 0), 3)
            cv2.putText(image, "Watch Dial Detected", (cx - 70, cy - r - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Detected Watch / Object Recognition", image)
    cv2.imwrite(get_output_path("detected_watch.jpg"), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
