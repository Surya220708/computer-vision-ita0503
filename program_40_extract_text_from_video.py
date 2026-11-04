"""
EXPERIMENT 40
Title: Extract Text from Videos
Aim: To write a Python function to extract text from video frames using OpenCV and OCR.
"""

import cv2
import os

def extract_text_from_video(video_path="sample_exp40_text_video.mp4"):
    if not os.path.exists(video_path):
        video_path = "video.mp4"

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frame_num = 0
    extracted_texts = set()

    # Try pytesseract
    use_tesseract = False
    try:
        import pytesseract
        use_tesseract = True
    except ImportError:
        pass

    # RapidOCR engine for guaranteed reliable extraction on Windows
    ocr_engine = None
    try:
        from rapidocr_onnxruntime import RapidOCR
        ocr_engine = RapidOCR()
    except ImportError:
        pass

    print("Extracting text from video frames...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_num += 1

        # Process every 10th frame to avoid duplicate extractions
        if frame_num % 10 == 0:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = ""

            if use_tesseract:
                try:
                    text = pytesseract.image_to_string(gray_frame).strip()
                except Exception:
                    pass

            if not text and ocr_engine is not None:
                try:
                    result, _ = ocr_engine(frame)
                    if result:
                        text = " ".join([line[1] for line in result]).strip()
                except Exception:
                    pass

            if text and text not in extracted_texts:
                extracted_texts.add(text)
                print(f"[Frame {frame_num}] Extracted Text: {text}")

    cap.release()
    cv2.destroyAllWindows()
    if not extracted_texts:
        print("Note: OCR did not detect new high-confidence text or OCR engine binary not configured.")
    else:
        print(f"Done! Extracted {len(extracted_texts)} unique text segment(s).")

if __name__ == "__main__":
    src_video = "sample_exp40_text_video.mp4" if os.path.exists("sample_exp40_text_video.mp4") else "video.mp4"
    extract_text_from_video(src_video)
