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


#### 🚀 Features

 - Real-Time Face Detection: Captures live video feed from the webcam to detect faces in real-time.

  - Facial Encoding: Encodes faces from images stored in the Pessoas (People) folder into a unique numeric representation for easy comparison.

 - Face Comparison: Compares faces detected through the webcam against pre-encoded faces in the database to check for similarities.

 - Visual Overlay: Displays a rectangle around detected faces and shows the name of the recognized individual on the video feed.

 - Simple & Effective: Easy-to-use Python script for real-time face recognition, suitable for learning and practical applications.

#### 🛠️ Technologies Used

 - This project uses the following libraries:

 - OpenCV: For capturing the live webcam feed and drawing shapes (e.g., rectangles) on the images or video.

 - face_recognition: A library that simplifies facial recognition tasks like face detection, encoding, and comparison.

 - os: To manage file paths and interact with the directory structure containing images.

#### 🖥️ Installation Guide

##### Clone the repository:


 - git clone https://github.com/ludiemert/Facial_recognition_HOG


 - cd face-recognition-realtime
 - Install the required dependencies:

Make sure you have Python 3.7+ installed, then run the following command to install the necessary libraries:

```python
pip install opencv-python face-recognition
```

#### Prepare the Pessoas directory:

 - Create a folder named Pessoas in the project root directory.
 - Add images of people to the folder. The filenames should be the name of the person (e.g., John.jpg, Elon.jpg).

#### 📂 Directory Structure

```python
face-recognition-realtime/
├── main.py               # Main Python file for the project
├── Pessoas/              # Folder containing images for encoding
│   ├── John.jpg
│   ├── Elon.jpg
│   └── ...
└── README.md             # Project documentation
```

#### ▶️ How to Run

 - Run the script:
```python
python main.py
```
 - Allow access to your webcam. The script will:

 - Resize the live video feed for performance optimization.
Detect faces in real-time.
Compare webcam faces with pre-encoded faces from the Pessoas folder.
Display the name of the recognized person and draw a bounding box around their face.
Press q to exit the program.

#### 📝 Code Overview

1. Encoder Creation (criarEncoders)
This function iterates through all images in the Pessoas folder.
It converts each image to RGB format, as required by the face_recognition library.
The function generates an encoding for each face and stores it alongside the corresponding name.
2. Webcam Face Comparison (compararWebcam)
Captures the live video feed from the webcam using OpenCV.
Detects faces in each frame, resizing the video for performance.
Compares the live face encodings with pre-encoded faces from the Pessoas folder.
Displays the name and draws a bounding box around the face on the live feed.

#### 🔧 Customization
 - Tolerance Adjustment:
 - Adjust the tolerance parameter in the fr.compare_faces function to fine-tune face matching sensitivity.

 - Add More Images:
 - Add more images to the Pessoas folder to increase the recognition database.

Performance Optimization:
Modify the frame resizing parameters for a balance between speed and accuracy in face detection.

#### 🛡️ Limitations and Recommendations
 - Lighting Conditions:
 - The recognition performance may vary under poor lighting or when faces are at extreme angles.

 - Dataset Size:
Larger datasets require more processing power and may affect performance.

 - Face Detection Limitations:
Faces should be clear and front-facing for optimal recognition accuracy.

#### 🤝 Contributions
Contributions are welcome! To contribute to the project:

 - Fork the repository.

Create a new branch:

```python
git checkout -b feature/your-feature-name
```
- Commit your changes:

```python
git commit -m "Add your feature description"
```

```python
Push your branch:
```

```python
git push origin feature/your-feature-name
Open a pull request.
```

#### 📜 License
 - This project is open-source and available under the MIT License.

#### 🙌 Acknowledgements
 - Face Recognition library by Adam Geitgey for simplifying facial recognition tasks.
 - OpenCV for enabling real-time video processing and easy integration with Python.


### 📦 Contribution

 - Feel free to contribute by submitting pull requests or reporting issues.

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


