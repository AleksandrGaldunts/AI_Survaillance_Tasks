from ultralytics import YOLO

models = ['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt']
for model_name in models:
    print(f"Downloading {model_name}...")
    YOLO(model_name)  # This will download the weights
print("All YOLOv8 variants downloaded!")
