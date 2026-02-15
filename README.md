🔬 Inference  
Your Pocket Dermatology Assistant  

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![ResNet50](https://img.shields.io/badge/ResNet50-Deep%20Learning-blue?style=for-the-badge)
![Gemini API](https://img.shields.io/badge/Gemini-API-8E44AD?style=for-the-badge&logo=google&logoColor=white)

---

🎯 What is Inference?

Inference is a cutting-edge skin disease detection system that leverages deep learning to analyze dermatoscopic images and provide instant preliminary diagnoses.

Built with precision, empathy, and accessibility in mind, it bridges the gap between advanced AI technology and everyday healthcare needs.

"Healthcare shouldn't be a privilege. It should be a tap away."

---

🧠 How It Works

Step 1 — Upload Image  
User uploads a dermatoscopic skin image through the web interface.

Step 2 — Image Preprocessing  
• Resize → 224×224  
• Convert to Tensor  
• Normalize using ImageNet statistics  

Step 3 — Deep Learning Inference  
ResNet50 extracts deep features and predicts probabilities across 5 classes.

Step 4 — Confidence Thresholding  
• If confidence ≥ threshold → Valid prediction  
• If confidence < threshold → Classified as "Unknown"

Step 5 — Smart Recommendations  
• Treatment suggestions generated  
• Gemini API enhances explanations  
• User receives structured output  

Visual Flow

```text
Upload Image
      │
      ▼
Preprocessing
      │
      ▼
ResNet50 Backbone
      │
      ▼
Classifier Head
      │
      ▼
Confidence Check
   ┌───────────────┐
   │ ≥ Threshold   │ → Diagnosis + Treatment
   │ < Threshold   │ → Unknown Classification
   └───────────────┘
```

---

✨ The Magic Under the Hood

Component              | Technology
-----------------------|-------------------------
Backend                | Flask (Python)
Deep Learning          | PyTorch + ResNet50
Image Processing       | PIL, TorchVision
NLP Enhancement        | Google Gemini API
Deployment             | Render-Ready

---

🩺 Detectable Conditions

Disease     | Description                     | Confidence Threshold
------------|---------------------------------|---------------------
Acne        | Inflammatory skin condition     | 83%+
Eczema      | Chronic skin inflammation       | 85%+
Psoriasis   | Autoimmune skin disorder        | 82%+
Fungal      | Fungal infections               | 91%+
Normal      | Healthy skin                    | 94%+
Unknown     | Low confidence / Rare condition | < 84%

---

✨ Key Features

🔍 Intelligent Image Analysis  
- ResNet50 fine-tuned on dermatological data  
- Robust ImageNet normalization  
- Handles varying image quality  

🛡️ Smart Uncertainty Handling  
- Confidence thresholding prevents unreliable predictions  
- Graceful fallback to "Unknown"  
- Encourages professional consultation  

💊 Actionable Recommendations  
- Curated treatment suggestions  
- Clear medical guidance  
- Structured explanations via Gemini API  

📄 Doctor Report Summarization  
- Paste any doctor report  
- Gemini AI transforms it into structured output  
- Extract insights instantly  

---

🚀 Getting Started

Prerequisites  
• Python 3.8+  
• pip  
• virtualenv  

Installation

```bash
git clone https://github.com/yourusername/inference.git
cd inference

python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key_here
PORT=10000
```

Get your Gemini API key:  
https://aistudio.google.com/app/apikey

---

Run the Application

```bash
python app.py
```

App runs at:  
http://localhost:10000

---

📁 Project Structure

```bash
inference/
├── app.py                      # Main Flask entry point
├── model/
│   └── skin_dermnet_model.pth  # Trained ResNet50 weights
├── templates/
│   ├── index.html              # Main scan interface
│   └── landing.html            # Landing page
├── static/
│   ├── uploads/                # Uploaded images
│   └── assets/                 # CSS, images, icons
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

🏗️ Architecture Deep Dive

Model Architecture

```text
Input Image (3 x 224 x 224)
        │
        ▼
┌────────────────────────────┐
│      ResNet50 Backbone     │
│  (Feature Extraction Layer)│
│  Output: 2048-dim vector   │
└────────────────────────────┘
        │
        ▼
┌────────────────────────────┐
│       Classifier Head      │
│  Linear (2048 → 256)       │
│  ReLU Activation           │
│  Dropout (0.4)             │
│  Linear (256 → 5 classes)  │
└────────────────────────────┘
        │
        ▼
Softmax Probabilities
        │
        ▼
Final Prediction
```

Image Preprocessing Pipeline

1. Resize → 224×224 pixels  
2. ToTensor → Convert to tensor [0,1]  
3. Normalize →  
   mean = [0.485, 0.456, 0.406]  
   std  = [0.229, 0.224, 0.225]  

---

🔐 Safety & Disclaimer

⚠️ IMPORTANT DISCLAIMER ⚠️

Inference is NOT a medical device.

This tool is for educational and informational purposes only.  
It is NOT a substitute for professional medical advice, diagnosis, or treatment.  
Always consult a qualified healthcare provider.

---

🤝 Contributing

1. Fork the repository  
2. git checkout -b feature/amazing-feature  
3. git commit -m "Add some amazing feature"  
4. git push origin feature/amazing-feature  
5. Open a Pull Request  

---

🏆 Acknowledgments

- DermNet for the training dataset  
- PyTorch team for the deep learning framework  
- Google Gemini for NLP capabilities  
- You, for building the future of healthcare  

---

⭐ If this project helped you, don’t forget to star it!

"The best way to predict the future is to invent it." — Alan Kay
