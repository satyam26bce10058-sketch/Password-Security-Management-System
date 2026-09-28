from password_tools import check_strength
from password_tools import password_suggestions
from validators import validate_username
from validators import validate_password
from storage import save_user
from storage import load_user
from storage import update_user
from security import verify_otp
def create_account():
    print("\n--- CREATE ACCOUNT ---")
    username = input("Enter username: ").strip()
    valid, message = validate_username(username)
    if not valid:
        print(message)
        return
    while True:
        password = input("Enter password: ")
        valid, message = validate_password(password)
        if not valid:
            print(message)
            continue
        strength = check_strength(password)
        print("Password Strength:", strength)
        if strength == "Weak":
            print("\nPassword is too weak.")
            suggestions = password_suggestions(password)
            for suggestion in suggestions:
                print("-", suggestion)
            continue
        break
    save_user(username, password)
    print("\nAccount created successfully!")
def login():
    print("\n--- LOGIN ---")
    username, password = load_user()
    if username is None:
        print("No account found.")
        print("Please create an account first.")
        return False
    attempts = 3
    while attempts > 0:
        entered_username = input("Username: ")
        entered_password = input("Password: ")
        if (
            entered_username == username
            and entered_password == password
        ):
             print("\nPassword correct!")
            if verify_otp():
                print(
                    "Login successful! Welcome,",
                    username
                )
                return True
            else:
                print("Login failed.")
                return False
        else:
            attempts -= 1
            print("\nIncorrect username or password.")
            if attempts > 0:
                print("Attempts remaining:", attempts)
    print("\nAccount temporarily locked.")
    return False
def change_password():
    print("\n--- CHANGE PASSWORD ---")
    username, old_password = load_user()
    if username is None:
        print("No account found.")
        return
    entered_old = input("Enter current password: ")
    if entered_old != old_password:
        print("Incorrect current password.")
        return
    while True:
        new_password = input("Enter new password: ")
        valid, message = validate_password(new_password)
        if not valid:
            print(message)
            continue
        strength = check_strength(new_password)
        print("New Password Strength:", strength)
        if strength == "Weak":
            print("Please choose a stronger password.")
            continue
        break
    update_user(username, new_password)
    print("Password changed successfully!")
def account_information():
    print("\n--- ACCOUNT INFORMATION ---")
    username, password = load_user()
    if username is None:
        print("No account exists.")
        return
    print("Username:", username)
    print("Password Strength:", check_strength(password))
