from storage import load_user
from password_tools import check_strength
def security_report():
    print("\n" + "=" * 40)
    print("       SECURITY REPORT")
    print("=" * 40)
    username, password = load_user()
     if username is None:
        print("No account found.")
        return
    strength = check_strength(password)
    print("Username         :", username)
    print("Password Strength :", strength)
    if strength == "Strong":
        print("Security Status   : Good")
