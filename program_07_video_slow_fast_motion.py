"""
EXPERIMENT 7
Title: Video Processing - Slow Motion and Fast Motion
Aim: To read a captured video in Python and display the video in slow motion and fast motion using OpenCV.
Note: Corrects the copy-paste placeholder in the lab manual.
"""

import cv2
import os

video_path = "video.mp4"
if not os.path.exists(video_path):
    video_path = "input_video.mp4"

def play_video(path, delay_ms, window_name):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    print(f"Playing {window_name} (delay: {delay_ms}ms per frame). Press 'q' to stop.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay_ms) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(window_name)

if __name__ == "__main__":
    print("--- 1. Displaying Video in Slow Motion (100 ms delay) ---")
    play_video(video_path, delay_ms=100, window_name="Slow Motion Video")

    print("--- 2. Displaying Video in Fast Motion (10 ms delay) ---")
    play_video(video_path, delay_ms=10, window_name="Fast Motion Video")
    cv2.destroyAllWindows()
