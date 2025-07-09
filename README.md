# 👁️ SOC 25 – Diabetic Retinopathy Detection

A deep learning-powered web application to detect **diabetic retinopathy** from retinal fundus images.

> 🧑‍💻 Developed by **Adnan Shaikh**  
> 📅 Summer of Code 2025 – SOC 25 Project Submission

---

## 📌 Overview

Diabetic Retinopathy is a leading cause of vision loss. This project uses a Convolutional Neural Network (CNN) to classify eye images into the following 5 categories:

- `No_DR`: No diabetic retinopathy
- `Mild`: Early-stage DR
- `Moderate`: Moderate DR
- `Severe`: Advanced non-proliferative DR
- `Proliferate_DR`: Proliferative diabetic retinopathy

The app provides a simple interface for image upload and prediction.

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 4  
- **Backend**: Flask (Python)
- **Deep Learning**: Keras (TensorFlow backend), trained CNN model
- **Others**: NumPy, Pillow, OpenCV

---

## 🖼️ App Interface

Upload a retinal image and get a prediction:

```
User → Upload Image → Model Prediction → Result with Confidence
```

_Example Screenshot (replace this with your image later):_  
<!-- ![screenshot](assets/screenshot.png) -->

---

## 📁 Folder Structure

```
├── app.py                  # Flask backend
├── templates/              # HTML files
├── assets/                 # Static files (CSS, image assets)
├── uploads/                # Uploaded images (temporary)
├── dr_model.h5             # Trained Keras model
├── soc_25.ipynb            # Model training notebook
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
└── README.md               # Project description (this file)
```

---

## 🚀 Running Locally

1. **Clone the repo**  
```bash
git clone https://github.com/AdnanShaikh88/SOC_25-_Diabetic_Retinopathy_Detection.git
cd SOC_25-_Diabetic_Retinopathy_Detection
```

2. **Install requirements**  
```bash
pip install -r requirements.txt
```

3. **Run the app**  
```bash
python app.py
```


## 📊 Model Info

- Model architecture: CNN
- Image input size: 224x224
- Framework: Keras
- Training dataset: [APTOS 2019 - Kaggle](https://www.kaggle.com/competitions/aptos2019-blindness-detection)

---



