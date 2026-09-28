import random
import string
SPECIAL_CHARACTERS = "!@#$%^&*()_+-="
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SPECIAL_CHARACTERS for c in password):
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
def password_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
