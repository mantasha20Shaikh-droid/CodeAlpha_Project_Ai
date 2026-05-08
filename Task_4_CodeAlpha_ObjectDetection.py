# TASK 4 — Object Detection and Tracking
   # Install Libraries

print("----Task 4 - Object Detection and Tracking----")

!pip install ultralytics opencv-python -q

   # YOLO Object Detection Code

from ultralytics import YOLO
import cv2
from google.colab.patches import cv2_imshow

   # Load YOLO Model
model = YOLO("yolov8n.pt")

   # Load Image
img = cv2.imread("/content/test.jpg")

   # Detect Objects
results = model(img)

   # Show Result
annotated_frame = results[0].plot()

cv2_imshow(annotated_frame)
  # Video Object Tracking

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="/content/Video.mp4",
    show=True
)
