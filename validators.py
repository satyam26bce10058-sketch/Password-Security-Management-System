def validate_username(username):
    if username == "":
        return False, "Username cannot be empty."
    if len(username) < 3:
        return False, "Username must contain at least 3 characters."
    if " " in username:
        return False, "Username cannot contain spaces."
    return True, "Valid username."
def validate_password(password):
    if len(password) < 8:
        return False, "Password must contain at least 8 characters."
    return True, "Valid password."
def validate_length(value):
    try:
        number = int(value)
        if number < 8:
            return False, "Length must be at least 8."
        return True, number
    except ValueError:
        return False, "Please enter a valid number."
