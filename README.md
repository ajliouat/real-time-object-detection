# Real-Time Object Detection

This project focuses on real-time object detection using YOLOv8. It is designed for autonomous driving applications.

## Features
- **Real-Time Performance**: Optimized for low-latency inference.
- **High Accuracy**: Leverages YOLOv8 for state-of-the-art object detection.
- **Scalable for Edge Devices**: Lightweight and efficient for deployment on edge devices.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Project Structure](#project-structure)
5. [Benchmarks](#benchmarks)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

### Prerequisites
- Python 3.8+
- OpenCV 4.5+
- TensorFlow 2.10+
- PyTorch 1.12+

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

To run real-time object detection:
```bash
./scripts/run_detection.sh --config configs/config.yaml
```

### Key Arguments
- `--config`: Path to the configuration file (YAML format).

---

## Configuration

The `config.yaml` file is the central configuration for the project. Below is an example configuration:

```yaml
model_path: "models/yolov8.pt"  # Path to the YOLOv8 model
input_source: "data/sample_video.mp4"  # Input video or camera source
confidence_threshold: 0.5  # Confidence threshold for detection
nms_threshold: 0.4  # Non-maximum suppression threshold
output_path: "output/detections.mp4"  # Output video path
```

---

## Project Structure

```
real-time-object-detection/
│
├── README.md                   # Project overview
├── requirements.txt            # Python dependencies
├── detect.py                   # Main detection script
├── src/                        # Source code
│   ├── detector.py             # Object detection implementation
│   ├── utils.py                # Utility functions
│   ├── preprocess.py           # Preprocessing functions
│   ├── postprocess.py          # Postprocessing functions
├── configs/                    # Configuration files
│   ├── config.yaml             # Main configuration file
├── models/                     # Model files
│   ├── yolov8.pt               # YOLOv8 model weights
├── data/                       # Data files
│   ├── sample_video.mp4        # Sample video for testing
├── scripts/                    # Build and utility scripts
│   ├── run_detection.sh        # Detection launch script
├── tests/                      # Unit tests
├── benchmarks/                 # Performance benchmarks
├── docs/                       # Documentation
```

---

## Benchmarks

### Performance Comparison
| Feature               | FPS (Frames Per Second) | Accuracy (mAP) |
|-----------------------|-------------------------|----------------|
| YOLOv8 (CPU)          | 15                      | 0.85           |
| YOLOv8 (GPU)          | 60                      | 0.85           |
| TensorFlow (GPU)      | 45                      | 0.82           |

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [OpenCV](https://opencv.org/) for real-time video processing.
- [YOLOv8](https://github.com/ultralytics/ultralytics) for state-of-the-art object detection.
- [TensorFlow](https://www.tensorflow.org/) for model deployment.
