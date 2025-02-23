import cv2
import torch
from src.preprocess import preprocess_frame
from src.postprocess import postprocess_detections

class ObjectDetector:
    def __init__(self, model, confidence_threshold, nms_threshold):
        self.model = model
        self.confidence_threshold = confidence_threshold
        self.nms_threshold = nms_threshold

    def detect(self, input_source, output_path):
        cap = cv2.VideoCapture(input_source)
        if not cap.isOpened():
            raise ValueError("Unable to open video source")

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Preprocess frame
            input_tensor = preprocess_frame(frame)

            # Run inference
            with torch.no_grad():
                detections = self.model(input_tensor)

            # Postprocess detections
            boxes, scores, classes = postprocess_detections(detections, self.confidence_threshold, self.nms_threshold)

            # Draw boxes on frame
            output_frame = draw_boxes(frame, boxes, scores, classes)

            # Write output frame
            out.write(output_frame)

        cap.release()
        out.release()