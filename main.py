from account import (
    create_account,
    login,
    change_password,
    account_information
)
from password_tools import (
    check_strength,
    generate_password,
    password_suggestions
)
from validators import validate_length
from report import security_report
def password_checker():
    print("\n--- PASSWORD STRENGTH CHECKER ---")
    password = input("Enter password: ")
    strength = check_strength(password)
    print("\nPassword Strength:", strength)
    suggestions = password_suggestions(password)
    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Password meets all basic requirements.")
def password_generator():
    print("\n--- PASSWORD GENERATOR ---")
    while True:
        value = input(
            "Enter password length (minimum 8): "
        )
        valid, result = validate_length(value)
        if not valid:
            print(result)
            continue
        length = result
        break
    password = generate_password(length)
    print("\nGenerated Password:", password)
    print(
        "Strength:",
        check_strength(password)
    )
