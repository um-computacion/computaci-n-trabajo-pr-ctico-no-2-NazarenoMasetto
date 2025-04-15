import string

def clean_text(text):
    allowed = string.ascii_letters + string.digits
    return ''.join(char.lower() for char in text if char.lower() in allowed)

def is_palindrome(text):
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]
