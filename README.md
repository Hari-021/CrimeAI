**Project Description**


🚀 Government-Grade AI System for Real-Time Crime Detection, Classification, and FIR Generation

A full-stack intelligent crime reporting system that uses NLP and Machine Learning to:
- Automatically classify crime categories from complaint text
- Predict urgency levels based on severity keywords
- Detect fake/frivolous complaints
- Generate FIR numbers automatically
- Track crime hotspots using geo-location data
- Provide real-time statistics and analytics


**Features**


✓ NLP-based crime category detection (Theft, Assault, Fraud, Harassment, Accident)
✓ Urgency prediction (Critical, High, Medium, Low)
✓ Fake complaint detection using keyword analysis
✓ Auto-generated FIR numbers
✓ SQLite database for persistent storage
✓ RESTful API with FastAPI
✓ Responsive UI with vanilla HTML/CSS/JS
✓ Real-time statistics dashboard
✓ Crime hotspot tracking


**Tech Stack**


Backend:   Python, FastAPI, SQLAlchemy, SQLite
Frontend: HTML5, CSS3, JavaScript (Vanilla)
AI/ML:    Natural Language Processing, Keyword-based Classification


**How It Works**


1. Citizen submits complaint via text
2. AI analyzes the text using NLP
3. System detects crime category
4. Urgency level is predicted
5. FIR number is auto-generated
6. Complaint is saved to database
7. Statistics are updated in real-time


**API End points**


POST /api/complaints/submit  - Submit new complaint
GET  /api/complaints         - Get all complaints
GET  /api/statistics        - Get system statistics
GET  /                      - Web dashboard


**Sample Request**



curl -X POST "http://localhost:8000/api/complaints/submit" \
  -d "text_content=Someone+stole+my+wallet&latitude=28.6139&longitude=77.2090"


**Sample Response**

json

{
  "status": "success",
  "category": "THEFT",
  "urgency": "MEDIUM",
  "fir": "FIR/4523/2024"
}


**To Run Locally**

bash

# Install dependencies
pip install fastapi uvicorn sqlalchemy

# Run the server
python app.py

# Open in browser
http://localhost:8000


**Author**
Periketi Hari Krishna

**GitHub**: github.com/Hari-021
**Email**: periketi.hari54@gmail.com

