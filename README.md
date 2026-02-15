🔬 Inference
Your Pocket Dermatology Assistant

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![ResNet50](https://img.shields.io/badge/ResNet50-Deep%20Learning-blue?style=for-the-badge)
![Gemini API](https://img.shields.io/badge/Gemini-API-8E44AD?style=for-the-badge&logo=google&logoColor=white)

────────────────────────────────────────

🎯 What is Inference?

Inference is a cutting-edge skin disease detection system that leverages deep learning to analyze dermatoscopic images and provide instant preliminary diagnoses.

Built with precision, empathy, and accessibility in mind, it bridges the gap between advanced AI technology and everyday healthcare needs.

"Healthcare shouldn't be a privilege. It should be a tap away."

────────────────────────────────────────

🧠 How It Works

┌─────────────┐      ┌──────────────┐      ┌─────────────────┐      ┌──────────────┐
│ Upload      │ ───▶ │ ResNet50     │ ───▶ │ Confidence      │ ───▶ │ Treatment    │
│ Skin Image  │      │ Inference    │      │ Thresholding    │      │ Recommen-    │
│             │      │              │      │ (60%)           │      │ dations      │
└─────────────┘      └──────────────┘      └─────────────────┘      └──────────────┘
                             │
                             ▼
                     ┌──────────────────┐
                     │ Unknown Class    │
                     │ Detection        │
                     └──────────────────┘

────────────────────────────────────────

✨ The Magic Under the Hood

Component              | Technology
-----------------------|-------------------------
Backend                | Flask (Python)
Deep Learning          | PyTorch + ResNet50
Image Processing       | PIL, TorchVision
NLP Enhancement        | Google Gemini API
Deployment             | Render-Ready

────────────────────────────────────────

🩺 Detectable Conditions

Disease     | Description                     | Confidence Threshold
------------|---------------------------------|---------------------
Acne        | Inflammatory skin condition     | 83%+
Eczema      | Chronic skin inflammation       | 85%+
Psoriasis   | Autoimmune skin disorder        | 82%+
Fungal      | Fungal infections               | 91%+
Normal      | Healthy skin                    | 94%+
Unknown     | Low confidence / Rare condition | < 84%

────────────────────────────────────────

✨ Key Features

🔍 Intelligent Image Analysis
- ResNet50 architecture fine-tuned on dermatological data
- Robust preprocessing pipeline with ImageNet normalization
- Handles varying image quality gracefully

🛡️ Smart Uncertainty Handling
- Built-in confidence thresholding prevents unreliable predictions
- Gracefully handles unknown conditions
- Encourages professional medical consultation when needed

💊 Actionable Recommendations
- Every diagnosis includes curated treatment suggestions
- Direct links to verified medical resources
- Clear guidance on when to consult a dermatologist

📄 Doctor Report Summarization
- Paste any doctor's report and let Gemini AI transform it into structured output
- Extract key insights instantly
- Professional formatting for easy understanding

────────────────────────────────────────

🚀 Getting Started

Prerequisites

Python 3.8+
pip
virtualenv

Installation

Clone the repository
git clone https://github.com/yourusername/inference.git
cd inference

Create virtual environment
python -m venv venv
source venv/bin/activate
(On Windows: venv\Scripts\activate)

Install dependencies
pip install -r requirements.txt

────────────────────────────────────────

Environment Setup

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here
PORT=10000

Get your Gemini API key:
https://aistudio.google.com/app/apikey

────────────────────────────────────────

Run the Application

python app.py

The app will be live at:
http://localhost:10000

────────────────────────────────────────

📁 Project Structure

inference/
├── app.py
├── model/
│   └── skin_dermnet_model.pth
├── templates/
│   ├── index.html
│   └── landing.html
├── static/
│   ├── uploads/
│   └── *.png
├── requirements.txt
└── README.md

────────────────────────────────────────

🏗️ Architecture Deep Dive

Model Architecture

SkinDiseaseModel(nn.Module)
├── backbone: ResNet50 (pretrained=False)
│   └── fc: Identity()
└── classifier: Sequential
    ├── Linear(2048 → 256)
    ├── ReLU()
    ├── Dropout(0.4)
    └── Linear(256 → 5)

Image Preprocessing Pipeline

1. Resize → 224×224 pixels
2. ToTensor → Convert to tensor [0, 1]
3. Normalize → ImageNet stats
   mean = [0.485, 0.456, 0.406]
   std  = [0.229, 0.224, 0.225]

────────────────────────────────────────

🔐 Safety & Disclaimer

⚠️ IMPORTANT DISCLAIMER ⚠️

Inference is NOT a medical device.

This tool is intended for educational and informational purposes only.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.
Always seek the advice of a qualified healthcare provider regarding any medical condition.

────────────────────────────────────────

🤝 Contributing

1. Fork the repository
2. Create your feature branch:
   git checkout -b feature/amazing-feature
3. Commit your changes:
   git commit -m "Add some amazing feature"
4. Push to the branch:
   git push origin feature/amazing-feature
5. Open a Pull Request

────────────────────────────────────────

🏆 Acknowledgments

- DermNet for the training dataset
- PyTorch team for the deep learning framework
- Google Gemini for NLP capabilities
- You, for building the future of healthcare

────────────────────────────────────────

⭐ If this project helped you, don’t forget to star it!

"The best way to predict the future is to invent it." — Alan Kay
