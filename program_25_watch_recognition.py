"""
EXPERIMENT 25
Title: Recognize Watch from Image by Object Recognition
Aim: To recognize a watch in a given image using general object recognition techniques in OpenCV.
"""

import cv2
import numpy as np
import os

image_path = "sample_exp25_watch.jpg"
if not os.path.exists(image_path):
    image_path = "watch.jpg"
    if not os.path.exists(image_path):
        image_path = "sample.jpg"

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected = False

    # Check if a custom watch cascade exists
    if hasattr(cv2, 'CascadeClassifier') and os.path.exists("watch_cascade.xml"):
        watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")
        watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in watches:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Watch", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            detected = True

    # General Object Recognition fallback (Hough Circles for circular watch dial)
    if not detected:
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                                   param1=50, param2=30, minRadius=20, maxRadius=250)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            best_circle = circles[0, 0] # primary detected circle
            cx, cy, r = best_circle[0], best_circle[1], best_circle[2]
            cv2.circle(image, (cx, cy), r, (0, 255, 0), 3)
            cv2.putText(image, "Watch Dial Detected", (cx - 70, cy - r - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            edges = cv2.Canny(gray, 50, 150)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                if cv2.contourArea(cnt) > 1000:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(image, "Object/Watch", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    break

    cv2.imshow("Detected Watch / Object Recognition", image)
    cv2.imwrite("detected_watch.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
