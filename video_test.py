from ultralytics import YOLO
import os

# Load the model (you can specify a model name or path to a trained model)
model = YOLO("yolov8n.pt")  # Replace with your model path if custom

# Set the video path
video_path = "C:/BDM/BSI model/videos"  # Replace with your actual video path

# Run detection
results = model.predict(
    source=video_path,
    conf=0.25,        # Confidence threshold
    save=True,        # Save the output video with bounding boxes
    save_txt=False,   # Set True to save labels per frame
    show=False        # Set True to view video during processing
)

print("✅ Detection completed.")
print("Results saved to:", os.path.abspath("runs/detect/predict"))