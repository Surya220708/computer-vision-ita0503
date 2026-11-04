"""
EXPERIMENT 29
Title: Eye Detection within Face ROI
Aim: To implement an eye detection algorithm using OpenCV to detect and locate human eyes in an image.
"""

import cv2
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


def detect_eyes(image_path="sample_exp29_eye.jpg"):
    image_file = resolve_path(image_path)
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Could not load image {image_file}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes_detected = 0

    face_cascade_path = resolve_path("haarcascades/haarcascade_frontalface_default.xml")
    eye_cascade_path = resolve_path("haarcascades/haarcascade_eye.xml")

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
                eyes_detected += 1

    yunet_model = resolve_path("yunet.onnx")
    if eyes_detected == 0 and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists(yunet_model):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create(yunet_model, "", (w, h), score_threshold=0.4)
        _, faces = detector.detect(image)
        if faces is not None:
            for face in faces:
                bx, by, bw, bh = face[0:4].astype(int)
                cv2.rectangle(image, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)
                reye = face[4:6].astype(int)
                leye = face[6:8].astype(int)
                for eye_pt in [reye, leye]:
                    cv2.circle(image, tuple(eye_pt), 14, (0, 255, 0), 2)
                    cv2.putText(image, "Eye", (eye_pt[0] - 15, eye_pt[1] - 18),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    eyes_detected += 1

    print(f"Total eyes detected: {eyes_detected}")
    cv2.imshow("Eye Detection", image)
    cv2.imwrite(get_output_path("detected_eyes.jpg"), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_eyes()
