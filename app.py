from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
import io

from calorie_data import CALORIE_LOOKUP

app = Flask(__name__)

# Load model
processor = AutoImageProcessor.from_pretrained("nateraw/food")
model = AutoModelForImageClassification.from_pretrained("nateraw/food")
model.eval()

CONFIDENCE_THRESHOLD = 0.60

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    image = Image.open(image_file).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    confidence, predicted_class = torch.max(probs, dim=1)
    confidence = confidence.item()
    label = model.config.id2label[predicted_class.item()]

    if confidence < CONFIDENCE_THRESHOLD:
        return jsonify({
            "is_food": False,
            "message": "No food detected in the image."
        })

    calories = CALORIE_LOOKUP.get(label.lower(), "Unknown")

    return jsonify({
        "is_food": True,
        "food": label,
        "confidence": round(confidence, 2),
        "calories": calories
    })

if __name__ == "__main__":
    app.run(debug=True)
