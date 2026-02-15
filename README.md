```markdown
# 🔬 inference
### Your Pocket Dermatology Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/ResNet-50-Deep%20Learning-blue?style=for-the-badge" alt="ResNet50">
  <img src="https://img.shields.io/badge/Gemini-API-8E44AD?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API">
</p>

---

## 🎯 What is inference?

**inference** is a cutting-edge skin disease detection system that leverages the power of deep learning to analyze dermatoscopic images and provide instant preliminary diagnoses. Built with precision, empathy, and accessibility in mind, it bridges the gap between advanced AI technology and everyday healthcare needs.

> *"Healthcare shouldn't be a privilege. It should be a tap away."*

---

## 🧠 How It Works

```

┌─────────────┐ ┌──────────────┐ ┌─────────────────┐ ┌──────────────┐ │ Upload │───▶│ ResNet50 │───▶│ Confidence │───▶│ Treatment │ │ Skin Image │ │ Inference │ │ Thresholding │ │ Recommen- │ │ │ │ │ │ (60%) │ │ dations │ └─────────────┘ └──────────────┘ └─────────────────┘ └──────────────┘ │ ▼ ┌──────────────────┐ │ Unknown Class │ │ Detection │ └──────────────────┘

```

### The Magic Under the Hood

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python) |
| **Deep Learning** | PyTorch + ResNet50 |
| **Image Processing** | PIL, TorchVision |
| **NLP Enhancement** | Google Gemini API |
| **Deployment** | Render-Ready |

---

## 🩺 Detectable Conditions

| Disease | Description | Confidence Threshold |
|---------|-------------|---------------------|
| **Acne** | Inflammatory skin condition | 83%+ |
| **Eczema** | Chronic skin inflammation | 85%+ |
| **Psoriasis** | Autoimmune skin disorder | 82%+ |
| **Fungal** | Fungal infections | 91%+ |
| **Normal** | Healthy skin | 94%+ |
| **Unknown** | Low confidence / Rare condition | < 84% |

---

## ✨ Key Features

### 🔍 Intelligent Image Analysis
- State-of-the-art **ResNet50** architecture fine-tuned on dermatological data
- Robust preprocessing pipeline with ImageNet normalization
- Handles images of varying quality with grace

### 🛡️ Smart Uncertainty Handling
- Built-in **confidence thresholding** prevents unreliable predictions
- Gracefully handles unknown conditions with "Unknown" classification
- Encourages professional medical consultation when needed

### 💊 Actionable Recommendations
- Every diagnosis comes with **curated treatment suggestions**
- Direct links to verified medical products and resources
- Clear guidance on when to consult a dermatologist

### 📄 Doctor Report Summarization
- Paste any doctor's report and let **Gemini AI** transform it into clean, structured HTML
- Extract key insights instantly
- Professional formatting for easy understanding

---

## 🚀 Getting Started

### Prerequisites

```

Python 3.8+ pip virtualenv

````

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/inference.git
cd inference

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

### Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=10000
```

> 🔑 **Get your Gemini API key**: Visit [Google AI Studio](https://aistudio.google.com/app/apikey)

### Run the Application

```bash
python app.py
```

The app will be live at `http://localhost:10000`

---

## 📁 Project Structure

```
inference/
├── app.py                      # Main Flask application
├── model/
│   └── skin_dermnet_model.pth # Trained ResNet50 weights
├── templates/
│   ├── index.html             # Main scan interface
│   └── landing.html           # Landing page
├── static/
│   ├── uploads/               # Image upload directory
│   └── *.png                  # Static assets
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🏗️ Architecture Deep Dive

### Model Architecture

```python
SkinDiseaseModel(nn.Module)
├── backbone: ResNet50 (pretrained=False)
│   └── fc: Identity()
└── classifier: Sequential
    ├── Linear(2048 → 256)
    ├── ReLU()
    ├── Dropout(0.4)
    └── Linear(256 → 5)  # 5 classes
```

### Image Preprocessing Pipeline

1. **Resize** → 224×224 pixels
2. **ToTensor** → Convert to tensor [0, 1]
3. **Normalize** → ImageNet stats (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

---

## 🔐 Safety & Disclaimer

<div align="center">

⚠️ **IMPORTANT DISCLAIMER** ⚠️

**inference is NOT a medical device.**

This tool is intended for educational and informational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

---

## 🏆 Acknowledgments

- **DermNet** for the training dataset
- **PyTorch** team for the amazing deep learning framework
- **Google Gemini** for NLP capabilities
- **You** for being curious and building the future of healthcare

---

<div align="center">

### ⭐ If this project helped you, don't forget to star it!

_"The best way to predict the future is to invent it."_ — Alan Kay

</div>
```
