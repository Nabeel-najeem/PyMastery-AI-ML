import re

def clean_resume_text(raw_text: str) -> str:
    """Removes extra spaces, newlines, and special characters from raw resume input."""
    # Replace multiple spaces and newlines with a single space
    cleaned_text = re.sub(r'\s+', ' ', raw_text)
    # Strip leading/trailing whitespace
    return cleaned_text.strip()