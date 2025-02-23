# API Reference

## ObjectDetector
- `__init__(self, model, confidence_threshold, nms_threshold)`: Constructor.
- `detect(self, input_source, output_path)`: Runs object detection on the input source.

## Utils
- `load_model(model_path)`: Loads the YOLOv8 model.
- `draw_boxes(frame, boxes, scores, classes)`: Draws bounding boxes on the frame.

## Preprocessing
- `preprocess_frame(frame)`: Preprocesses the input frame.

## Postprocessing
- `postprocess_detections(detections, confidence_threshold, nms_threshold)`: Filters and processes detections.