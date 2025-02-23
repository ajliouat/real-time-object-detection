import torch
import cv2

def preprocess_frame(frame):
    # Resize and normalize frame
    frame = cv2.resize(frame, (640, 640))
    frame = frame / 255.0
    frame = torch.from_numpy(frame).float().permute(2, 0, 1).unsqueeze(0)
    return frame