import os
import aiohttp
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Ollama API
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")

async def get_gpt_explanation(phrase: str) -> str:
    """
    Get an explanation from Ollama about why a phrase might be considered abusive or manipulative
    """
    try:
        # Check if Ollama base URL is available
        if not OLLAMA_BASE_URL:
            return "Ollama API not configured. This is a placeholder explanation for why the phrase might be considered harmful or manipulative."
        
        # Create a prompt for Ollama
        prompt = f"""The phrase \"{phrase}\" could be considered manipulative, abusive, or gaslighting. 
        Please provide a brief, empathetic explanation (2-3 sentences) of why this language might be harmful 
        in a relationship or conversation. Focus on how it might make the recipient feel and why it's problematic.
        Keep your response under 150 words and be gentle but clear."""
        
        # Call the Ollama API
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "system": "You are a helpful assistant that explains why certain phrases might be considered manipulative, abusive, or gaslighting in a gentle, empathetic way.",
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 150
                    }
                }
            ) as response:
                # Check if the request was successful
                if response.status == 200:
                    # Extract and return the explanation
                    result = await response.json()
                    explanation = result.get("response", "").strip()
                    return explanation
                else:
                    # Return error message
                    error_text = await response.text()
                    return f"Error calling Ollama API: {response.status} - {error_text}"
    
    except Exception as e:
        # Fallback explanation if API call fails
        return f"This phrase may be considered harmful because it could invalidate someone's feelings or experiences. It's important to use language that respects others' perspectives and emotions. (Error: {str(e)})"