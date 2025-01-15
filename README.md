# Proj_YOLO
Object detection with the YOLO computer vision method

### 🧑💻 YOLO Video Detection: Real-Time Object Detection 🕵️‍♂️🎥

 - This project demonstrates the power of YOLO (You Only Look Once), one of the most popular and efficient methods for real-time object detection. Using Python, OpenCV, and a pre-trained model, the script processes videos or camera streams and identifies objects with high precision and performance.

---

<h4 align="center">Face Detection - img_FR_HOG 🚀</h4>

<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="img_Yolo/1 - proj_Yolo_tiny.png" style="width: 90%;" alt="2_rectangle_imgElon">
                <p style="margin-top: 5px;">1 - proj_Yolo_tiny </p>
            </td>
            <td style="width: 50%; text-align: center;">
                <img src="img_Yolo/2 - yolov3 com acuracia maior.png" style="width: 90%;" alt="5_compare_faces_false">
                <p style="margin-top: 5px;">2 - yolov3 com acuracia maior.png</p>
            </td>
        </tr>
    </table>
</div>

  <br/>
  <br/>


<h4 align="center"> yolov3 with more accuracy 🚀</h4>

<div align="center">
    <table>
        <tr>
           <td style="width: 50%; text-align: center;">
                <img src="img_Yolo/3 - yolov3 com acuracia maior.png" style="width: 90%;" alt="2_rectangle_imgElon">
                <p style="margin-top: 5px;"> yolov3 with more accuracy </p>
            </td>          
        </tr>
    </table>
</div>

  <br/>
  <br/>


---


  <br/>
  <br/>


#### 🚀 About YOLO

 - YOLO (You Only Look Once) is a revolutionary approach to object detection that balances accuracy and speed. Unlike other methods that divide the image into multiple regions and analyze each one separately, YOLO views the image as a whole, making class and location predictions simultaneously.

 ---

#### 🛠️ Why Use YOLO?

 - Speed: YOLO is extremely fast, making it ideal for real-time applications.
 - Accuracy: Despite being fast, it maintains significant accuracy, especially in optimized versions like YOLOv3.
 -  Unified Approach: It treats detection as a regression problem, unifying all steps into a single operation.

  ---
  
#### 🖥️ How Does It Work?

- Image Division: The image is divided into a grid of cells.
- Prediction per Cell: Each cell predicts a set of bounding boxes and class probabilities for objects.
- Smart Filtering: YOLO uses methods like Non-Maximum Suppression (NMS) to remove overlaps and improve detection clarity.


#### 🖥️ YOLOv3 and YOLOv3-tiny:
- In this project, you can choose between:
-  ##### YOLOv3: More accurate, ideal for complex detections.
-  ##### YOLOv3-tiny: A lighter and faster version, suitable for devices with lower processing power.

 ---

####   📋 Features
- Real-Time Object Detection: Identifies and displays object classes and confidence levels directly on the video feed.
- Bounding Boxes: Precise bounding boxes around detected objects.
- Easy Customization: Switch between YOLO models and adjust confidence thresholds and resolution settings.
- Multi-Class Detection: Recognizes up to 80 different classes based on the COCO dataset, including people, animals, vehicles, and more.

 ---
 
####  🛠️ Requirements

- Ensure you have the following installed before running the project:

- Python 3.8+
- Libraries:
- OpenCV: pip install opencv-python
- NumPy: pip install numpy
- YOLO Files:
- yolov3.cfg and yolov3.weights (or their tiny versions)
- coco.names (list of classes)
- Video input or camera.

 ---
 
#### 🚦 How to Use

1. Clone the Repository
```python
git clone https://github.com/ludiemert/Proj_YOLO.git
cd your-repo
```

2. Add YOLO Model Files
```python
Place the yolov3.cfg, yolov3.weights, and coco.names files in the root directory.
```

3. Configure Video or Camera
- In the code, edit the line that defines the video source:

```python
video = cv2.VideoCapture('dog1.mp4')  # For camera, replace with '0' or '1'.
```

4. Run the Script
```python
python yolo_video_detection.py
```

5. View the Results
- The video will display in a window with real-time object detections.

 ---
 
#### ⚙️ Customizable Settings

- Model Resolution: Adjust the input size to balance accuracy and performance:

```python
blob = cv2.dnn.blobFromImage(img, 1/255, (320, 320), [0, 0, 0], 1, crop=False)
```

- Confidence Threshold: Set the confidence threshold to display detections:

```python
confThresh = 0.5
```

 ---
 
#### 🌟 Use Cases

- Real-Time Security: Detect people or vehicles in a camera feed.
 - Animal Monitoring: Identify specific animals in videos (like "dog1.mp4").
 - Commercial Applications: Track products in industrial environments.

#### 🖼️ Demonstration
 - Before YOLO:


 ---
 
#### After YOLO:

 ---
 
#### 🧠 How the Script Works
 - Video Reading: The script reads frames from the video or camera.
 - Pre-Processing: Images are normalized and resized to the model-supported size (e.g., 320x320).
 - Inference: YOLO processes the frames to detect objects.
 - Post-Processing: Applies NMS to reduce noise and display the final bounding boxes.
 - Display: Shows the processed frames with identified objects.

 ---
 
#### 📜 License
 - This project is licensed under the MIT License. Feel free to use and modify the code as needed.


 ---
 
#### 🤝 Contributions
 - Contributions are welcome! Follow these steps:

- Fork the project.
- Create a branch for your feature: git checkout -b my-feature.
 - Commit your changes: git commit -m 'Added a new feature'.
 - Push the branch: git push origin my-feature.
 - Open a Pull Request.

 ---
 

### 📦 Portugues





- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

## 🌐 **Contact**
<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

---
Developed with ❤ by [ludiemert](https://github.com/ludiemert).


