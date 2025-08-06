# Helmet Detection Using Yolo Shift Invariant Technique


# Abstract

The abstract for the project describes a computer vision system for detecting helmets worn by motorcyclists in real-time
Using You Only Look Once (YOLO) object detection method. The system is designed to perform in various lighting and
Surrounding circumstances and are capable of detecting helmets even when the wearer is in motion or there are shifts in the
Camera's perspective. The system is trained on an enormous dataset of annotated helmet photos and can accurately detect
Helmets with a high degree of precision and recall. The project demonstrates the potential of YOLO and deep learning
techniques to improve road safety by automatically detecting and alerting riders who are not wearing helmets, helping to
reduce the number of motorcycle-related accidents and fatalities.

Keywords— CNN, Computer vision, Deep learning, Helmet detection, model training, , Traffic data, YOLO

# Objectives

- Detect motorcyclists in real-time video streams
- Identify whether riders are wearing helmets or not
- Mark violators with bounding boxes and alert labels
- Improve detection accuracy in varying lighting and motion conditions

# What I Did

- Trained a YOLO-based model using a custom dataset of helmet/no-helmet images
- Preprocessed and annotated training data using LabelImg
- Applied OpenCV for real-time video capture and detection
- Improved detection performance using image augmentation and parameter tuning
- Achieved ~85% accuracy in real-world helmet detection scenarios

# Technologies & Tools

- YOLOv3 / YOLOv4
- Python
- OpenCV
- LabelImg (for data annotation)
- NumPy, Matplotlib (for visualization and data handling)

# Results

- Accurate detection of helmet vs. no-helmet in diverse conditions
- Real-time performance with minimal lag using OpenCV
- Potential integration into smart traffic systems or CCTV monitoring tools
