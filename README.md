````markdown
<div align="center">

# 🚀 Insurance Premium Prediction API

### ⚡ FastAPI + Machine Learning Powered Insurance Cost Prediction System

<br>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>

<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>

<img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange?style=for-the-badge"/>

<img src="https://img.shields.io/github/license/Nilesh-swain/insurance_prediction?style=for-the-badge"/>

<img src="https://img.shields.io/github/stars/Nilesh-swain/insurance_prediction?style=for-the-badge"/>

</p>

<br>

### 🧠 Predict Insurance Premiums using Machine Learning & FastAPI

A modern REST API that predicts insurance costs based on health and demographic data using a trained Random Forest Regression model.

</div>

---

# 📌 Overview

This project is a production-ready **Machine Learning API** built with **FastAPI**.

The system predicts insurance charges using user details such as:

- 👤 Age
- ⚖️ BMI
- 🚬 Smoking Habit
- 👨‍👩‍👧 Children
- 🌍 Region
- ⚧ Gender

The ML model is trained using:

- ✅ Random Forest Regressor
- ✅ Scikit-learn
- ✅ Insurance Dataset

---

# ✨ Features

✅ FastAPI REST API  
✅ High Performance Backend  
✅ Machine Learning Prediction  
✅ Interactive Swagger Documentation  
✅ Clean Folder Structure  
✅ JSON API Responses  
✅ Scalable & Production Ready  
✅ Easy Deployment  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Language |
| FastAPI | API Framework |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```bash
insurance_prediction/
│
├── main.py
├── requirements.txt
├── insurance_randomforest.pkl
├── README.md
├── .gitignore
└── venv/
````

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nilesh-swain/insurance_prediction.git
```

---

## 2️⃣ Navigate into Project

```bash
cd insurance_prediction
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start on:

```bash
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates beautiful API documentation.

| Docs       | URL                         |
| ---------- | --------------------------- |
| Swagger UI | http://127.0.0.1:8000/docs  |
| ReDoc      | http://127.0.0.1:8000/redoc |

---

# 📡 API Endpoint

## 🔮 POST `/predict`

Predict insurance premium based on user information.

---

# 📥 Request Example

```json
{
    "age": 25,
    "sex": "male",
    "bmi": 28.5,
    "children": 1,
    "smoker": "no",
    "region": "southeast"
}
```

---

# 📤 Response Example

```json
{
    "predicted_insurance_cost": 13245.87
}
```

---

# 🧠 Machine Learning Pipeline

```text
User Input
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Random Forest Model
     ↓
Insurance Cost Prediction
```

---

# 📊 Input Features

| Feature  | Type    | Description        |
| -------- | ------- | ------------------ |
| age      | Integer | Age of the user    |
| sex      | String  | Male / Female      |
| bmi      | Float   | Body Mass Index    |
| children | Integer | Number of children |
| smoker   | String  | Smoking status     |
| region   | String  | Residential region |

---

# 🔥 Python API Example

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "age": 25,
    "sex": "male",
    "bmi": 28.5,
    "children": 1,
    "smoker": "no",
    "region": "southeast"
}

response = requests.post(url, json=data)

print(response.json())
```

---

# 🌐 cURL Example

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"age\":25,\"sex\":\"male\",\"bmi\":28.5,\"children\":1,\"smoker\":\"no\",\"region\":\"southeast\"}"
```

---

# ☁️ Deployment on Render

### Prerequisites
- GitHub account with repository pushed
- Render account (free tier available)

### Step 1: Connect Your Repository

1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click **"New Web Service"**
4. Connect your GitHub repository

### Step 2: Configure Service

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Root Directory (Optional):** `./`

### Step 3: Set Environment Variables

| Key | Value |
|-----|-------|
| `PYTHONUNBUFFERED` | `true` |
| `PORT` | `8000` |

### Step 4: Deploy

Click **"Deploy"** and Render will:
- Install dependencies from `requirements.txt`
- Start your FastAPI server
- Provide a public URL

### Step 5: Test Live API

Your API will be available at:
```
https://your-service-name.onrender.com/docs
```

### Auto-Deploy Configuration

Update your `render.yaml` to control what triggers auto-deploy:
- Only deploy when files in `main.py`, `requirements.txt` change
- Ignore changes in `venv/`, `__pycache__/`

---

# 🚀 Future Enhancements

* 🌐 Frontend Dashboard
* 🐳 Docker Support
* ☁️ Advanced Cloud Monitoring
* 🔐 JWT Authentication
* 📈 Model Performance Monitoring
* 🔄 CI/CD Integration
* 📊 Data Visualization
* 📱 Mobile App

---

# 🤝 Contributing

Contributions are welcome.

```bash
1. Fork Repository
2. Create Feature Branch
3. Commit Changes
4. Push Changes
5. Open Pull Request
```

---

# 👨‍💻 Author

## Nilesh Swain

### 🔗 GitHub

https://github.com/Nilesh-swain

---

# ⭐ Show Your Support

If you found this project useful:

⭐ Star the Repository
🍴 Fork the Project
🚀 Build Amazing Things

---

<div align="center">

# ⚡ Built with FastAPI & Machine Learning

### Turning data into predictions, one API call at a time.

</div>
```
