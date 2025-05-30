from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv

from app.models.abusive_language import analyze_text, get_abusive_phrases
from app.utils.ollama_helper import get_gpt_explanation

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="SAFESPELL API",
    description="API for detecting abusive, coercive, or manipulative language in text",
    version="1.0.0"
)

# Configure CORS
origins = eval(os.getenv("API_CORS_ORIGINS", "[\"http://localhost:3000\"]"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and Response Models
class TextAnalysisRequest(BaseModel):
    text: str

class FlaggedPhrase(BaseModel):
    phrase: str
    start_index: int
    end_index: int
    explanation: str

class TextAnalysisResponse(BaseModel):
    flagged_phrases: List[FlaggedPhrase]
    severity_score: int
    original_text: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to SAFESPELL API"}

@app.post("/analyze", response_model=TextAnalysisResponse)
async def analyze_text_endpoint(request: TextAnalysisRequest):
    try:
        # Get the text from the request
        text = request.text
        
        if not text or len(text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        # Find abusive phrases in the text
        abusive_phrases = get_abusive_phrases(text)
        
        # Calculate severity score (1-5)
        severity_score = min(5, max(1, len(abusive_phrases) + 1)) if abusive_phrases else 1
        
        # Get GPT explanations for each phrase
        flagged_phrases = []
        for phrase_info in abusive_phrases:
            explanation = await get_gpt_explanation(phrase_info["phrase"])
            flagged_phrases.append(
                FlaggedPhrase(
                    phrase=phrase_info["phrase"],
                    start_index=phrase_info["start_index"],
                    end_index=phrase_info["end_index"],
                    explanation=explanation
                )
            )
        
        return TextAnalysisResponse(
            flagged_phrases=flagged_phrases,
            severity_score=severity_score,
            original_text=text
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
        reload=True
    )