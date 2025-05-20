from langdetect import detect
import re

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
