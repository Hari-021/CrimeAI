from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

complaints = []

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- AI ANALYSIS ---------------- #
def analyze(text):
    text_lower = text.lower()

    if "stolen" in text_lower or "theft" in text_lower:
        category = "THEFT"
    elif "attack" in text_lower or "beat" in text_lower:
        category = "ASSAULT"
    elif "fraud" in text_lower or "scam" in text_lower:
        category = "FRAUD"
    else:
        category = "OTHER"

    if "murder" in text_lower or "fire" in text_lower or "death" in text_lower:
        urgency = "CRITICAL"
    elif "robbery" in text_lower or "attack" in text_lower:
        urgency = "HIGH"
    else:
        urgency = "MEDIUM"

    import random
    fir = f"FIR/{random.randint(1000,9999)}/2024"

    return {
        "category": category,
        "urgency": urgency,
        "fir": fir
    }


# ---------------- SUBMIT API ---------------- #
@app.post("/api/complaints/submit")
async def submit(
    text_content=Form(...),
    address=Form(...),
    image: UploadFile = File(None)
):

    result = analyze(text_content)

    filename = ""

    # Save uploaded image
    if image:
        filename = image.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        with open(file_path, "wb") as f:
            f.write(await image.read())

    complaints.append({
        "id": len(complaints) + 1,
        "text": text_content,
        "address": address,
        "image": filename,
        "category": result["category"],
        "urgency": result["urgency"],
        "fir": result["fir"]
    })

    return {
        "status": "success",
        "category": result["category"],
        "urgency": result["urgency"],
        "fir": result["fir"]
    }


# ---------------- GET COMPLAINTS ---------------- #
@app.get("/api/complaints")
async def get_complaints():
    return complaints[::-1]


# ---------------- STATS ---------------- #
@app.get("/api/statistics")
async def get_stats():
    return {
        "total": len(complaints),
        "critical": len([c for c in complaints if c["urgency"] == "CRITICAL"])
    }


# ---------------- FRONTEND ---------------- #
@app.get("/", response_class=HTMLResponse)
async def home():

    html = """
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>AI Crime System</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
font-family:Segoe UI;
background:linear-gradient(135deg,#1a1a2e,#16213e);
min-height:100vh;
color:#fff;
}

header{
background:linear-gradient(90deg,#00d2ff,#3a7bd5);
padding:20px;
text-align:center;
}

.container{
max-width:1000px;
margin:auto;
padding:20px;
}

.stats{
display:flex;
gap:20px;
margin:20px 0;
}

.stat{
background:rgba(255,255,255,0.1);
padding:20px;
border-radius:12px;
flex:1;
text-align:center;
}

.stat .num{
font-size:2.5rem;
font-weight:bold;
}

.main{
display:grid;
grid-template-columns:1fr 1fr;
gap:20px;
}

.card{
background:rgba(255,255,255,0.1);
padding:20px;
border-radius:15px;
}

h2{
color:#00d2ff;
border-bottom:2px solid #00d2ff;
padding-bottom:10px;
margin-bottom:15px;
}

.input-box{
position:relative;
margin-bottom:15px;
}

.input-box textarea,
.input-box input{
width:100%;
padding:14px;
border-radius:10px;
border:2px solid rgba(255,255,255,0.2);
background:rgba(255,255,255,0.1);
color:white;
font-size:15px;
outline:none;
}

textarea{
height:120px;
resize:none;
}

.mic-btn{
position:absolute;
right:10px;
top:10px;
background:#00d2ff;
border:none;
width:40px;
height:40px;
border-radius:50%;
cursor:pointer;
font-size:18px;
}

.upload-box{
margin-top:10px;
}

.upload-box input{
background:rgba(255,255,255,0.1);
padding:10px;
border-radius:10px;
}

button.submit-btn{
width:100%;
padding:15px;
background:linear-gradient(90deg,#00d2ff,#3a7bd5);
border:none;
border-radius:10px;
font-size:16px;
color:white;
cursor:pointer;
margin-top:10px;
}

.result{
margin-top:15px;
padding:15px;
background:#11998e;
border-radius:10px;
display:none;
}

.result.show{
display:block;
}

.complaint{
padding:12px;
border-bottom:1px solid rgba(255,255,255,0.2);
}

</style>
</head>

<body>

<header>
<h1>🚔 AI Crime Intelligence</h1>
<p>Government-Grade AI</p>
</header>

<div class="container">

<div class="stats">

<div class="stat">
<div class="num" id="total">0</div>
<div>Total</div>
</div>

<div class="stat">
<div class="num" id="critical">0</div>
<div>Critical</div>
</div>

</div>

<div class="main">

<!-- LEFT -->

<div class="card">

<h2>Submit Complaint</h2>

<form id="form">

<!-- Complaint Text -->

<div class="input-box">

<textarea id="desc"
placeholder="Describe what happened..."></textarea>

<button type="button"
class="mic-btn"
onclick="startVoice()">
🎤
</button>

</div>

<!-- Address -->

<div class="input-box">
<input id="address"
placeholder="Enter Address">
</div>

<!-- Upload -->

<div class="upload-box">

<label>📸 Upload Evidence</label><br><br>

<input type="file"
id="photo"
accept="image/*"
capture="environment">

</div>

<button class="submit-btn">
Submit Complaint
</button>

</form>

<div class="result" id="result">

<h3>Complaint Submitted!</h3>

<p>FIR: <b id="fir"></b></p>

<p>Category: <b id="cat"></b></p>

<p>Urgency: <b id="urg"></b></p>

</div>

</div>

<!-- RIGHT -->

<div class="card">

<h2>Complaints</h2>

<div id="list"></div>

</div>

</div>

</div>

<script>

const url = window.location.origin;


// ---------------- SPEECH TO TEXT ---------------- //

function startVoice(){

const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;

if(!SpeechRecognition){
alert("Speech Recognition not supported");
return;
}

const recognition = new SpeechRecognition();

recognition.lang = "en-US";

recognition.start();

recognition.onresult = function(event){

document.getElementById("desc").value =
event.results[0][0].transcript;

};

}


// ---------------- SUBMIT ---------------- //

async function sub(e){

e.preventDefault();

const fd = new FormData();

fd.append(
"text_content",
document.getElementById("desc").value
);

fd.append(
"address",
document.getElementById("address").value
);

const file =
document.getElementById("photo").files[0];

if(file){
fd.append("image", file);
}

const r = await fetch(
url + "/api/complaints/submit",
{
method:"POST",
body:fd
}
);

const d = await r.json();

document.getElementById("fir").innerText = d.fir;

document.getElementById("cat").innerText = d.category;

document.getElementById("urg").innerText = d.urgency;

document.getElementById("result").classList.add("show");

load();

}


// ---------------- LOAD COMPLAINTS ---------------- //

async function load(){

const r = await fetch(url + "/api/complaints");

const d = await r.json();

document.getElementById("list").innerHTML =
d.map(c => `
<div class="complaint">
#${c.id}
<b>${c.category}</b>
${c.urgency}
<br>
<small>${c.address}</small>
</div>
`).join("");


document.getElementById("total").innerText =
d.length;

document.getElementById("critical").innerText =
d.filter(c => c.urgency=="CRITICAL").length;

}

document.getElementById("form").onsubmit = sub;

load();

</script>

</body>
</html>
"""

    return html


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)