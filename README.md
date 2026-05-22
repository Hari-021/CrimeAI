# 🚔 AI Crime Intelligence System

An advanced AI-powered crime complaint management system built using **FastAPI, HTML, CSS, and JavaScript**.

This project allows citizens to submit crime complaints using:

- 🎤 Voice Input
- 📸 Image Upload
- 📍 Address Details

The AI system automatically analyzes complaints and generates FIR details with urgency levels.

---

# 🌟 Features

## ✅ AI Complaint Analysis

The system automatically detects:

### Crime Categories
- Theft
- Assault
- Fraud
- Other

### Urgency Levels
- Critical
- High
- Medium

---

## 🎤 Voice Complaint Support

Users can:

- Click microphone button
- Speak complaint
- Convert speech to text automatically

Uses:
- Web Speech API

---

## 📸 Image Upload Support

Citizens can upload:

- Crime evidence photos
- Screenshots
- Incident images

On mobile devices it shows:

- Camera
- Gallery / Photos

---

## 📍 Address-Based Reporting

Instead of latitude and longitude:

- Simple address input field added
- Easier for citizens to report incidents

---

## 📊 Live Dashboard

Displays:

- Total complaints
- Critical complaints
- Complaint history

---

## 🧠 FIR Generation

The system automatically generates:

- FIR Number
- Category
- Urgency Level

Using AI-based analysis logic.

---

# 🛠️ Technologies Used

## Backend
- FastAPI
- Python
- Uvicorn

## Frontend
- HTML
- CSS
- JavaScript

## AI Features
- NLP-based text analysis
- Voice recognition
- Automated classification

---

# 📂 Project Structure

```bash
AI_Crime_System/
│
├── main.py
├── uploads/
├── README.md


#⚙️ Installation Process

Step 1 — Install Python
Download Python:
https://www.python.org/downloads/
During installation enable:
Add Python to PATH

Step 2 — Clone Repository
git clone https://github.com/your-username/AI-Crime-Intelligence.git

Step 3 — Open Project Folder
cd AI-Crime-Intelligence

Step 4 — Install Dependencies
pip install fastapi uvicorn python-multipart

Step 5 — Run the Project
uvicorn main:app --reload --port 9000

Step 6 — Open in Browser
http://localhost:9000

#🧪 How It Works
1️⃣ User Submits Complaint

The citizen enters:

Complaint description
Address
Optional evidence image

OR

Uses microphone for voice complaint.

2️⃣ AI Analyzes Complaint

The backend:

Detects crime keywords
Classifies crime type
Detects urgency level
3️⃣ FIR Generated

The system generates:

FIR/3891/2024

With category and urgency level.

4️⃣ Dashboard Updates

Live complaint statistics update automatically.

📸 Key Functionalities
🎙️ Speech Recognition

Uses browser speech API:

window.SpeechRecognition
📤 File Upload

Supports:

Camera capture
Gallery upload

Using:

<input type="file" accept="image/*" capture="environment">


#🔮 Future Enhancements

Planned upgrades:

Google Maps Integration
AI Crime Prediction
Heatmap Analytics
Emergency Alerts
Multi-language Support
Facial Recognition
CCTV Integration
Admin Dashboard
PDF FIR Download
Email/SMS Notifications
📈 Use Cases
Smart Policing
Women Safety Systems
Emergency Reporting
Government AI Platforms
Cybercrime Reporting
Public Safety Applications

#👨‍💻 Author
Periketi Hari Krishna
AI & Full Stack Developer

Interested in:
Artificial Intelligence
Crime Analytics
NLP Systems
FastAPI Development
Smart Government Solutions

#⭐ Support
If you like this project:

⭐ Star the repository
🍴 Fork the project
🛠️ Contribute improvements

#📄 License

This project is open-source and available under the MIT License.
