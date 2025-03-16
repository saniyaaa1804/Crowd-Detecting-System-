import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_crowd_density(station=None):
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error: Could not open webcam."

    # Set resolution (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        return "Error: Could not read frame."

    # Perform inference
    results = model(frame)

    # Count people
    people_count = results.pred[0][:, -1].eq(0).sum().item()  # Class 0 is 'person' in COCO dataset

    # Classify crowd density
    if people_count <= 2:
        density = "Low"
    elif 3 <= people_count <= 3:
        density = "Medium"
    else:
        density = "High"

    # Release the webcam
    cap.release()

    return density
