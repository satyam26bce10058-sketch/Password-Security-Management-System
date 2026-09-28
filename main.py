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
