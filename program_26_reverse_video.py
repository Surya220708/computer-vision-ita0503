"""
EXPERIMENT 26
Title: Reverse Frames of Video
Aim: To implement a function using OpenCV that reads a video, reverses its frames, and saves the reversed video.
"""

import cv2
import os

def reverse_video(input_video_path, output_video_path):
    if not os.path.exists(input_video_path):
        input_video_path = "sample_exp26_reverse.mp4"
        if not os.path.exists(input_video_path):
            input_video_path = "input_video.mp4"
            if not os.path.exists(input_video_path):
                input_video_path = "video.mp4"

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {input_video_path}")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps <= 0:
        fps = 20

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

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
    print(f"Reversed video successfully saved as: {output_video_path}")

if __name__ == "__main__":
    src_video = "sample_exp26_reverse.mp4" if os.path.exists("sample_exp26_reverse.mp4") else "input_video.mp4"
    reverse_video(src_video, "output_reversed.mp4")
