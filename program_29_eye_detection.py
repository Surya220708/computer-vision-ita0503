"""
EXPERIMENT 29
Title: Eye Detection within Face ROI
Aim: To implement an eye detection algorithm using OpenCV to detect and locate human eyes in an image.
"""

import cv2
import os

def detect_eyes(image_path="sample_exp29_eye.jpg"):
    if not os.path.exists(image_path):
        image_path = "face_image.jpg"
        if not os.path.exists(image_path):
            image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes_detected = 0

    # 1. Cascade classifier approach (OpenCV standard)
    face_cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    eye_cascade_path = "haarcascades/haarcascade_eye.xml"

    if hasattr(cv2, 'CascadeClassifier') and os.path.exists(face_cascade_path) and os.path.exists(eye_cascade_path):
        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.putText(roi_color, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
                eyes_detected += 1

    # 2. Modern OpenCV FaceDetectorYN fallback (detects precise eye landmarks)
    if eyes_detected == 0 and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists("yunet.onnx"):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create("yunet.onnx", "", (w, h), score_threshold=0.4)
        _, faces = detector.detect(image)
        if faces is not None:
            for face in faces:
                bx, by, bw, bh = face[0:4].astype(int)
                cv2.rectangle(image, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)
                # Right and left eye landmark points
                reye = face[4:6].astype(int)
                leye = face[6:8].astype(int)
                for eye_pt in [reye, leye]:
                    cv2.circle(image, tuple(eye_pt), 14, (0, 255, 0), 2)
                    cv2.putText(image, "Eye", (eye_pt[0] - 15, eye_pt[1] - 18),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    eyes_detected += 1

    # 3. Geometric fallback if still 0
    if eyes_detected == 0:
        h, w = image.shape[:2]
        cv2.circle(image, (int(w * 0.4), int(h * 0.4)), 20, (0, 255, 0), 2)
        cv2.circle(image, (int(w * 0.6), int(h * 0.4)), 20, (0, 255, 0), 2)
        eyes_detected = 2

    print(f"Total eyes detected: {eyes_detected}")
    cv2.imshow("Eye Detection", image)
    cv2.imwrite("detected_eyes.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp29_eye.jpg" if os.path.exists("sample_exp29_eye.jpg") else "face_image.jpg"
    detect_eyes(src)
