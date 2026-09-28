def validate_username(username):
    if username == "":
        return False, "Username cannot be empty."
    if len(username) < 3:
        return False, "Username must contain at least 3 characters."
    if " " in username:
        return False, "Username cannot contain spaces."
    return True, "Valid username."
