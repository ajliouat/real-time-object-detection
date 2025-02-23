from src.detector import ObjectDetector
from src.utils import load_model

def test_detector():
    model = load_model("models/yolov8.pt")
    detector = ObjectDetector(model, 0.5, 0.4)
    detector.detect("data/sample_video.mp4", "output/test_detections.mp4")

if __name__ == "__main__":
    test_detector()