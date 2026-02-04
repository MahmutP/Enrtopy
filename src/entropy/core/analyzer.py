import string
from typing import Dict, List, Any

def analyze_password(password: str) -> Dict[str, Any]:
    """
    Analyzes the strength of a given password.
    
    Args:
        password (str): The password to analyze.
        
    Returns:
        dict: A dictionary containing score, status, color, pros, and cons.
    """
    score = 0
    pros: List[str] = []
    cons: List[str] = []
    
    # Length Analysis
    length = len(password)
    if length >= 20: 
        score += 40
        pros.append("Exceptional Length (Passphrase?)")
    elif length >= 16: 
        score += 30
        pros.append("Excellent Length")
    elif length >= 12: 
        score += 20
        pros.append("Good Length")
    else: 
        cons.append("Short Length (< 12 chars)")

    # Character Set Analysis
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if has_upper: 
        score += 10
        pros.append("Uppercase Characters")
    else:
        cons.append("No Uppercase")
        
    if has_lower: 
        score += 10
        pros.append("Lowercase Characters")
    else:
        cons.append("No Lowercase")
        
    if has_digit: 
        score += 20
        pros.append("Numbers")
    else:
        cons.append("No Numbers")
        
    if has_symbol: 
        score += 20
        pros.append("Special Symbols")
    else:
        cons.append("No Symbols")
    
    # Pattern/Entropy Bonus
    separators = "-_."
    if any(sep in password for sep in separators):
        score += 10
        pros.append("Good Separation")

    # Final Score Calculation
    score = min(max(score, 0), 100)

    # Status Determination
    if score >= 90:
        color = "bright_green"
        status = "SECURE"
    elif score >= 60:
        color = "yellow"
        status = "MODERATE"
    else:
        color = "red"
        status = "VULNERABLE"

    return {
        "score": score,
        "color": color,
        "status": status,
        "pros": pros,
        "cons": cons
    }
