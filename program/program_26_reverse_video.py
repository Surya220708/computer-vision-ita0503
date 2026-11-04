"""
EXPERIMENT 26
Title: Reverse Frames of Video
Aim: To implement a function using OpenCV that reads a video, reverses its frames, and saves the reversed video.
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


def reverse_video(input_video_path, output_video_path):
    resolved_in = resolve_path(input_video_path)
    cap = cv2.VideoCapture(resolved_in)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {resolved_in}")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps <= 0:
        fps = 20

    out_file = get_output_path(output_video_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(out_file, fourcc, fps, (frame_width, frame_height))

    frames = []
    print("Reading frames...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    print(f"Total frames read: {len(frames)}. Reversing frames...")
    frames.reverse()

    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Reversed video successfully saved as: {out_file}")

if __name__ == "__main__":
    reverse_video("sample_exp26_reverse.mp4", "output_reversed.mp4")
