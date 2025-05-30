# Placeholder for routes.py 

from fastapi import APIRouter, HTTPException, Depends
from .model import AnalysisRequest, AnalysisResponse, FlaggedPhrase, AIModelInput, AIModelOutput
import os
from dotenv import load_dotenv
import openai # OpenAI will be used for now

# Placeholder for keyword detection logic
def detect_keywords(text: str) -> list[str]:
    """
    Simple keyword detection.
    This is a placeholder. In a real application, you'd use more sophisticated NLP.
    """
    # Keywords that might indicate manipulation
    keywords = [
        "you always", "you never", "you're too sensitive", "it's your fault",
        "if you really loved me", "don't be dramatic", "I was just joking",
        "you're imagining things", "everyone knows", "I'm the victim here"
    ]
    found_phrases = []
    # A simple way to find phrases containing keywords
    # This can be improved significantly
    sentences = text.split('.') # Rudimentary sentence splitting
    for sentence in sentences:
        for keyword in keywords:
            if keyword.lower() in sentence.lower():
                found_phrases.append(sentence.strip())
                break # Avoid adding the same sentence multiple times for different keywords
    return list(set(found_phrases)) # Return unique phrases

# --- AI Model Abstraction ---
# This is where you'd define an interface for different AI models.
# For now, we'll directly use OpenAI, but structure it for easy replacement.

async def get_openai_explanation(phrase: str) -> AIModelOutput:
    """
    Gets explanation and severity from OpenAI GPT.
    NOTE: This is where you would swap to other models like Qwen or LLaMA.
    You would create a similar function for each model, e.g., get_qwen_explanation,
    and then have a central function that calls the appropriate one based on configuration.
    """
    load_dotenv() # Load environment variables from .env file (in the backend directory)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not found in environment variables.")

    try:
        # Ensure you have the openai library installed: pip install openai
        # For newer versions of openai library (>=1.0.0)
        client = openai.OpenAI(api_key=api_key)
        completion = await client.chat.completions.create(
            model="gpt-3.5-turbo", # Or your preferred model
            messages=[
                {"role": "system", "content": "You are an expert in identifying and explaining emotionally manipulative language. Analyze the following phrase. Provide a concise explanation of why it might be manipulative and a severity score from 1 (mild) to 5 (severe). Respond in JSON format with keys 'explanation' and 'severity'."},
                {"role": "user", "content": f"Analyze this phrase: \"{phrase}\""}
            ],
            # Ensure the model is instructed or constrained to output valid JSON.
            # For more robust JSON output, consider using response_format={"type": "json_object"} with compatible models.
            # However, for broad compatibility and simplicity here, we'll parse the text response.
        )
        
        response_content = completion.choices[0].message.content
        
        # Attempt to parse the JSON response from the model
        # This part is crucial and might need error handling if the model doesn't strictly adhere to JSON
        import json
        try:
            data = json.loads(response_content)
            explanation = data.get("explanation", "No explanation provided.")
            severity = data.get("severity")
            if not isinstance(severity, int) or not (1 <= severity <= 5):
                severity = 3 # Default severity if parsing fails or value is out of range
        except json.JSONDecodeError:
            explanation = "Failed to parse AI model response. The raw response was: " + response_content
            severity = 3 # Default severity

        return AIModelOutput(explanation=explanation, severity=severity)

    except openai.APIError as e:
        # Handle OpenAI API errors
        print(f"OpenAI API Error: {e}")
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error during AI call: {e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred while contacting the AI model: {str(e)}")


router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Analyzes text to detect and explain emotionally manipulative language.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    # 1. Detect potentially manipulative phrases (simple keyword-based for now)
    flagged_by_keywords = detect_keywords(request.text)

    if not flagged_by_keywords:
        return AnalysisResponse(flagged_phrases=[])

    processed_phrases: list[FlaggedPhrase] = []

    # 2. For each flagged phrase, get AI explanation and severity
    # In a real app, you might want to batch these calls or handle them asynchronously more efficiently.
    for phrase_text in flagged_by_keywords:
        if not phrase_text: # Skip empty strings if any
            continue
        try:
            # This is where you would choose your AI model provider.
            # For now, it directly calls OpenAI.
            # Example for modularity:
            # ai_output = await get_ai_analysis(AIModelInput(text_to_analyze=phrase_text), model_choice="openai")
            # For now, directly:
            ai_model_output = await get_openai_explanation(phrase_text)
            
            processed_phrases.append(
                FlaggedPhrase(
                    phrase=phrase_text,
                    severity_score=ai_model_output.severity,
                    explanation=ai_model_output.explanation
                )
            )
        except HTTPException as e:
            # If a specific call to the AI fails, we can either skip it or return a partial result.
            # For now, let's add a placeholder or log the error and continue.
            print(f"Error processing phrase '{phrase_text}': {e.detail}")
            # Optionally, add a default/error entry for this phrase:
            # processed_phrases.append(
            #     FlaggedPhrase(
            #         phrase=phrase_text,
            #         severity_score=0, # Or some indicator of error
            #         explanation=f"Could not analyze phrase due to error: {e.detail}"
            #     )
            # )
            # For simplicity, we'll just skip a phrase if its analysis fails.
            # Consider how you want to handle partial failures in a production app.
            continue 
        except Exception as e:
            print(f"Unexpected error processing phrase '{phrase_text}': {str(e)}")
            continue


    return AnalysisResponse(flagged_phrases=processed_phrases)

# How to switch to a Hugging Face model (e.g., Qwen or LLaMA) later:
#
# 1. Define a new function similar to `get_openai_explanation`, e.g., `get_huggingface_explanation`.
#    This function would:
#    - Load the desired Hugging Face model (e.g., using `transformers` library).
#      ```python
#      # from transformers import pipeline
#      # nlp_pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", device=0) # device=0 for GPU
#      ```
#    - Format the input prompt for that specific model.
#    - Call the model to get the explanation and severity.
#      (You might need to fine-tune or prompt-engineer the model to output in the desired format, e.g., JSON with 'explanation' and 'severity').
#    - Parse the model's output into your `AIModelOutput` Pydantic model.
#
# 2. Modify the main analysis logic to choose the model:
#    You could use an environment variable or a configuration setting to select the AI provider.
#    ```python
#    # AI_PROVIDER = os.getenv("AI_PROVIDER", "openai") # Default to openai
#
#    # async def get_ai_analysis(input_data: AIModelInput, model_choice: str):
#    #     if model_choice == "openai":
#    #         return await get_openai_explanation(input_data.text_to_analyze)
#    #     elif model_choice == "huggingface_qwen":
#    #         # return await get_qwen_explanation(input_data.text_to_analyze)
#    #         pass # Implement Qwen
#    #     elif model_choice == "huggingface_llama":
#    #         # return await get_llama_explanation(input_data.text_to_analyze)
#    #         pass # Implement Llama
#    #     else:
#    #         raise ValueError("Unsupported AI provider")
#    ```
#
# 3. Update the call in the `/analyze` endpoint:
#    ```python
#    # ai_model_output = await get_ai_analysis(
#    #     AIModelInput(text_to_analyze=phrase_text),
#    #     model_choice=AI_PROVIDER
#    # )
#    ```
#
# Key considerations for Hugging Face models:
# - **Model Hosting**: Running large models locally requires significant computational resources (RAM, VRAM).
#   Alternatively, you can use services like Hugging Face Inference Endpoints, Amazon SageMaker, etc.
# - **Output Formatting**: You'll need to ensure the chosen open-source model can reliably output the explanation and severity score in a parseable format (like JSON). This might involve specific prompting or fine-tuning.
# - **Dependencies**: Add `transformers`, `torch`, etc., to your `requirements.txt`. 