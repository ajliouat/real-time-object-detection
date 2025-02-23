import torch

def postprocess_detections(detections, confidence_threshold, nms_threshold):
    boxes = detections[..., :4]
    scores = detections[..., 4]
    classes = detections[..., 5]

    # Filter by confidence threshold
    mask = scores > confidence_threshold
    boxes = boxes[mask]
    scores = scores[mask]
    classes = classes[mask]

    # Apply non-maximum suppression
    keep = torch.ops.torchvision.nms(boxes, scores, nms_threshold)
    boxes = boxes[keep]
    scores = scores[keep]
    classes = classes[keep]

    return boxes, scores, classes