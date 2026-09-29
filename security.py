import random


MAX_ATTEMPTS = 3


def generate_otp():
    return random.randint(100000, 999999)


def verify_otp():
    print("\n--- 2-Step Verification ---")

    otp = generate_otp()

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        print("Your OTP is:", otp)

        entered_otp = input("Enter OTP: ")

        if entered_otp == str(otp):
            print("OTP verification successful!")
            return True

        attempts += 1

        print("Incorrect OTP.")

        if attempts < MAX_ATTEMPTS:
            print(
                "Attempts remaining:",
                MAX_ATTEMPTS - attempts
            )

    print("OTP verification failed.")
    return False
