"""
EXPERIMENT 27
Title: Human Face Detection
Aim: To implement a face detection algorithm using OpenCV to detect and locate human faces in images.
"""

import cv2
import os

def detect_faces(image_path="sample_exp27_face.jpg"):
    if not os.path.exists(image_path):
        image_path = "face_image.jpg"
        if not os.path.exists(image_path):
            image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = []

    # 1. Cascade classifier approach (OpenCV standard)
    cascade_paths = [
        "haarcascades/haarcascade_frontalface_default.xml",
        os.path.join(getattr(cv2, 'data', None).haarcascades if hasattr(cv2, 'data') else '', 'haarcascade_frontalface_default.xml'),
        "haarcascade_frontalface_default.xml"
    ]
    cascade_file = next((p for p in cascade_paths if os.path.exists(p)), None)

    if hasattr(cv2, 'CascadeClassifier') and cascade_file:
        face_cascade = cv2.CascadeClassifier(cascade_file)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 2. Modern OpenCV FaceDetectorYN fallback (if CascadeClassifier is absent)
    if len(faces) == 0 and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists("yunet.onnx"):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create("yunet.onnx", "", (w, h), score_threshold=0.4)
        _, raw_faces = detector.detect(image)
        if raw_faces is not None:
            faces = [f[:4].astype(int) for f in raw_faces]

    # 3. Contour/skin-color fallback
    if len(faces) == 0:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0, 30, 60), (20, 150, 255))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > 2000:
                faces = [cv2.boundingRect(cnt)]
                break

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    print(f"Detected {len(faces)} face(s).")
    cv2.imshow("Face Detection", image)
    cv2.imwrite("detected_faces.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src = "sample_exp27_face.jpg" if os.path.exists("sample_exp27_face.jpg") else "face_image.jpg"
    detect_faces(src)
