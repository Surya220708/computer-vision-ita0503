# Computer Vision Laboratory (ITA0503)

Comprehensive implementation and verified observation results for all 40 experiments of the **ITA05 - Computer Vision Laboratory** curriculum (Saveetha Engineering College).

---

## 📁 Repository Structure

The repository is cleanly organized with dedicated directories for programs and output screenshots:

```
computer-vision/
├── program/                 # Dedicated directory containing all 40 Python programs
│   ├── program_01_grayscale.py
│   ├── program_02_gaussian_blur.py
│   ├── ...
│   └── program_40_extract_text_from_video.py
├── output/                  # Dedicated directory containing all observation screenshot cards and outputs
│   ├── exp_01_result.png
│   ├── exp_02_result.png
│   ├── ...
│   ├── exp_40_result.png
│   └── index.html           # Interactive visual observation gallery
├── haarcascades/            # Pre-trained Haar Cascade XML classifiers
├── yunet.onnx               # High-precision YuNet face detector model
├── sample_exp*.jpg / .mp4   # Sourced thematic test images and video clips (Exp 11 - 40)
├── create_catalog.py        # Automated Markdown and HTML gallery generator
├── create_observation_results.py # Observation card generator
├── OBSERVATION_RESULTS.md   # Full documentation with embedded screenshot cards
└── README.md
```

---

## 🧪 Index of Experiments

| Exp No | Experiment Title | Python Program | Observation Screenshot |
|:---:|:---|:---|:---:|
| 01 | Convert Image to Grayscale | [`program/program_01_grayscale.py`](program/program_01_grayscale.py) | [`output/exp_01_result.png`](output/exp_01_result.png) |
| 02 | Convert Image to Blur using Gaussian Blur | [`program/program_02_gaussian_blur.py`](program/program_02_gaussian_blur.py) | [`output/exp_02_result.png`](output/exp_02_result.png) |
| 03 | Canny Edge Detection Outline | [`program/program_03_canny_edge_detection.py`](program/program_03_canny_edge_detection.py) | [`output/exp_03_result.png`](output/exp_03_result.png) |
| 04 | Histogram Equalization | [`program/program_04_histogram_equalization.py`](program/program_04_histogram_equalization.py) | [`output/exp_04_result.png`](output/exp_04_result.png) |
| 05 | Color Histogram Analysis | [`program/program_05_color_histogram.py`](program/program_05_color_histogram.py) | [`output/exp_05_result.png`](output/exp_05_result.png) |
| 06 | Image Erosion using Erode Function | [`program/program_06_image_erosion.py`](program/program_06_image_erosion.py) | [`output/exp_06_result.png`](output/exp_06_result.png) |
| 07 | Video Slow Motion & Fast Motion Playback | [`program/program_07_video_slow_fast_motion.py`](program/program_07_video_slow_fast_motion.py) | [`output/exp_07_result.png`](output/exp_07_result.png) |
| 08 | Image Dilation using Dilate Function | [`program/program_08_image_dilation.py`](program/program_08_image_dilation.py) | [`output/exp_08_result.png`](output/exp_08_result.png) |
| 09 | Image Scaling (2x Bigger and 0.5x Smaller) | [`program/program_09_image_scaling.py`](program/program_09_image_scaling.py) | [`output/exp_09_result.png`](output/exp_09_result.png) |
| 10 | 90-Degree Clockwise Rotation Along Y-Axis | [`program/program_10_rotate_90_clockwise.py`](program/program_10_rotate_90_clockwise.py) | [`output/exp_10_result.png`](output/exp_10_result.png) |
| 11 | 180-Degree Clockwise Rotation Along Y-Axis | [`program/program_11_rotate_180_clockwise.py`](program/program_11_rotate_180_clockwise.py) | [`output/exp_11_result.png`](output/exp_11_result.png) |
| 12 | 270-Degree Clockwise Rotation Along Y-Axis | [`program/program_12_rotate_270_clockwise.py`](program/program_12_rotate_270_clockwise.py) | [`output/exp_12_result.png`](output/exp_12_result.png) |
| 13 | Affine Transformation | [`program/program_13_affine_transformation.py`](program/program_13_affine_transformation.py) | [`output/exp_13_result.png`](output/exp_13_result.png) |
| 14 | Perspective Transformation | [`program/program_14_perspective_transformation.py`](program/program_14_perspective_transformation.py) | [`output/exp_14_result.png`](output/exp_14_result.png) |
| 15 | Harris Corner Detection | [`program/program_15_harris_corner_detection.py`](program/program_15_harris_corner_detection.py) | [`output/exp_15_result.png`](output/exp_15_result.png) |
| 16 | Sobel Edge Detection Filter | [`program/program_16_sobel_edge_detection.py`](program/program_16_sobel_edge_detection.py) | [`output/exp_16_result.png`](output/exp_16_result.png) |
| 17 | Image Watermarking Technique | [`program/program_17_watermarking.py`](program/program_17_watermarking.py) | [`output/exp_17_result.png`](output/exp_17_result.png) |
| 18 | Image Cropping, Copying & Pasting ROI | [`program/program_18_crop_copy_paste_roi.py`](program/program_18_crop_copy_paste_roi.py) | [`output/exp_18_result.png`](output/exp_18_result.png) |
| 19 | Morphological Erosion Technique | [`program/program_19_morphological_erosion.py`](program/program_19_morphological_erosion.py) | [`output/exp_19_result.png`](output/exp_19_result.png) |
| 20 | Morphological Dilation Technique | [`program/program_20_morphological_dilation.py`](program/program_20_morphological_dilation.py) | [`output/exp_20_result.png`](output/exp_20_result.png) |
| 21 | Morphological Opening Technique | [`program/program_21_morphological_opening.py`](program/program_21_morphological_opening.py) | [`output/exp_21_result.png`](output/exp_21_result.png) |
| 22 | Morphological Closing Technique | [`program/program_22_morphological_closing.py`](program/program_22_morphological_closing.py) | [`output/exp_22_result.png`](output/exp_22_result.png) |
| 23 | Morphological Top Hat Technique | [`program/program_23_morphological_tophat.py`](program/program_23_morphological_tophat.py) | [`output/exp_23_result.png`](output/exp_23_result.png) |
| 24 | Morphological Black Hat Technique | [`program/program_24_morphological_blackhat.py`](program/program_24_morphological_blackhat.py) | [`output/exp_24_result.png`](output/exp_24_result.png) |
| 25 | Watch Object Recognition | [`program/program_25_watch_recognition.py`](program/program_25_watch_recognition.py) | [`output/exp_25_result.png`](output/exp_25_result.png) |
| 26 | Reverse Frames of Video | [`program/program_26_reverse_video.py`](program/program_26_reverse_video.py) | [`output/exp_26_result.png`](output/exp_26_result.png) |
| 27 | Human Face Detection | [`program/program_27_face_detection.py`](program/program_27_face_detection.py) | [`output/exp_27_result.png`](output/exp_27_result.png) |
| 28 | Vehicle Detection in Video Frames | [`program/program_28_vehicle_detection.py`](program/program_28_vehicle_detection.py) | [`output/exp_28_result.png`](output/exp_28_result.png) |
| 29 | Human Eye Detection within Face ROI | [`program/program_29_eye_detection.py`](program/program_29_eye_detection.py) | [`output/exp_29_result.png`](output/exp_29_result.png) |
| 30 | Human Smile Detection within Face ROI | [`program/program_30_smile_detection.py`](program/program_30_smile_detection.py) | [`output/exp_30_result.png`](output/exp_30_result.png) |
| 31 | Image Segmentation by Thresholding | [`program/program_31_image_segmentation.py`](program/program_31_image_segmentation.py) | [`output/exp_31_result.png`](output/exp_31_result.png) |
| 32 | Canvas with 4 Colored Corner Boxes | [`program/program_32_colored_corner_boxes.py`](program/program_32_colored_corner_boxes.py) | [`output/exp_32_result.png`](output/exp_32_result.png) |
| 33 | Draw Rectangle on White Canvas | [`program/program_33_draw_rectangle.py`](program/program_33_draw_rectangle.py) | [`output/exp_33_result.png`](output/exp_33_result.png) |
| 34 | Draw Circle on White Canvas | [`program/program_34_draw_circle.py`](program/program_34_draw_circle.py) | [`output/exp_34_result.png`](output/exp_34_result.png) |
| 35 | Add Centered Text String to Image | [`program/program_35_add_text_to_image.py`](program/program_35_add_text_to_image.py) | [`output/exp_35_result.png`](output/exp_35_result.png) |
| 36 | Background Subtraction based on Color | [`program/program_36_subtract_background.py`](program/program_36_subtract_background.py) | [`output/exp_36_result.png`](output/exp_36_result.png) |
| 37 | Foreground Subtraction based on Color | [`program/program_37_subtract_foreground.py`](program/program_37_subtract_foreground.py) | [`output/exp_37_result.png`](output/exp_37_result.png) |
| 38 | Count Number of Faces in Image | [`program/program_38_count_faces.py`](program/program_38_count_faces.py) | [`output/exp_38_result.png`](output/exp_38_result.png) |
| 39 | Play Video in Reverse Mode in Slow Motion | [`program/program_39_play_video_reverse_slow.py`](program/program_39_play_video_reverse_slow.py) | [`output/exp_39_result.png`](output/exp_39_result.png) |
| 40 | Extract Text from Video Frames using OCR | [`program/program_40_extract_text_from_video.py`](program/program_40_extract_text_from_video.py) | [`output/exp_40_result.png`](output/exp_40_result.png) |

---

## 🚀 How to Run

### Requirements
Install the required dependencies:
```bash
pip install opencv-python numpy matplotlib rapidocr-onnxruntime
```

### Running Programs
Every program in `program/` supports execution both from the repository root and from inside the `program/` directory:

```bash
# Option 1: Run from root directory
python program/program_01_grayscale.py

# Option 2: Run from inside program/ directory
cd program
python program_01_grayscale.py
```

All resulting output images and processed videos are automatically saved into the `output/` directory.

### Viewing Observation Screenshots
Open [`output/index.html`](output/index.html) in any web browser to view the interactive gallery of all 40 verified experiment cards, or browse [`OBSERVATION_RESULTS.md`](OBSERVATION_RESULTS.md).
