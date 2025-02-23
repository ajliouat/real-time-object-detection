import torch
import cv2

def load_model(model_path):
    model = torch.hub.load('ultralytics/yolov8', 'custom', path=model_path)
    return model

def draw_boxes(frame, boxes, scores, classes):
    for box, score, cls in zip(boxes, scores, classes):
        x1, y1, x2, y2 = box
        label = f"{cls} {score:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame