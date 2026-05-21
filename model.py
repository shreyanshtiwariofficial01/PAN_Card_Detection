from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/pancard_model/weights/best.pt")