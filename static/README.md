# 🪪 PAN Card Detection Using YOLO – Computer Vision Project
## 📌 Project Overview

This project focuses on building an **AI-powered PAN Card Detection System using the YOLO (You Only Look Once)** object detection algorithm. The primary objective is to automatically detect PAN Cards from uploaded images using deep learning and computer vision techniques.

The project is entirely AI-driven and detection-oriented, where the model identifies PAN Card regions from input images with high accuracy.

## 🎯 Problem Statement

Manual document verification processes are time-consuming and inefficient in many industries such as banking, finance, KYC verification, and government services.

**The goal of this project is to:**
- Detect PAN Cards automatically from images
- Reduce manual verification effort
- Improve document identification accuracy
- Build a real-time AI-based detection system

---

## 🧾 Dataset Description
The dataset contains PAN Card images annotated for object detection training.

**Dataset Includes:**
- PAN Card Images
- Bounding Box Annotations
- YOLO Label Files

### Annotation Information:

**Each image contains:**

- PAN Card object coordinates
- Detection class labels
- Bounding box information

---

## 🔍 Project Workflow

The project followed a structured, industry-standard workflow:

### 1️⃣ Data Understanding
- Checked dataset structure and image organization
- Verified annotation files and YOLO label format
- Identified object classes for detection

### 2️⃣ Data Preprocessing
- Resized images for model training
- Organized train and validation datasets
- Validated annotation accuracy

### 3️⃣ Exploratory Analysis
- Analyzed image distributions
- Checked annotation consistency
- Observed bounding box patterns
- Examined dataset balance

### 4️⃣ Model Training
- YOLO Object Detection Training
- Trained YOLO model on custom PAN Card dataset
- Learned PAN Card localization and detection
- Optimized detection accuracy

### 5️⃣ Model Evaluation
- Detection Performance Analysis
- Tested model on unseen images
- Evaluated prediction confidence
- Verified bounding box accuracy

### 6️⃣ FastAPI Integration
- Backend Development
- Built FastAPI prediction API
- Uploaded images processed through AI model
- Detection output returned dynamically

### 7️⃣ Frontend Development
**Modern UI Design**
- Created futuristic glassmorphism UI
- Added drag-and-drop upload functionality
- Displayed detection output visually

---

## 📊 Key Observations
- YOLO performs fast real-time PAN Card detection
- Proper annotation improves detection accuracy
- Image quality affects model prediction performance
- Bounding box precision is important for accurate detection
- Deep learning enables automated document verification

---

## 📈 Key Insights
- YOLO is highly effective for custom object detection tasks
- PAN Card detection can be automated efficiently using AI
- Real-time detection reduces manual verification effort
- Deep learning improves scalability in document verification systems
- AI-based systems provide faster and more reliable results

## 🛠 Tools & Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook

---

## 📈 Outcome

This project demonstrates the importance of deep learning and computer vision in automating real-world document verification systems.

### The system successfully:

- Detects PAN Cards from uploaded images
- Generates bounding box predictions
- Provides real-time AI-based detection results
- Integrates AI with modern web technologies

---

## 🚀 Future Work
- OCR integration for PAN number extraction
- Aadhaar Card detection support
- Multi-document detection system
- Real-time webcam detection
- Cloud deployment
- Mobile application integration

---

## Project Structure

PAN_Card_Detection/
│
├── images/                  # Sample PAN card images for testing
│   ├── sample1.jpg
│   └── sample2.png
│
├── output/                  # Extracted results saved here
│
├── src/
│   ├── detect.py            # Main PAN card detection logic
│   ├── preprocess.py        # Image preprocessing functions
│   ├── ocr.py               # OCR text extraction
│   └── utils.py             # Helper utilities
│
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md