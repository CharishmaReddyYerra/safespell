# Placeholder for main.py 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as api_router
import uvicorn

app = FastAPI(
    title="SAFESPELL API",
    description="API for detecting and explaining emotionally manipulative language.",
    version="0.1.0"
)

# Configure CORS
origins = [
    "http://localhost:3000",  # Allow your React frontend
    "http://localhost:5173",  # Allow your React frontend (vite)
    # Add any other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SAFESPELL API"}

# Include the API router
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 