"""
SOC 25 - Diabetic Retinopathy Detection
Author: Adnan Shaikh
"""

from flask import Flask, render_template, request, send_from_directory
import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Upload settings
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
model = load_model('dr_model.h5')

# Class labels
classes = ['No_DR', 'Mild', 'Moderate', 'Severe', 'Proliferate_DR']

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess the image
        img = Image.open(filepath).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        preds = model.predict(img_array)
        pred_class = classes[np.argmax(preds)]
        confidence = float(np.max(preds)) * 100

        return render_template('index.html',
                               prediction=pred_class,
                               confidence=f"{confidence:.2f}",
                               filename=filename)
    return "Something went wrong"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
