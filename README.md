# GPA Predictor using Docker Compose

โปรเจกต์นี้เป็นระบบ Web Application สำหรับทำนายเกรดเฉลี่ย (GPA) โดยใช้ Machine Learning (Linear Regression) ทำงานร่วมกันแบบ Containerized ด้วย Docker Compose

## รายละเอียดระบบ
ระบบแบ่งการทำงานออกเป็น 2 ส่วนหลัก:
1. **Backend (FastAPI):** ทำหน้าที่เป็น API Server ประมวลผลโมเดล Machine Learning
2. **Frontend (Streamlit):** ส่วนติดต่อผู้ใช้ (UI) สำหรับกรอกข้อมูลและแสดงผลลัพธ์

## เทคโนโลยีที่ใช้
- Docker & Docker Compose
- Python 3.10
- FastAPI (Backend)
- Streamlit (Frontend)
- Scikit-learn (Machine Learning Model)

## วิธีการใช้งาน
1. ตรวจสอบให้แน่ใจว่าติดตั้ง Docker Desktop เรียบร้อยแล้ว
2. โคลนโปรเจกต์นี้ลงเครื่อง:
   git clone [ใส่ลิงก์ GitHub ของคุณที่นี่]
   cd gpa-predictor
3. สั่งรันระบบ:
   docker compose up

4. เข้าใช้งานผ่าน Browser:
   - หน้าเว็บ: http://localhost:8502
   - API Documentation: http://localhost:8765/docs

## โครงสร้างโปรเจกต์
- backend/: Source Code API และ Dockerfile
- frontend/: Source Code ของหน้าเว็บและ Dockerfile
- docker-compose.yml: ไฟล์สำหรับจัดการ Container ทั้งหมด