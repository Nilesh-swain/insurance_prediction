from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import pickle
import uvicorn

# =========================
# Load Model
# =========================

try:
    with open("insurance_randomforest.pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:
    print(f"Model loading failed: {e}")
    model = None

# =========================
# FastAPI App
# =========================

app = FastAPI(
    title="Insurance Charges Prediction API",
    description="Predict medical insurance charges using Random Forest Model",
    version="1.0.0"
)

# =========================
# Input Schema
# =========================

class InsuranceData(BaseModel):

    age: int = Field(..., gt=0, lt=100)
    sex: str
    bmi: float = Field(..., gt=10, lt=60)
    children: int = Field(..., ge=0, le=10)
    smoker: str
    region: str

# =========================
# Home Route
# =========================

@app.get("/")
def home():

    return {
        "message": "Insurance Prediction API Running Successfully 🚀"
    }

# =========================
# Health Check Route
# =========================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }

# =========================
# Prediction Route
# =========================

@app.post("/predict")
def predict(data: InsuranceData):

    try:

        if model is None:
            raise HTTPException(
                status_code=500,
                detail="Model not loaded properly"
            )

        # -------------------------
        # Convert Input to DataFrame
        # -------------------------

        input_data = pd.DataFrame({
            "age": [data.age],
            "sex": [data.sex.lower()],
            "bmi": [data.bmi],
            "children": [data.children],
            "smoker": [data.smoker.lower()],
            "region": [data.region.lower()]
        })

        # -------------------------
        # Prediction
        # -------------------------

        prediction = model.predict(input_data)

        predicted_charge = float(round(prediction[0], 2))

        # -------------------------
        # Response
        # -------------------------

        return {
            "success": True,
            "prediction": {
                "predicted_insurance_charge": predicted_charge
            },
            "input_data": input_data.to_dict(orient="records")[0]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

# =========================
# Run Server
# =========================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )