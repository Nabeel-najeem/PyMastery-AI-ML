import re

def clean_resume_text(raw_text: str) -> str:
    """Removes extra spaces, newlines, and special characters from raw resume input."""
    # Replace multiple spaces and newlines with a single space
    cleaned_text = re.sub(r'\s+', ' ', raw_text)
    # Strip leading/trailing whitespace
    return cleaned_text.strip()

def estimate_token_count(text: str) -> int:
    """Provides a rough estimate of words/tokens to enforce Freemium tier limits."""
    if not text:
        return 0
    # A simple split by space gives a fast, reliable word count
    words = text.split(' ')
    return len(words)