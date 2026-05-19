from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

complaints = []

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
    return {"category": category, "urgency": urgency, "fir": fir}

@app.post("/api/complaints/submit", response_model=dict)
async def submit(text_content=Form(...), latitude=Form(...), longitude=Form(...)):
    result = analyze(text_content)
    complaints.append({"id": len(complaints)+1, "text": text_content, "category": result["category"], "urgency": result["urgency"], "fir": result["fir"]})
    return {"status": "success", "category": result["category"], "urgency": result["urgency"], "fir": result["fir"]}

@app.get("/api/complaints")
async def get_complaints():
    return complaints[::-1]

@app.get("/api/statistics")
async def get_stats():
    return {"total": len(complaints), "critical": len([c for c in complaints if c["urgency"]=="CRITICAL"])}

@app.get("/", response_class=HTMLResponse)
async def home():
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Crime System</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Segoe UI;background:linear-gradient(135deg,#1a1a2e,#16213e);min-height:100vh;color:#fff}
header{background:linear-gradient(90deg,#00d2ff,#3a7bd5);padding:20px;text-align:center}
.container{max-width:1000px;margin:0 auto;padding:20px}
.stats{display:flex;gap:20px;margin:20px 0}
.stat{background:rgba(255,255,255,0.1);padding:20px;border-radius:10px;flex:1;text-align:center}
.stat .num{font-size:2.5rem;font-weight:bold}
.main{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.card{background:rgba(255,255,255,0.1);padding:20px;border-radius:15px}
h2{color:#00d2ff;border-bottom:2px solid #00d2ff;padding-bottom:10px}
input,textarea{width:100%;padding:12px;margin:10px 0;border:2px solid rgba(255,255,255,0.2);border-radius:8px;background:rgba(255,255,255,0.1);color:#fff}
button{width:100%;padding:15px;background:linear-gradient(90deg,#00d2ff,#3a7bd5);color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer}
.result{margin-top:15px;padding:15px;background:#11998e;border-radius:8px;display:none}
.result.show{display:block}
</style>
</head>
<body>
<header><h1>🚔 AI Crime Intelligence</h1><p>Government-Grade AI</p></header>
<div class="container">
<div class="stats">
<div class="stat"><div class="num" id="total">0</div><div>Total</div></div>
<div class="stat"><div class="num" id="critical">0</div><div>Critical</div></div>
</div>
<div class="main">
<div class="card"><h2>Submit Complaint</h2>
<form id="form"><input id="desc" placeholder="Describe what happened..."><input id="lat" value="28.6"><input id="lng" value="77.2"><button>Submit</button></form>
<div class="result" id="result"><h3>Done!</h3><p>FIR: <b id="fir"></b></p><p>Category: <b id="cat"></b></p></div></div>
<div class="card"><h2>Complaints</h2><div id="list"></div></div>
</div>
</div>
<script>
const url=window.location.origin;
async function sub(e){e.preventDefault();const fd=new URLSearchParams();fd.append("text_content",document.getElementById("desc").value);fd.append("latitude",document.getElementById("lat").value);fd.append("longitude",document.getElementById("lng").value);
const r=await fetch(url+"/api/complaints/submit",{method:"POST",body:fd});const d=await r.json();
document.getElementById("fir").innerText=d.fir;document.getElementById("cat").innerText=d.category;document.getElementById("result").classList.add("show");load();}
async function load(){const r=await fetch(url+"/api/complaints");const d=await r.json();
document.getElementById("list").innerHTML=d.map(c=>"<div style='padding:10px;border-bottom:1px solid #fff'>#"+c.id+" "+c.category+" <b>"+c.urgency+"</b></div>").join("");
document.getElementById("total").innerText=d.length;document.getElementById("critical").innerText=d.filter(c=>c.urgency=="CRITICAL").length;}
document.getElementById("form").onsubmit=sub;load();
</script>
</body>
</html>"""
    return html

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)