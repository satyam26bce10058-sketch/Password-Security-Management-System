Password Security Management System
1. Project Overview

The Password Security Management System is a beginner-level Python project that I created to practice the concepts I learned in my Python Essentials course.

It is a command-line application that focuses on basic password management and account security. The user can check the strength of a password, generate a new password, create an account, log in, change the password, and view a simple security report.

The project also includes basic input validation, file handling, OTP verification, and unit testing.

Note: This project is made for educational purposes. It is not intended to be used as a real password management or security system.

2. Objectives

The main objectives of this project are:

Check whether a password is Weak, Medium, or Strong.

Give suggestions when a password can be improved.

Generate a password based on the length entered by the user.

Create and manage a basic user account.

Provide a simple login system with OTP verification.

Allow the user to change their password.

Display basic account security information.

Practice using functions and separate Python modules.

Practice file handling and input validation.

Learn how to write and run basic unit tests.

3. Features
Password Management

Check password strength

Get suggestions for improving a password

Generate passwords

Validate password length

Account Management

Create an account

Log in

Verify username and password

Change password

View account information

Security and Report

OTP verification

Maximum 3 OTP attempts

Maximum 3 login attempts

Basic security report

Password strength status

Testing

The project includes tests using Python's built-in unittest module.

There are currently 10 tests:

4 password-related tests

6 validation-related tests

4. Main Functional Modules

The project can be divided into three main functional areas.

1. Password Management

This part of the project handles password-related operations such as checking password strength, giving suggestions, and generating passwords.

Files used:

password_tools.py
validators.py

2. Account Management

This part handles creating an account, logging in, changing the password, and viewing account information.

File used:

account.py

3. Security and Reporting

This part handles OTP verification and generates a simple report showing the current password strength.

Files used:

security.py
report.py

5. Technologies and Python Concepts Used
Tools

Python 3

Git

GitHub

Command Prompt / Terminal

Python Concepts

During this project, I used and practiced:

Variables

Strings

Boolean values

Lists

Tuples

Conditional statements

if-else

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
Password-Security-Management-System/
│
├── data/
│   └── users.txt
│
├── tests/
│   ├── test_password.py
│   └── test_validators.py
│
├── README.md
├── statement.md
├── main.py
├── account.py
├── password_tools.py
├── report.py
├── security.py
├── storage.py
└── validators.py

File Description
File	Description
main.py	Displays the main menu and controls the program workflow
account.py	Handles account creation, login, password change, and account information
password_tools.py	Checks password strength, provides suggestions, and generates passwords
security.py	Generates and verifies OTPs
storage.py	Saves and loads account information from the text file
validators.py	Validates usernames, passwords, and password length
report.py	Generates the basic security report
tests/test_password.py	Tests password-related functions
tests/test_validators.py	Tests validation functions
data/users.txt	Stores the current account information
.gitignore	Prevents Python cache files from being uploaded to Git
7. Requirements

To run this project, you need:

Python 3

No external Python libraries are required.

Git is only needed if you want to clone or manage the project using Git.

8. How to Run
Step 1: Download the Project

Download the project from GitHub or clone the repository.

Step 2: Open the Project Folder

Open Command Prompt or Terminal in the project folder.

Step 3: Start the Program

Run:

python main.py


The program will display the following menu:

==================================================
       PASSWORD SECURITY MANAGEMENT SYSTEM
==================================================

1. Create Account
2. Login
3. Check Password Strength
4. Generate Password
5. Change Password
6. Account Information
7. Security Report
8. Exit


Enter the number of the option you want to use.

9. How to Run the Tests

The project uses Python's built-in unittest module.

Password Tests

Run:

python -m unittest tests.test_password


The test file contains 4 tests.

Expected result:

....
----------------------------------------------------------------------
Ran 4 tests in ...s

OK

Validation Tests

Run:

python -m unittest tests.test_validators


The test file contains 6 tests.

Expected result:

......
----------------------------------------------------------------------
Ran 6 tests in ...s

OK

Test Summary

A total of 10 tests are included in the project:

4 password tests

6 validation tests

All 10 tests were successfully run on my local computer.

10. Input Validation and Error Handling

The program checks several types of invalid input.

For example:

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
Usability

The project uses a simple numbered menu, making it easy to understand and operate from the command line.

Performance

The program works with a small amount of data and performs simple operations such as password checking and reading or writing a text file. These operations are expected to complete quickly for the intended use of the project.

Security

The project includes basic security-related features such as password strength checking, login attempt limits, and OTP verification.

However, passwords are stored as plain text because this is a beginner educational project. Password hashing and encryption are outside the current scope.

Reliability

The program uses input validation and basic error handling to reduce problems caused by invalid user input.

Maintainability

The code is divided into separate Python files. For example, password functions are kept in password_tools.py, validation functions are kept in validators.py, and account operations are kept in account.py.

This makes the code easier to understand and modify.

12. User Workflow

The general workflow of the program is:

Start
  |
  v
Main Menu
  |
  +----> Create Account
  |
  +----> Login
  |        |
  |        +----> Username & Password
  |        |
  |        +----> OTP Verification
  |
  +----> Check Password Strength
  |
  +----> Generate Password
  |
  +----> Change Password
  |
  +----> Account Information
  |
  +----> Security Report
  |
  +----> Exit

13. Testing Results

I tested the project using Python's unittest module.

Password Tests
Ran 4 tests
OK

Validation Tests
Ran 6 tests
OK

Total
10 tests passed


The tests were run locally before preparing the project for submission.

14. Limitations

Since this is a beginner-level educational project, it has some limitations:

Account information is stored in a text file.

Passwords are stored as plain text.

OTP is simulated by displaying the OTP in the terminal.

The project currently supports only one stored account.

It does not use a database.

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
