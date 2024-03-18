from ultralytics import  YOLO
model=YOLO('yolov8x')
results=model.predict('oyun.mp4',save=True)
print(results)
print("boxes:")
for box in results[0].boxes:
    print(box)