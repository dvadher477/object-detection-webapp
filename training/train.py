from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("../models/yolov10.pt")

# Train the model on the BCCD dataset
model.train(data="bccd.yaml", epochs=50, imgsz=640, batch=16)

# Save the fine-tuned model
model.save("../models/yolov10_bccd.pt")