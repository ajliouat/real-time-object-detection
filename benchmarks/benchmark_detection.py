import time
from src.detector import ObjectDetector
from src.utils import load_model

def benchmark_detection():
    model = load_model("models/yolov8.pt")
    detector = ObjectDetector(model, 0.5, 0.4)

    start_time = time.time()
    detector.detect("data/sample_video.mp4", "output/benchmark_detections.mp4")
    end_time = time.time()

    print(f"Detection completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    benchmark_detection()