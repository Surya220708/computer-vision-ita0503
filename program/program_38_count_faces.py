"""
EXPERIMENT 38
Title: Count Number of Faces
Aim: To count the number of faces in a given input image using OpenCV.
"""

import cv2
import os

def resolve_path(filename):
    """Find file in current dir, parent dir, input dir, or script dir."""
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else "."
    search_paths = [
        filename,
        os.path.join("input", filename),
        os.path.join("..", "input", filename),
        os.path.join(base_dir, "..", "input", filename),
        os.path.join(base_dir, "input", filename),
        os.path.join("..", filename),
        os.path.join(base_dir, "..", filename),
        os.path.join(base_dir, filename),
    ]
    for p in search_paths:
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


def count_faces(image_path="sample_exp38_face_count.jpg"):
    image_file = resolve_path(image_path)
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Could not load image {image_file}")
        return 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = []

    cascade_file = resolve_path("haarcascades/haarcascade_frontalface_default.xml")
    if hasattr(cv2, 'CascadeClassifier') and os.path.exists(cascade_file):
        face_cascade = cv2.CascadeClassifier(cascade_file)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    yunet_model = resolve_path("yunet.onnx")
    if len(faces) == 0 and hasattr(cv2, 'FaceDetectorYN_create') and os.path.exists(yunet_model):
        h, w = image.shape[:2]
        detector = cv2.FaceDetectorYN_create(yunet_model, "", (w, h), score_threshold=0.3, nms_threshold=0.3)
        _, raw_faces = detector.detect(image)
        if raw_faces is not None:
            faces = [f[:4].astype(int) for f in raw_faces]

    face_count = len(faces)
    print(f"Number of faces detected: {face_count}")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.rectangle(image, (15, 10), (320, 60), (0, 0, 0), -1)
    cv2.putText(image, f"Total Faces: {face_count}", (25, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    cv2.imshow("Face Count Detection", image)
    cv2.imwrite(get_output_path("counted_faces.jpg"), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return face_count

if __name__ == "__main__":
    count_faces()
