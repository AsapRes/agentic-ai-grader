from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/evaluate")
async def evaluate_transcript(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    
    # Placeholder for your actual rubric evaluation logic
    response = {
        "candidate_score": 78,
        "rubric_match": {
            "communication_skills": 16,
            "problem_solving": 14,
            "domain_knowledge": 18,
            "confidence": 15,
            "cultural_fit": 15,
        },
        "verdict": "Strong candidate with good potential",
        "feedback": "Good interview performance. Could improve clarity in responses."
    }

    return JSONResponse(content=response)
