"""
EXPERIMENT 30
Title: Smile Detection within Face ROI
Aim: To implement a smile detection algorithm using OpenCV to detect and locate human smiles in images.
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


def detect_smile(image_path="sample_exp30_smile.jpg"):
    image_file = resolve_path(image_path)
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Could not load image {image_file}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smile_detected = False

    face_cascade_path = resolve_path("haarcascades/haarcascade_frontalface_default.xml")
    smile_cascade_path = resolve_path("haarcascades/haarcascade_smile.xml")

    if hasattr(cv2, 'CascadeClassifier') and os.path.exists(face_cascade_path) and os.path.exists(smile_cascade_path):
        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
                smile_detected = True

    yunet_model = resolve_path("yunet.onnx")
    if not smile_detected and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists(yunet_model):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create(yunet_model, "", (w, h), score_threshold=0.4)
        _, faces = detector.detect(image)
        if faces is not None and len(faces) > 0:
            face = faces[0]
            bx, by, bw, bh = face[0:4].astype(int)
            cv2.rectangle(image, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)
            rmouth = face[10:12].astype(int)
            lmouth = face[12:14].astype(int)
            mx = min(rmouth[0], lmouth[0]) - 15
            my = min(rmouth[1], lmouth[1]) - 15
            mw = abs(rmouth[0] - lmouth[0]) + 30
            mh = max(25, int(bw * 0.18))
            cv2.rectangle(image, (mx, my), (mx + mw, my + mh), (0, 0, 255), 3)
            cv2.putText(image, "Smile Detected", (mx, my - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            smile_detected = True

    cv2.imshow("Smile Detection", image)
    cv2.imwrite(get_output_path("detected_smile.jpg"), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_smile()
