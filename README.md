````markdown
# 🚀 Insurance Premium Prediction API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-green)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

### Intelligent Insurance Cost Prediction using Machine Learning & FastAPI

</div>

---

# 📌 Overview

This project is a **Machine Learning powered FastAPI application** that predicts insurance premiums based on user information such as:

- Age
- BMI
- Smoking habits
- Region
- Number of children
- Gender

The model is trained using a **Random Forest Regressor** and deployed through a high-performance FastAPI backend.

---

# ✨ Features

✅ FastAPI Backend  
✅ Machine Learning Prediction API  
✅ Clean & Scalable Project Structure  
✅ Interactive Swagger Documentation  
✅ Production Ready Setup  
✅ Lightweight & Fast Response  
✅ JSON-Based API Communication  

---

# 🛠️ Tech Stack

| Technology | Usage |
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
fast-api/
│
├── main.py
├── requirements.txt
├── insurance_randomforest.pkl
├── .gitignore
├── README.md
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nilesh-swain/insurance_prediction.git
```

## 2️⃣ Move Into Project Folder

```bash
cd insurance_prediction
```

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows PowerShell

```bash
venv\Scripts\activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API docs.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoint

## POST `/predict`

Predict insurance premium based on user data.

---

# 📥 Sample Request

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

# 📤 Sample Response

```json
{
  "predicted_insurance_cost": 13245.87
}
```

---

# 🧠 Machine Learning Model

The prediction model uses:

- Random Forest Regressor
- Supervised Learning
- Regression Problem Solving

### Model Workflow

```text
User Input
   ↓
Data Preprocessing
   ↓
Random Forest Model
   ↓
Insurance Cost Prediction
```

---

# 📊 Input Features

| Feature | Type | Description |
|---|---|---|
| age | Integer | User age |
| sex | String | Male/Female |
| bmi | Float | Body Mass Index |
| children | Integer | Number of children |
| smoker | String | Smoking habit |
| region | String | Residential region |

---

# 🔥 Example Using Python

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

# 🌐 Example Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"age\":25,\"sex\":\"male\",\"bmi\":28.5,\"children\":1,\"smoker\":\"no\",\"region\":\"southeast\"}"
```

---

# 🚀 Future Improvements

- Docker Deployment
- Frontend Integration
- Cloud Deployment
- Authentication System
- CI/CD Pipeline
- Model Monitoring
- Multiple ML Models Comparison

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Create a Pull Request

---

# 🛡️ License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

### Nilesh Swain

- GitHub: https://github.com/Nilesh-swain

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
🧠 Learn something new  
🚀 Build something amazing  

---

<div align="center">

### Built with FastAPI + Machine Learning ⚡

</div>
````
