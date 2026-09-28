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
    if not any(c.isupper() for c in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(c.islower() for c in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add at least one number.")
    if not any(c in SPECIAL_CHARACTERS for c in password):
        suggestions.append("Add at least one special character.")
    return suggestions
def generate_password(length):
    if length < 8:
        return None
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    special = SPECIAL_CHARACTERS
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers),
        random.choice(special)
    ]
    all_characters = lower + upper + numbers + special
    for i in range(length - 4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return "".join(password)
