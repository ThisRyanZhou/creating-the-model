from ultralytics import YOLO

# Load your trained model (fixed path)
weights_path = Path("runs/train/yolo_letters2/weights/best.pt")

# Run inference on a single image
results = model("testabcq.jpg")  # returns a list of Results

# Access the first element
result = results[0]

# Show results in a window
result.show()

# Save results to a folder
result.save("runs/test_outputs")

# Print boxes, classes, and confidence
print(result.boxes.xyxy)  # bounding boxes
print(result.boxes.cls)   # predicted class IDs
print(result.boxes.conf)  # confidence scores
