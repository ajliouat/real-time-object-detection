from src.postprocess import postprocess_detections
import torch

def test_postprocess():
    detections = torch.randn(100, 6)  # Mock detections
    boxes, scores, classes = postprocess_detections(detections, 0.5, 0.4)
    assert len(boxes) == len(scores) == len(classes)

if __name__ == "__main__":
    test_postprocess()