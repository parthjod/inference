from flask import Flask, render_template, request
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os
from dotenv import load_dotenv
from datetime import datetime

from google import genai

# =====================================================
# Load environment variables
# =====================================================
load_dotenv()

app = Flask(__name__)

# =====================================================
# Gemini API Configuration
# =====================================================
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

GEMINI_MODEL = "gemini-2.5-flash"

# =====================================================
# Classes (must match training)
# =====================================================
disease_classes = ["Acne", "Eczema", "Psoriasis", "Fungal", "Normal"]

# NEW: Unknown detection threshold
CONF_THRESHOLD = 0.6

# =====================================================
# Model Definition
# =====================================================
class SkinDiseaseModel(nn.Module):

    def __init__(self, num_classes):
        super().__init__()

        self.backbone = models.resnet50(pretrained=False)

        in_features = self.backbone.fc.in_features

        self.backbone.fc = nn.Identity()

        self.classifier = nn.Sequential(
            nn.Linear(in_features, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):

        features = self.backbone(x)

        return self.classifier(features)

# =====================================================
# Load trained model
# =====================================================
device = "cpu"

model = SkinDiseaseModel(len(disease_classes))

checkpoint = torch.load(
    "model/skin_disease_dermnet.pth",
    map_location=device
)

model.load_state_dict(checkpoint["model_state_dict"])

model.eval()

# =====================================================
# Image Transform
# =====================================================
transform = transforms.Compose([
    transforms.Resize((224, 224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# =====================================================
# Helper: linkify URLs
# =====================================================
def linkify(text):

    import re

    url_pattern = r'(https?://[^\s\)]+)'

    return re.sub(
        url_pattern,
        r'<a href="\1" target="_blank" style="color: var(--primary); font-weight: 600; text-decoration: underline;">\1</a>',
        text
    )

# =====================================================
# Next Steps Recommendations
# =====================================================
raw_next_steps = {

    "Acne":
    "For mild acne, use Benzac AC (https://tinyurl.com/8ywvzn5m). If persistent, consult dermatologist.",

    "Eczema":
    "Moisturize regularly. Hydrocortisone cream may help (https://tinyurl.com/43hmwb7v).",

    "Psoriasis":
    "Calcipotriol treatment recommended (https://tinyurl.com/hasbr8xa). Consult dermatologist.",

    "Fungal":
    "Use Clotrimazole antifungal cream (https://tinyurl.com/hasbr8xa). Keep area dry.",

    "Normal":
    "Skin appears healthy. Maintain routine using gentle cleanser (https://tinyurl.com/mwuc9fsv).",

    # NEW: Unknown recommendation
    "Unknown":
    "The AI model is not confident about this image. This may be an uncommon condition or non-skin image. Please consult a certified dermatologist for proper diagnosis."
}

next_steps = {k: linkify(v) for k, v in raw_next_steps.items()}

# =====================================================
# Medical-grade prediction function
# =====================================================
def predict_disease(image):

    model_input = transform(image).unsqueeze(0)

    with torch.no_grad():

        outputs = model(model_input)

        probs = torch.softmax(outputs, dim=1)

        confidence, predicted_idx = torch.max(probs, dim=1)

    confidence_value = confidence.item()

    predicted_class = disease_classes[predicted_idx.item()]

    # Unknown detection logic
    if confidence_value < CONF_THRESHOLD:

        return "Unknown", confidence_value

    else:

        return predicted_class, confidence_value

# =====================================================
# ROUTES
# =====================================================

@app.route("/", methods=["GET"])
def landing():

    return render_template("landing.html")


@app.route("/scan", methods=["GET", "POST"])
def scan():

    result = None
    confidence = None
    summary = None
    error = None
    image_url = None
    scan_date = None

    if request.method == "POST":

        # =====================================
        # Image Upload Flow
        # =====================================
        if "image" in request.files and request.files["image"].filename != "":

            file = request.files["image"]

            try:

                filename = "temp_upload.png"

                filepath = os.path.join("static", "uploads", filename)

                file.save(filepath)

                image_url = f"/static/uploads/{filename}"

                image = Image.open(filepath).convert("RGB")

                disease, conf = predict_disease(image)

                confidence = round(conf * 100, 1)

                scan_date = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")

                result = {

                    "disease": disease,

                    "next_steps": next_steps.get(
                        disease,
                        "Consult dermatologist."
                    )
                }

            except Exception as e:

                error = f"Error processing image: {str(e)}"

        # =====================================
        # Gemini Report Summary Flow
        # =====================================
        elif "report" in request.form and request.form["report"].strip() != "":

            report_text = request.form["report"]

            try:

                prompt = (
                    "Summarize doctor's report into simple bullet points:\n\n"
                    f"{report_text}"
                )

                response = gemini_client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt
                )

                summary = response.text

            except Exception as e:

                error = f"Error generating summary: {str(e)}"

    return render_template(

        "index.html",

        result=result,

        confidence=confidence,

        summary=summary,

        error=error,

        image_url=image_url,

        scan_date=scan_date
    )

# =====================================================
# Run App
# =====================================================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )