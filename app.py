from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from chatbot import chatbot_instance  # Ensure chatbot_instance is defined in chatbot.py
import numpy as np
import os

app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Class label mapping
class_labels = {
    0: "Bacterial leaf blight",
    1: "Bacterial leaf streak",
    2: "Bacterial panicle blight",
    3: "Blast",
    4: "Brown spot",
    5: "Dead heart",
    6: "Downy mildew",
    7: "Hispa",
    8: "Normal",
    9: "Tungro"
}

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# @app.route('/predict', methods=['POST'])
# def predict():
#     prediction_label = None
#     image_url = None

#     if 'image' not in request.files:
#         return render_template("index.html", prediction="No image provided.")

#     file = request.files['image']
#     if file.filename == '':
#         return render_template("index.html", prediction="No selected file.")

#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Load model only when needed (prevents compile_metrics warning)
#         model = load_model("paddy_disease_model.h5")

#         # Preprocess image
#         img = image.load_img(filepath, target_size=(224, 224))
#         img_array = np.expand_dims(img, axis=0)

#         # Predict
#         prediction = model.predict(img_array)
#         predicted_class = np.argmax(prediction)
#         prediction_label = class_labels[predicted_class]
#         image_url = filepath

#     return render_template("index.html", prediction=prediction_label, image_url=image_url)

@app.route('/predict', methods=['POST'])
def predict():
    prediction_label = None
    image_url = None
    confidence_threshold = 0.7  # 👈 Set your own confidence threshold here

    if 'image' not in request.files:
        return render_template("index.html", prediction="No image provided.")

    file = request.files['image']
    if file.filename == '':
        return render_template("index.html", prediction="No selected file.")

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Load model only when needed
        model = load_model("paddy_disease_model.h5")

        # Preprocess image
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = np.expand_dims(img, axis=0)

        # Predict
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        confidence_score = float(np.max(prediction))  # Get the highest confidence

        if confidence_score < confidence_threshold:
            prediction_label = "Image not recognized as a valid paddy leaf. Please upload a valid paddy leaf image."
        else:
            prediction_label = f"{class_labels[predicted_class]} (Confidence: {confidence_score:.2f})"

        image_url = filepath

    return render_template("index.html", prediction=prediction_label, image_url=image_url)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    response = None

    if user_input:
        response = chatbot_instance.get_response(user_input)

    return render_template("index.html", response=response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    

    