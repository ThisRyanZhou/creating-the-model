from ultralytics import YOLO
import os

model = YOLO("yolov8n.yaml")

epochs = os.environ["EPOCHS"]
imgsz = os.environ["IMAGE_SIZE"]
batch = os.environ["BATCH"]

model.train(
    data="letters.yaml",
    epochs=int(epochs),
    imgsz=int(imgsz),
    batch=int(batch),

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
