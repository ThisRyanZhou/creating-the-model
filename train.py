from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

model.train(
    data="letters.yaml",
    epochs=500,
    imgsz=1024,
    batch=8,

    flipud=0.0,
    fliplr=0.5,

    degrees=10,
    translate=0.2,
    scale=0.5,
    shear=2,

    hsv_h=0.015,
    hsv_s=0.4,
    hsv_v=0.4,

    mosaic=1.0,
    close_mosaic=10,
    mixup=0.2
)
