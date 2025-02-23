# Design Document

## Overview
The Real-Time Object Detection project is designed for autonomous driving applications. It leverages YOLOv8 for high-accuracy object detection and OpenCV for real-time video processing.

## Architecture
- **Preprocessing**: Resizes and normalizes input frames.
- **Inference**: Runs YOLOv8 model on preprocessed frames.
- **Postprocessing**: Filters detections using confidence threshold and non-maximum suppression.
- **Visualization**: Draws bounding boxes and labels on output frames.