# AI Chatbot for Agricultural Assistance

Welcome to the AI Chatbot for Agricultural Assistance! This project combines deep learning and conversational AI to help farmers and agricultural experts diagnose paddy diseases from leaf images and get instant, expert advice on treatment and prevention.

## Features
- Paddy Disease Prediction: Upload a leaf image and get instant disease classification using a trained deep learning model.
- Conversational Chatbot: Ask any agriculture-related question and get expert, context-aware answers powered by a local LLM (Ollama).
- Beautiful, Modern UI: Clean, responsive interface with background images and easy-to-use forms.
- No Cloud Required: All AI runs locally—no OpenAI API key or internet required after setup!

## Project Workflow

User Uploads Paddy Leaf Image → Model Predicts Disease → Display Predicted Disease & Image → User Chats with AI Bot → Bot Gives Disease-Specific & General Advice

1. Upload Image: User uploads a paddy leaf image via the web interface.
2. Prediction: The deep learning model predicts the disease.
3. Result Display: The predicted disease and uploaded image are shown.
4. Chat: User can ask the AI bot for treatment, prevention, or any agri-related question.
5. Expert Advice: The bot responds with actionable, context-aware advice.

## Project Structure

```
├── app.py
├── chatbot.py
├── paddy_disease_model.h5
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── images/
│   └── uploads/
```

## Quickstart

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the model:
   - Place `paddy_disease_model.h5` in the project root (if not present)
   - For chatbot, make sure Ollama is running with the required model (e.g., llama3.2:1b)
5. Run the app:
   ```bash
   python app.py
   ```
6. Open your browser:
   - Go to http://localhost:5001

## Tech Stack
- Flask (Python web framework)
- TensorFlow / Keras (Deep learning model)
- Ollama (Local LLM for chatbot)
- HTML/CSS (Frontend)

## Example Use Cases
- Diagnose paddy diseases from leaf images
- Get instant treatment and prevention advice
- Ask general agriculture questions (fertilizers, pests, best practices)

## Notes
- For best results, use clear, well-lit images of paddy leaves.
- The chatbot works offline after initial setup (Ollama must be running locally).
- You can customize the background images in `static/images/` for your own branding.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or support, open an issue or contact [your-email@example.com].

Empowering farmers with AI—one leaf at a time! 