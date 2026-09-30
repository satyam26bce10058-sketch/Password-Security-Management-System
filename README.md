Password Security Management System
1. Project Overview

The Password Security Management System is a beginner-level Python command-line project developed to demonstrate basic password security, account management, validation, file handling, and testing concepts.

The system allows users to:

Check password strength

Get suggestions for improving weak passwords

Generate passwords

Create an account

Log in using username, password, and OTP verification

Change their password

View account information

Generate a basic security report

This project was developed using Python concepts learned during the Python Essentials course.

Note: This is an educational project and is not intended to be used as a production-level password management system.

2. Objectives

The main objectives of this project are:

To check the strength of a password.

To provide suggestions for improving weak passwords.

To generate passwords of a user-selected length.

To allow users to create and manage a basic account.

To provide login verification using an OTP simulation.

To allow users to change their password.

To provide a basic security report.

To demonstrate modular Python programming.

To demonstrate input validation and file handling.

To demonstrate unit testing.

3. Features
Password Management

Password strength checker

Password improvement suggestions

Password generator

Password length validation

Account Management

Create account

Login

Password verification

Change password

Account information

Security and Reporting

OTP verification simulation

Maximum three OTP attempts

Login attempt limitation

Security report

Password strength status

Testing

Unit testing using Python's unittest module

Validation testing

10 automated tests

4. Functional Modules

The project contains three major functional modules.

Module 1: Password Management

This module provides:

Password strength checking

Password improvement suggestions

Password generation

Password length validation

Main files:

password_tools.py
validators.py

Module 2: Account Management

This module provides:

Account creation

Login

Password change

Account information

Main file:

account.py

Module 3: Security and Reporting

This module provides:

OTP verification

Login attempt control

Password security report

Password strength status

Main files:

security.py
report.py

5. Technologies and Python Concepts Used
Technologies

Python 3

Git

GitHub

Command Prompt / Terminal

Python Concepts

Variables

Data types

Strings

Boolean values

Lists

Tuples

Conditional statements

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
├── .gitignore
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
File	Purpose
main.py	Main menu and program workflow
account.py	Account creation, login, password change, and account information
password_tools.py	Password strength checking, suggestions, and password generation
security.py	OTP generation and verification
storage.py	Saving and loading account information
validators.py	Username, password, and length validation
report.py	Security report
tests/test_password.py	Password function unit tests
tests/test_validators.py	Validation function unit tests
data/users.txt	Stores the current account data
.gitignore	Prevents Python cache files from being tracked
7. Requirements

Before running the project, install:

Python 3

No external Python packages are required.

Git is optional if the project is downloaded as a ZIP file.

8. How to Run the Project
Step 1: Download the Project

Download or clone the GitHub repository to your computer.

Step 2: Open the Project Folder

Open Command Prompt or Terminal inside the project folder.

Step 3: Run the Program

Use:

python main.py


The main menu will appear:

1. Create Account
2. Login
3. Check Password Strength
4. Generate Password
5. Change Password
6. Account Information
7. Security Report
8. Exit


Select an option by entering the corresponding number.

9. How to Run Tests

The project uses Python's built-in unittest framework.

Run the password tests:

python -m unittest tests.test_password


Expected result:

....
----------------------------------------------------------------------
Ran 4 tests in ...s

OK


Run the validation tests:

python -m unittest tests.test_validators


Expected result:

......
----------------------------------------------------------------------
Ran 6 tests in ...s

OK

Total Tests

The project contains 10 automated tests:

4 password tests

6 validation tests

All 10 tests have been successfully tested locally.

10. Input Validation and Error Handling

The project performs basic validation for:

Empty usernames

Short usernames

Usernames containing spaces

Short passwords

Invalid password lengths

Password generator lengths below 8

Incorrect login credentials

Incorrect OTP entries

The program displays messages to help the user correct invalid input.

11. Non-Functional Requirements
Usability

The system provides a simple numbered command-line menu so that users can easily understand the available options.

Performance

The application performs small operations such as password checking, file reading, and file writing. These operations are suitable for the small amount of data used by this educational project.

Security

The system includes:

Password strength checking

Login attempt limitation

OTP verification simulation

The project is educational and does not implement production-level password encryption or hashing.

Reliability

Input validation and basic error handling are used to reduce invalid input and unexpected program behavior.

Maintainability

The program is divided into multiple Python modules. Each module has a specific responsibility, making the project easier to understand and modify.

Error Handling

The program handles invalid input such as:

Invalid password length

Non-numeric password length

Invalid username

Incorrect login credentials

Incorrect OTP

12. User Workflow

The basic workflow is:

Start
  |
  v
Main Menu
  |
  +----> Create Account
  |
  +----> Login
  |        |
  |        +----> Username & Password Verification
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

13. Testing Result

The project was tested using Python's built-in unittest framework.

Password Tests
Ran 4 tests
OK

Validation Tests
Ran 6 tests
OK

Total
10 tests passed

14. Limitations

This project is designed for learning and demonstration purposes.

Current limitations include:

Account information is stored in a text file.

Passwords are not encrypted or hashed.

OTP is simulated by displaying the OTP in the terminal.

Only a basic account storage system is implemented.

The application is designed for a single stored account.

The password generator uses Python's random module and is intended for educational demonstration rather than production security.

15. Future Improvements

Possible future improvements include:

Password hashing

Secure password storage

Multiple user accounts

Database storage instead of a text file

More advanced password security checks

Improved OTP handling

Graphical user interface

More extensive automated testing

16. Project Purpose

This project demonstrates how basic Python programming concepts can be combined to create a complete modular command-line application.

It was developed as an educational project to practice:

Python programming

Functions

Modules

File handling

Validation

Control flow

Exception handling

Unit testing
