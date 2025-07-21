# AI Chatbot for Agricultural Assistance

Empowering farmers with AI—one leaf at a time!

---

## Project Overview

This project is a fully local AI-powered web application designed to assist farmers and agricultural experts. It combines deep learning for paddy leaf disease recognition with a conversational LLM chatbot, delivering instant, actionable insights and expert advice—all from your own device, with no cloud dependency.

---

## Features

- Paddy Disease Prediction  
  Upload a photo of a paddy leaf and receive an instant, high-confidence diagnosis using a deep learning model.

- Conversational Agro Chatbot  
  Ask any agriculture-related question and get expert, context-aware answers powered by a local LLM (Ollama).

- Modern, Responsive UI  
  Clean, visually appealing interface with dynamic backgrounds and intuitive forms.

- 100% Local & Private  
  All AI runs on your machine—no internet required after setup, and your data never leaves your device.

---

## Project Structure

```
.
├── app.py
├── chatbot.py
├── paddy_disease_model.h5
├── requirements.txt
├── README.md
├── index.html
├── style.css
├── static/
│   ├── images/
│   └── uploads/
```

---

## Technology Stack

- Backend: Flask (Python)
- Deep Learning: TensorFlow / Keras
- Chatbot: Ollama (local LLM), LangChain
- Frontend: HTML, CSS (custom, responsive)
- Image Processing: Pillow, NumPy

---

## How It Works

1. Image Upload  
   Users upload a paddy leaf image via the web interface.

2. Disease Prediction  
   The deep learning model analyzes the image and predicts the disease class with confidence scoring.

3. Result Display  
   The predicted disease and the uploaded image are displayed to the user.

4. Expert Chat  
   Users can chat with the AI bot for treatment, prevention, or any agriculture-related queries.

5. Actionable Advice  
   The bot responds with tailored, context-aware recommendations.

---

## User Experience

- Intuitive Upload: Effortlessly upload images for instant analysis.
- Dynamic Chat: Engage in natural conversations with the Agro Bot for expert guidance.
- Visual Feedback: See your uploaded image and prediction results side-by-side.
- Mobile Friendly: Responsive design for use on any device.

---

## Example Use Cases

- Diagnose paddy diseases from leaf images
- Get instant treatment and prevention advice
- Ask about fertilizers, pest management, and best agricultural practices
- Receive step-by-step guidance for crop health

---

## Notes & Customization

- For best results, use clear, well-lit images of paddy leaves.
- The chatbot works offline after initial setup (Ollama must be running locally).
- Customize background images in `static/images/` for your own branding.
- All user data and images remain private and local.

---

## Contributing

Contributions are welcome.  
If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

---

## Contact

For questions or support, open an issue or contact bindelapreetham2004@gmail.com.

Empowering farmers with AI—one leaf at a time!
