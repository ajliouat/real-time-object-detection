import argparse
import yaml
from src.detector import ObjectDetector
from src.utils import load_model, draw_boxes

def main(config):
    # Load model
    model = load_model(config['model_path'])

    # Initialize detector
    detector = ObjectDetector(model, config['confidence_threshold'], config['nms_threshold'])

    # Run detection
    detector.detect(config['input_source'], config['output_path'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    main(config)