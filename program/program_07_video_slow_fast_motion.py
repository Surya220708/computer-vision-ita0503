"""
EXPERIMENT 7
Title: Video Display in Slow Motion and Fast Motion
Aim: To read a captured video in Python and display it in slow motion and fast motion using OpenCV.
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


video_path = resolve_path("video.mp4")
if not os.path.exists(video_path):
    video_path = resolve_path("input_video.mp4")

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
else:
    print("Playing video. Press 'q' to quit.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video Playback", frame)
        # 10ms for fast motion, 100ms for slow motion
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
