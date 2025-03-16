import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open USB camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Count people
    people_count = results.pred[0][:, -1].eq(0).sum().item()  # Class 0 is 'person' in COCO dataset

    # Display results
    cv2.putText(frame, f"People: {people_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Crowd Flow Analytics", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


total_people = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    people_count = results.pred[0][:, -1].eq(0).sum().item()
    total_people += people_count

    cv2.putText(frame, f"People: {people_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Total: {total_people}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Crowd Flow Analytics", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
