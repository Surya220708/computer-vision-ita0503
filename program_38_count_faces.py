"""
EXPERIMENT 38
Title: Count Number of Faces
Aim: To count the number of faces in a given input image using OpenCV.
"""

import cv2
import os

def count_faces(image_path="sample_exp38_face_count.jpg"):
    if not os.path.exists(image_path):
        image_path = "face_image.jpg"
        if not os.path.exists(image_path):
            image_path = "sample.jpg"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = []

    # 1. Cascade classifier approach (OpenCV standard)
    cascade_file = "haarcascades/haarcascade_frontalface_default.xml"
    if hasattr(cv2, 'CascadeClassifier') and os.path.exists(cascade_file):
        face_cascade = cv2.CascadeClassifier(cascade_file)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    # 2. Modern OpenCV FaceDetectorYN fallback
    if len(faces) == 0 and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists("yunet.onnx"):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create("yunet.onnx", "", (w, h), score_threshold=0.3, nms_threshold=0.3)
        _, raw_faces = detector.detect(image)
        if raw_faces is not None:
            faces = [f[:4].astype(int) for f in raw_faces]

    # 3. Fallback skin-region face detection
    if len(faces) == 0:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (0, 30, 60), (20, 150, 255))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > 2000:
                faces.append(cv2.boundingRect(cnt))

    face_count = len(faces)
    print(f"Number of faces detected: {face_count}")

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display count banner on the image
    cv2.rectangle(image, (15, 10), (320, 60), (0, 0, 0), -1)
    cv2.putText(image, f"Total Faces: {face_count}", (25, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    cv2.imshow("Face Count Detection", image)
    cv2.imwrite("counted_faces.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return face_count

if __name__ == "__main__":
    src = "sample_exp38_face_count.jpg" if os.path.exists("sample_exp38_face_count.jpg") else "face_image.jpg"
    count_faces(src)
