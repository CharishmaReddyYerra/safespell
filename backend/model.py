from pydantic import BaseModel, Field
from typing import List, Optional

class AnalysisRequest(BaseModel):
    text: str = Field(..., example="Person A: I felt really uncomfortable when you said that yesterday.\nPerson B: I never said that. You're always imagining things and being too sensitive.")

class FlaggedPhrase(BaseModel):
    phrase: str
    severity_score: int = Field(..., ge=1, le=5)
    explanation: str

class AnalysisResponse(BaseModel):
    flagged_phrases: List[FlaggedPhrase]
    # Optional: Add an overall summary or score if needed later
    # overall_summary: Optional[str] = None 

# Example of how you might structure input for different AI models later
class AIModelInput(BaseModel):
    text_to_analyze: str
    # You could add model-specific parameters here, e.g.:
    # model_name: Optional[str] = "gpt-3.5-turbo"
    # max_tokens: Optional[int] = 150

class AIModelOutput(BaseModel):
    explanation: str
    severity: int 