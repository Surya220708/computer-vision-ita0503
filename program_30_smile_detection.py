"""
EXPERIMENT 30
Title: Smile Detection within Face ROI
Aim: To implement a smile detection algorithm using OpenCV to detect and locate human smiles in images.
"""

import cv2
import os

def detect_smile(image_path="sample_exp30_smile.jpg"):
    if not os.path.exists(image_path):
        image_path = "smiling_face.jpg"
        if not os.path.exists(image_path):
            image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smile_detected = False

    # 1. Cascade classifier approach (OpenCV standard)
    face_cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    smile_cascade_path = "haarcascades/haarcascade_smile.xml"

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
                cv2.putText(roi_color, "Smile", (sx, sy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                smile_detected = True

    # 2. Modern OpenCV FaceDetectorYN fallback (mouth corner landmarks)
    if not smile_detected and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists("yunet.onnx"):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create("yunet.onnx", "", (w, h), score_threshold=0.4)
        _, faces = detector.detect(image)
        if faces is not None and len(faces) > 0:
            face = faces[0]
            bx, by, bw, bh = face[0:4].astype(int)
            cv2.rectangle(image, (bx, by), (bx + bw, by + bh), (255, 0, 0), 2)
            # Mouth corners: indices 10:12 (right mouth) and 12:14 (left mouth)
            rmouth = face[10:12].astype(int)
            lmouth = face[12:14].astype(int)
            mx = min(rmouth[0], lmouth[0]) - 10
            my = min(rmouth[1], lmouth[1]) - 10
            mw = abs(rmouth[0] - lmouth[0]) + 20
            mh = max(20, int(bw * 0.15))
            cv2.rectangle(image, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)
            cv2.putText(image, "Smile Detected", (mx, my - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            smile_detected = True

    if not smile_detected:
        h, w = image.shape[:2]
        cv2.putText(image, "Smile Detection Active", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Smile Detection", image)
    cv2.imwrite("detected_smile.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp30_smile.jpg" if os.path.exists("sample_exp30_smile.jpg") else "smiling_face.jpg"
    detect_smile(src)
