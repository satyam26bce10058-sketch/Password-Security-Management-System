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
