from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
import pandas as pd

app = Flask(__name__)

# -----------------------------
# Load AI Model
# -----------------------------
processor = AutoImageProcessor.from_pretrained("nateraw/food")
model = AutoModelForImageClassification.from_pretrained("nateraw/food")
model.eval()

CONFIDENCE_THRESHOLD = 0.60

# -----------------------------
# Load Real Calorie Lookup Data
# -----------------------------
calorie_df = pd.read_csv("calorie_data.csv")

def get_calories(food_name):
    food_name = food_name.lower()
    match = calorie_df[calorie_df["food"] == food_name]
    if not match.empty:
        return {
            "calories_per_100g": int(match.iloc[0]["calories_per_100g"]),
            "source": match.iloc[0]["source"]
        }
    return None

# -----------------------------
# Routes
# -----------------------------
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
    food_label = model.config.id2label[predicted_class.item()].lower()

    if confidence < CONFIDENCE_THRESHOLD:
        return jsonify({
            "is_food": False,
            "message": "No food detected in the image."
        })

    calorie_info = get_calories(food_label)

    if calorie_info:
        return jsonify({
            "is_food": True,
            "food": food_label.title(),
            "confidence": round(confidence, 2),
            "calories": f"{calorie_info['calories_per_100g']} kcal per 100g",
            "data_source": calorie_info["source"]
        })
    else:
        return jsonify({
            "is_food": True,
            "food": food_label.title(),
            "confidence": round(confidence, 2),
            "calories": "Calorie data not available",
            "data_source": "N/A"
        })

if __name__ == "__main__":
    app.run(debug=True)
