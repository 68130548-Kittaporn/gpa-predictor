import streamlit as st
import requests

st.title("GPA Predictor")
st.write("กรอกข้อมูลเพื่อประเมินเกรดเฉลี่ยด้วย Machine Learning")

attendance = st.number_input("จำนวนครั้งที่เข้าเรียน (0 - 20 ครั้ง):", min_value=0, max_value=20, value=15)
study_hours = st.number_input("จำนวนชั่วโมงที่อ่านหนังสือ/สัปดาห์ (0 - 30 ชั่วโมง):", min_value=0, max_value=30, value=10)

if st.button("ทำนายผลเกรดเฉลี่ย"):
    payload = {
        "attendance": attendance,
        "study_hours": study_hours
    }
    
    try:
        response = requests.post("http://backend:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            predicted_gpa = result["predicted_gpa"]
            
            st.success(f"เกรดเฉลี่ยที่คาดว่าจะได้รับ: {predicted_gpa}")
        else:
            st.error("เกิดข้อผิดพลาดจากระบบ Backend")
    except Exception as e:
        st.error(f"ไม่สามารถเชื่อมต่อกับ Backend ได้: {e}")