from ultralytics import YOLO

# Load the YOLOv8n model (pretrained)
model = YOLO("yolov8n.yaml")

# Train using the YAML dataset
model.train(
    data="letters.yaml",  # path to YAML file
    imgsz=640,
    batch=16,
    epochs=50,
    lr0=0.01,
    project="runs/train",
    name="yolo_letters2"
)

print("Training completed!")
