from src.preprocess import preprocess_frame
import cv2

def test_preprocess():
    frame = cv2.imread("data/sample_frame.jpg")
    input_tensor = preprocess_frame(frame)
    assert input_tensor.shape == (1, 3, 640, 640)

if __name__ == "__main__":
    test_preprocess()