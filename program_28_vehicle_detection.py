"""
EXPERIMENT 28
Title: Vehicle Detection in Video
Aim: To implement a vehicle detection algorithm using OpenCV to detect and locate vehicles in each frame of a video.
"""

import cv2
import os

def detect_vehicles(video_path="sample_exp28_traffic.mp4"):
    if not os.path.exists(video_path):
        video_path = "traffic_video.mp4"
        if not os.path.exists(video_path):
            video_path = "video.mp4"

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Check for cascade file
    has_cascade = hasattr(cv2, 'CascadeClassifier') and (os.path.exists('cars.xml') or os.path.exists('haarcascades/cars.xml'))
    if has_cascade:
        cascade_file = 'cars.xml' if os.path.exists('cars.xml') else 'haarcascades/cars.xml'
        vehicle_cascade = cv2.CascadeClassifier(cascade_file)

    # Background subtractor for robust moving vehicle detection
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=25)

    print("Playing Vehicle Detection. Press 'q' to stop.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected = False

        if has_cascade:
            vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
            if len(vehicles) > 0:
                for (x, y, w, h) in vehicles:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, "Vehicle", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                detected = True

        if not detected:
            fg_mask = bg_subtractor.apply(frame)
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                if cv2.contourArea(cnt) > 400:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, "Vehicle", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    src_video = "sample_exp28_traffic.mp4" if os.path.exists("sample_exp28_traffic.mp4") else "traffic_video.mp4"
    detect_vehicles(src_video)
