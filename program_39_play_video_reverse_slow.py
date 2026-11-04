"""
EXPERIMENT 39
Title: Play Video in Reverse Mode in Slow Motion
Aim: To write a Python function to play a given video in reverse mode in slow motion using OpenCV.
"""

import cv2
import os

def play_video_reverse_slow(video_path="sample_exp39_slow_reverse.mp4"):
    if not os.path.exists(video_path):
        video_path = "video.mp4"

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frames = []
    print("Reading video frames...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    print(f"Total {len(frames)} frames loaded. Playing in reverse in slow motion (100 ms delay). Press 'q' to stop.")
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion Video", frame)
        # 100 ms wait delay gives slow motion playback
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    src_video = "sample_exp39_slow_reverse.mp4" if os.path.exists("sample_exp39_slow_reverse.mp4") else "video.mp4"
    play_video_reverse_slow(src_video)
