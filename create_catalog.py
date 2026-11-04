import os

titles = [
    'Convert Image to Grayscale',
    'Convert Image to Blur using Gaussian Blur',
    'Canny Edge Detection Outline',
    'Histogram Equalization',
    'Color Histogram Analysis',
    'Image Erosion using Erode Function',
    'Video Slow Motion & Fast Motion Playback',
    'Image Dilation using Dilate Function',
    'Image Scaling (2x Bigger and 0.5x Smaller)',
    '90-Degree Clockwise Rotation Along Y-Axis',
    '180-Degree Clockwise Rotation Along Y-Axis',
    '270-Degree Clockwise Rotation Along Y-Axis',
    'Affine Transformation',
    'Perspective Transformation',
    'Harris Corner Detection',
    'Sobel Edge Detection Filter',
    'Image Watermarking Technique',
    'Image Cropping, Copying & Pasting ROI',
    'Morphological Erosion Technique',
    'Morphological Dilation Technique',
    'Morphological Opening Technique',
    'Morphological Closing Technique',
    'Morphological Top Hat Technique',
    'Morphological Black Hat Technique',
    'Watch Object Recognition',
    'Reverse Frames of Video',
    'Human Face Detection',
    'Vehicle Detection in Video Frames',
    'Human Eye Detection within Face ROI',
    'Human Smile Detection within Face ROI',
    'Image Segmentation by Thresholding',
    'Canvas with 4 Colored Corner Boxes',
    'Draw Rectangle on White Canvas',
    'Draw Circle on White Canvas',
    'Add Centered Text String to Image',
    'Background Subtraction based on Color',
    'Foreground Subtraction based on Color',
    'Count Number of Faces in Image',
    'Play Video in Reverse Mode in Slow Motion',
    'Extract Text from Video Frames using OCR'
]

# Generate Markdown catalog
with open('OBSERVATION_RESULTS.md', 'w', encoding='utf-8') as md:
    md.write('# Computer Vision Laboratory - All 40 Observation Results\n\n')
    md.write('This document contains the verified observation results, inputs, outputs, and screenshots for all 40 laboratory experiments from **ITA05 - Computer Vision Laboratory**.\n\n')
    md.write('| Exp No | Experiment Title | Python Program | Observation Screenshot |\n')
    md.write('|:---:|:---|:---|:---:|\n')
    for i in range(1, 41):
        py_files = [f for f in os.listdir('program') if f.startswith(f'program_{i:02d}')]
        py_name = py_files[0] if py_files else f'program_{i:02d}.py'
        img_rel = f'output/exp_{i:02d}_result.png'
        md.write(f'| {i} | {titles[i-1]} | [{py_name}](file:///d:/computer%20vision/program/{py_name}) | [View Screenshot](file:///d:/computer%20vision/{img_rel}) |\n')
    md.write('\n## Gallery of Observation Cards\n\n')
    for i in range(1, 41):
        md.write(f'### Experiment {i}: {titles[i-1]}\n')
        md.write(f'![Exp {i} Observation Screenshot](file:///d:/computer%20vision/output/exp_{i:02d}_result.png)\n\n---\n\n')

# Generate interactive HTML Gallery
with open('output/index.html', 'w', encoding='utf-8') as html:
    html.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Computer Vision Lab - Observation Results Gallery</title>
<style>
  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
  h1 { text-align: center; color: #38bdf8; margin-bottom: 8px; }
  p.subtitle { text-align: center; color: #94a3b8; margin-bottom: 30px; font-size: 16px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(560px, 1fr)); gap: 24px; max-width: 1500px; margin: 0 auto; }
  .card { background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.4); border: 1px solid #334155; transition: transform 0.2s; }
  .card:hover { transform: translateY(-4px); border-color: #38bdf8; }
  .card-header { padding: 12px 18px; background: #0f172a; border-bottom: 1px solid #334155; font-size: 17px; font-weight: 600; color: #e2e8f0; }
  .card img { width: 100%; height: auto; display: block; }
</style>
</head>
<body>
<h1>ITA05 - Computer Vision Laboratory</h1>
<p class="subtitle">Complete Observation Record & Results Gallery for All 40 Experiments</p>
<div class="grid">
''')
    for i in range(1, 41):
        html.write(f'''  <div class="card">
    <div class="card-header">Exp {i}: {titles[i-1]}</div>
    <img src="exp_{i:02d}_result.png" alt="Exp {i} Result" loading="lazy">
  </div>\n''')
    html.write('''</div>\n</body>\n</html>''')

print('Generated OBSERVATION_RESULTS.md and output/index.html successfully!')
