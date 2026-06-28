from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LinearRegression

app = FastAPI()

# จำลองข้อมูลเพื่อสร้างโมเดล (X: [เข้าเรียน(ครั้ง), อ่านหนังสือ(ชม.)], y: เกรดเฉลี่ย)
# ข้อมูลสมมติ: เข้าเรียนเยอะ + อ่านหนังสือเยอะ = เกรดสูง
X = np.array([
    [10, 5], [15, 10], [18, 15], [20, 20], [8, 2], 
    [12, 8], [14, 12], [19, 18], [5, 1], [16, 14]
])
y = np.array([2.5, 3.0, 3.5, 4.0, 2.0, 2.8, 3.2, 3.9, 1.5, 3.4])

# Train โมเดลตอนเริ่มต้นระบบ
model = LinearRegression()
model.fit(X, y)

class PredictInput(BaseModel):
    attendance: int
    study_hours: int

@app.get("/")
def read_root():
    return {"message": "GPA Prediction API is running!"}

@app.post("/predict")
def predict_gpa(data: PredictInput):
    # ป้อนข้อมูลเข้าโมเดลเพื่อทำนาย
    input_data = np.array([[data.attendance, data.study_hours]])
    prediction = model.predict(input_data)[0]
    
    # ควบคุมไม่ให้เกรดเกิน 4.00 หรือต่ำกว่า 0.00
    gpa = float(np.clip(prediction, 0.0, 4.0))
    
    return {"predicted_gpa": round(gpa, 2)}