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

### Database Used
- **No database is used in the current version of the project**

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
