"""
EXPERIMENT 39
Title: Play Video in Reverse Mode in Slow Motion
Aim: To write a Python function to play a given video in reverse mode in slow motion using OpenCV.
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


def play_video_reverse_slow(video_path="sample_exp39_slow_reverse.mp4"):
    video_file = resolve_path(video_path)
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_file}")
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
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    play_video_reverse_slow()
