from typing import List, Dict, Any
import re

# List of potentially abusive, manipulative, or gaslighting phrases
ABUSIVE_PHRASES = [
    "you're overreacting",
    "you're too sensitive",
    "you're crazy",
    "you're imagining things",
    "no one will believe you",
    "you're making things up",
    "you're remembering it wrong",
    "that never happened",
    "you're being dramatic",
    "you're being irrational",
    "you're being hysterical",
    "you need help",
    "you're the problem",
    "if you really loved me",
    "you made me do this",
    "look what you made me do",
    "i'm the only one who cares about you",
    "no one else will love you",
    "you're nothing without me",
    "you'll never find anyone better",
    "you're worthless",
    "you're useless",
    "you deserve this",
    "this is your fault",
    "you brought this on yourself",
    "you're too emotional",
    "you always exaggerate",
    "you never listen",
    "you always make everything about you",
    "you're being selfish",
    "you're being childish",
    "you should know better",
    "i'm just trying to help you",
    "i'm doing this for your own good",
    "you're lucky to have me",
    "i'm the best you'll ever get",
    "you owe me",
    "after all i've done for you",
    "you're ungrateful",
    "you're impossible to talk to",
    "you're impossible to please",
    "you're always complaining",
    "you're never satisfied",
    "you're always negative",
    "you're always causing problems",
    "you're embarrassing me",
    "you're making a scene",
    "everyone agrees with me",
    "nobody likes you",
    "everyone thinks you're",
    "you should be ashamed",
]

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyze text for abusive language and return analysis results
    """
    abusive_phrases = get_abusive_phrases(text)
    severity_score = min(5, max(1, len(abusive_phrases) + 1)) if abusive_phrases else 1
    
    return {
        "flagged_phrases": abusive_phrases,
        "severity_score": severity_score,
        "original_text": text
    }

def get_abusive_phrases(text: str) -> List[Dict[str, Any]]:
    """
    Find abusive phrases in the text and return their positions
    """
    text_lower = text.lower()
    results = []
    
    for phrase in ABUSIVE_PHRASES:
        for match in re.finditer(r'\b' + re.escape(phrase) + r'\b', text_lower):
            start_index = match.start()
            end_index = match.end()
            original_phrase = text[start_index:end_index]
            
            results.append({
                "phrase": original_phrase,
                "start_index": start_index,
                "end_index": end_index
            })
    
    return results