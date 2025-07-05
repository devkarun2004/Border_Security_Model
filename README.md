🛡 Border Surveillance Object Detection using YOLOv8

This project is a real-time object detection system built using YOLOv8, designed for intelligent border surveillance. It detects and classifies multiple entities such as soldiers, intruders (unknown persons), drones, animals, and more from both images and videos, aiding in national security and situational awareness.


---

🚀 Features

🔍 Real-time detection in images and videos

🎯 Multi-class detection:

Soldier (🟢 Green)

Unknown Person / Intruder (🔴 Red)

Animal (🟠 Orange)

Drone (🔺 Bright Red)


🎥 Video frame-by-frame surveillance inference

🧠 Trained using synthetic and open-source datasets

💻 Lightweight CPU inference compatible



---

🧪 Tech Stack

Python 3.12

Ultralytics YOLOv8

OpenCV

Roboflow (for dataset generation)

MakeSense.ai (for manual labeling)

CMD + venv (Windows environment)


📂 Dataset

Total 4 classes: soldier, person, animal, drone

Custom synthetic images (generated) + Roboflow-labeled datasets

Organized in YOLO format with separate train/val directories



🏁 How to Run

1. Clone this repo and navigate to project directory


2. Create and activate virtual environment:

python -m venv venv
.\venv\Scripts\activate


3. Install dependencies:

pip install ultralytics opencv-python


4. Train model:

yolo task=detect mode=train model=yolov8n.pt data="data.yaml" epochs=50 imgsz=640


5. Predict on images/videos:

yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" source="test.jpg"


🧠 Results

Achieved 42.1% mAP@0.5 on "soldier" class

Real-time detection performance on test images and videos

Model adaptable to real border surveillance scenarios


📌 Use Cases

Border and military surveillance

Intrusion and infiltration detection

Real-time situational awareness via CCTV/video
