Password Security Management System

1. Project Overview

The Password Security Management System is a beginner-level Python project that I created to practice the concepts I learned in my Python Essentials course.

It is a command-line application for basic password management and account security. The user can check password strength, generate a password, create an account, log in, change the password, and view a simple security report.

The project also includes input validation, file handling, OTP verification, and unit testing.

Note: This project is made for educational purposes. It is not intended to be used as a real password management or security system.

2. Objectives

The main objectives of this project are:

Check whether a password is Weak, Medium, or Strong.
Give suggestions for improving a weak password.
Generate a password based on the length entered by the user.
Create and manage a basic user account.
Provide a simple login system with OTP verification.
Allow the user to change the password.
Display basic account security information.
Practice using functions and separate Python modules.
Practice file handling and input validation.
Learn how to write and run basic unit tests.

3. Features

3.1 Password Management

The password management part of the project provides the following features:

Check password strength.
Get suggestions for improving a password.
Generate passwords.
Validate password length.

3.2 Account Management

The account management part provides the following features:

Create an account.
Log in.
Verify username and password.
Change password.
View account information.

3.3 Security and Reporting

The security and reporting part provides the following features:

OTP verification.
Maximum 3 OTP attempts.
Maximum 3 login attempts.
Basic security report.
Password strength status.

3.4 Testing

The project includes tests using Python's built-in unittest module.

There are currently 10 tests in total.

There are 4 password-related tests and 6 validation-related tests.

4. Main Functional Modules

The project can be divided into three main functional areas.

4.1 Password Management

This part handles password-related operations such as checking password strength, giving suggestions, generating passwords, and validating password length.

The main files used are password_tools.py and validators.py.

4.2 Account Management

This part handles creating an account, logging in, changing the password, and viewing account information.

The main file used is account.py.

4.3 Security and Reporting

This part handles OTP verification, login attempt control, and generating a simple security report.

The main files used are security.py and report.py.

5. Technologies and Python Concepts Used

5.1 Tools

Python 3
Git
GitHub
Command Prompt / Terminal

5.2 Python Concepts

During this project, I used and practiced the following Python concepts:

Variables
Strings
Boolean values
Lists
Tuples
Conditional statements
if-else statements
while loops
for loops
Functions
User-defined modules
File handling
Exception handling
String methods
Built-in functions
unittest

6. Project Structure

The project is organized into separate folders and Python files.

6.1 Main Program Files

main.py is responsible for displaying the main menu and controlling the program workflow.

account.py handles account creation, login, password change, and account information.

password_tools.py handles password strength checking, password suggestions, and password generation.

security.py handles OTP generation and verification.

storage.py handles saving and loading account information.

validators.py handles username, password, and password length validation.

report.py generates the basic security report.

6.2 Testing Files

The tests folder contains the unit tests used for the project.

test_password.py contains tests for password-related functions.

test_validators.py contains tests for validation functions.

6.3 Data File

The data folder contains users.txt.

The users.txt file stores the current account information used by the program.

6.4 Documentation Files

README.md contains information about the project, features, installation, usage, and testing.

statement.md contains the problem statement, scope, target users, and high-level features.

7. Requirements

To run this project, you need Python 3 installed on your computer.

No external Python libraries are required.

Git is only needed if you want to clone or manage the project using Git.

8. How to Run

8.1 Step 1: Download the Project

Download the project from GitHub or clone the repository.

8.2 Step 2: Open the Project Folder

Open Command Prompt or Terminal in the project folder.

8.3 Step 3: Start the Program

Run the following command:

python main.py

The program will display the main menu.

The available options are:

Create Account

Login

Check Password Strength

Generate Password

Change Password

Account Information

Security Report

Exit

Enter the number of the option you want to use.

9. How to Run the Tests

The project uses Python's built-in unittest module.

9.1 Password Tests

Run the following command:

python -m unittest tests.test_password

The password test file contains 4 tests.

The expected result is that all 4 tests pass successfully.

9.2 Validation Tests

Run the following command:

python -m unittest tests.test_validators

The validation test file contains 6 tests.

The expected result is that all 6 tests pass successfully.

9.3 Test Summary

The project contains 10 automated tests in total.

There are 4 password tests and 6 validation tests.

All 10 tests were successfully run on my local computer.

10. Input Validation and Error Handling

The program checks several types of invalid input.

Empty usernames are rejected.

Usernames shorter than 3 characters are rejected.

Usernames containing spaces are rejected.

Passwords shorter than 8 characters are rejected.

Password generator lengths below 8 are rejected.

Non-numeric password lengths are handled.

Incorrect login details are rejected.

Incorrect OTP entries are handled.

The program displays a message when the user enters invalid information and asks for valid input where appropriate.

11. Non-Functional Requirements

11.1 Usability

The project uses a simple numbered command-line menu, making it easy to understand and operate.

11.2 Performance

The program works with a small amount of data and performs simple operations such as password checking and reading or writing a text file. These operations are suitable for the intended educational use of the project.

11.3 Security

The project includes basic security-related features such as password strength checking, login attempt limits, and OTP verification.

However, passwords are stored as plain text because this is a beginner educational project. Password hashing and encryption are outside the current scope.

11.4 Reliability

The program uses input validation and basic error handling to reduce problems caused by invalid user input.

11.5 Maintainability

The code is divided into separate Python files. Each file has a specific responsibility, which makes the project easier to understand and modify.

11.6 Error Handling

The program handles common invalid inputs such as invalid password length, non-numeric password length, invalid username, incorrect login credentials, and incorrect OTP entries.

12. User Workflow

The user first starts the program and reaches the main menu.

From the main menu, the user can choose to create an account, log in, check password strength, generate a password, change the password, view account information, generate a security report, or exit the program.

When creating an account, the user enters a username and password. The program validates the username and password and checks the password strength before saving the account information.

When logging in, the user enters the username and password. If the details are correct, the program asks for an OTP. The user must enter the correct OTP to complete the login.

The user can also check the strength of any password without creating an account.

The password generator allows the user to enter a desired password length and generates a password containing different types of characters.

The change password option allows the user to enter the current password and then create a new password.

The account information option displays the username and current password strength.

The security report displays the username, password strength, and a basic security status.

The user can exit the application by selecting the Exit option from the main menu.

13. Testing Results

I tested the project using Python's built-in unittest module.

The password tests completed successfully with 4 tests passed.

The validation tests completed successfully with 6 tests passed.

A total of 10 tests passed successfully.

The tests were run locally before preparing the project for submission.

14. Limitations

Since this is a beginner-level educational project, it has some limitations.

Account information is stored in a text file.

Passwords are stored as plain text.

OTP is simulated by displaying the OTP in the terminal.

The project currently supports only one stored account.

The project does not use a database.

The password generator uses Python's random module and is intended for learning purposes rather than real-world password generation.

15. Future Improvements

If I continue developing this project, some possible improvements would be:

Add password hashing.
Store users in a database.
Support multiple user accounts.
Improve OTP handling.
Add more advanced password checks.
Create a graphical user interface.
Add more automated tests.
Improve the overall account management system.

16. Project Purpose

I created this project to apply the Python concepts I learned in the Python Essentials course to a small practical application.

While developing it, I practiced functions, modules, conditions, loops, data structures, file handling, validation, exception handling, and unit testing.

The project helped me understand how individual Python concepts can be combined to create a complete command-line application.
