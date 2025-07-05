from ultralytics import YOLO
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on all images in the directory and save the results
results = model.predict(
    source="C:/BDM/BSI model/images/test",  # Folder with input images
    save=True,        # Save output images with bounding boxes
    save_txt=False,   # Set to True to save labels as .txt files
    show=False        # Set to True to display the images during inference
)

print("✅ Inference completed.")
print("Results saved to:", os.path.abspath("runs/detect/predict"))