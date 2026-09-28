import random
MAX_ATTEMPTS = 3
def generate_otp():
    return random.randint(100000, 999999)
def verify_otp():
    print("\n--- 2-Step Verification ---")
    otp = generate_otp()
    print("Your OTP is:", otp)
