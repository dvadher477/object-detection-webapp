from ultralytics import YOLO
from PIL import Image

# Load the fine-tuned model
model = YOLO("../models/yolov10_bccd.pt")

def predict(image_path):
    image = Image.open(image_path)
    results = model(image)
    predictions = results.pandas().xyxy[0]  # Includes bounding boxes, classes, and confidence scores
    return results.plot(), predictions
