# 🍽️ Food Detection & Calorie Estimation Web Application

## 📌 Project Overview

This project is a Python-based web application that allows users to upload or capture an image of food through a simple and responsive web interface. The application uses an AI-powered image classification model to analyze the uploaded image and determine whether it contains food.

If food is detected, the system predicts the food category and displays an estimated calorie count based on standard nutritional references. If the image does not contain food, the application clearly informs the user that no food was detected.

The project is designed to be beginner-friendly, fully local (no paid APIs), and suitable for learning, demos, academic projects, or hackathons.

---

## 🧑‍💻 Languages and Libraries Used

### Programming Languages
- **Python 3.11+**
- **HTML5**
- **CSS3**
- **JavaScript (ES6)**

### Backend Framework & Libraries
- **Flask** – Web framework for backend and API handling
- **PyTorch (torch)** – Deep learning framework used for inference
- **Transformers (Hugging Face)** – Pre-trained food image classification model
- **Pillow (PIL)** – Image processing
- **NumPy** – Numerical operations

### Frontend Technologies
- **HTML** – Page structure
- **CSS** – Styling and responsive layout
- **JavaScript (Fetch API)** – Client–server communication
- **MediaDevices API** – Camera capture support in browsers

---

## 🗄️ Database Information

## 📊 Dataset Usage and Model Training Explanation

### Why a Pre-trained Model Is Used Instead of Training on a Dataset from Scratch

This project does not train an AI model from scratch locally. Instead, it uses a **pre-trained food image classification model** that has already been trained on a large, real-world dataset.

The model used in this application is trained on the **Food-101 dataset**, which contains over **101,000 real food images across 101 categories**. This dataset is widely used in academic research and industry for food recognition tasks.

### Reason for This Approach

Training a deep learning model from scratch requires:
- High-performance GPU hardware
- Large storage and memory resources
- Significant training time
- Advanced machine learning expertise

Since the primary goal of this project is to build an **end-to-end AI-powered web application**, rather than to conduct deep learning research, using a pre-trained model is the most practical and industry-standard approach.

### Benefits of Using a Pre-trained Model

- Enables fast and reliable inference on standard laptops
- Eliminates the need for heavy computational resources
- Ensures reproducibility and stability
- Allows the project to focus on application design and user experience

### Calorie Estimation Consideration

There is currently no reliable public dataset that directly maps food images to accurate calorie values. Calorie content depends on portion size, ingredients, and cooking methods, which cannot be determined precisely from an image alone.

Therefore, this project estimates calories by:
- Identifying the food category using the AI model
- Mapping it to standard nutritional reference values
- Displaying an approximate calorie range for a typical serving

This approach ensures transparency, realism, and usability while avoiding misleading precision.

### Dataset and Model Reference

- **Food-101 Dataset**  
  https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/

- **Pre-trained Model Source**  
  Hugging Face Model Hub: `nateraw/food`

### Explanation
- The application performs **real-time image analysis only**
- Food calorie data is stored as a **static Python dictionary**
- No user data, images, or results are persisted

### Future Scope
A database can be added later for:
- User authentication
- History of analyzed images
- Personalized calorie tracking

---

## ⚙️ How to Install and Run

### 1️⃣ Prerequisites
- Windows / macOS / Linux
- Python **3.11 or higher**
- Internet connection (for first-time model download)

---

### 2️⃣ Clone or Create Project Folder and Run
```bash
mkdir food-calorie-app
cd food-calorie-app
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
