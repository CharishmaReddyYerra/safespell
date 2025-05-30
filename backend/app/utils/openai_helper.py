import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

async def get_gpt_explanation(phrase: str) -> str:
    """
    Get an explanation from GPT about why a phrase might be considered abusive or manipulative
    """
    try:
        # Check if API key is available
        if not openai.api_key:
            return "API key not configured. This is a placeholder explanation for why the phrase might be considered harmful or manipulative."
        
        # Create a prompt for GPT
        prompt = f"""The phrase \"{phrase}\" could be considered manipulative, abusive, or gaslighting. 
        Please provide a brief, empathetic explanation (2-3 sentences) of why this language might be harmful 
        in a relationship or conversation. Focus on how it might make the recipient feel and why it's problematic.
        Keep your response under 150 words and be gentle but clear."""
        
        # Call the OpenAI API
        response = await openai.ChatCompletion.acreate(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains why certain phrases might be considered manipulative, abusive, or gaslighting in a gentle, empathetic way."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        # Extract and return the explanation
        explanation = response.choices[0].message.content.strip()
        return explanation
    
    except Exception as e:
        # Fallback explanation if API call fails
        return f"This phrase may be considered harmful because it could invalidate someone's feelings or experiences. It's important to use language that respects others' perspectives and emotions."