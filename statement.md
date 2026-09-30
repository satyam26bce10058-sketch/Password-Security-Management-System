Project Statement

1. Project Title

Password Security Management System

2. Problem Statement

Many users create weak or easily guessable passwords and may not know how secure their passwords are. There is also a need for a simple system that can help users create stronger passwords and manage basic account security.

This project provides a simple Python-based Password Security Management System that allows users to check password strength, generate passwords, create an account, log in, change their password, and view a basic security report.

3. Project Scope

The project is a command-line application developed using Python. It focuses on basic password security concepts, input validation, account management, password generation, OTP verification simulation, and security reporting.

The project is intended for educational purposes and demonstrates beginner-level Python programming concepts.

4. Target Users

The project is mainly intended for:

Beginner computer users who want to check password strength.

Students learning basic password security concepts.

Students learning Python programming and modular programming.

5. Objectives

The main objectives of this project are:

To check the strength of a password.

To provide suggestions for improving weak passwords.

To generate passwords of a user-selected length.

To allow users to create and manage a basic account.

To provide login verification using an OTP simulation.

To allow users to change their password.

To provide a basic security report.

To demonstrate modular Python programming.

To practice input validation and file handling.

To practice basic unit testing.

6. High-Level Features

The project provides the following features:

6.1 Password Strength Checker

Checks whether a password is Weak, Medium, or Strong.

6.2 Password Generator

Generates a password based on the length entered by the user.

6.3 Password Suggestions

Provides suggestions when a password does not meet the basic strength requirements.

6.4 Account Creation

Allows the user to create a basic account using a username and password.

6.5 Login System

Allows the user to log in using the stored username and password.

6.6 OTP Verification

Provides a simple OTP verification simulation after successful password verification.

6.7 Password Change

Allows the user to change the existing password after verifying the current password.

6.8 Account Information

Displays the stored username and the current password strength.

6.9 Security Report

Displays a basic security report based on the current password strength.

6.10 Input Validation

Checks usernames, passwords, password lengths, login details, and OTP entries.

7. Functional Modules

7.1 Password Management Module

This module handles password strength checking, password suggestions, password generation, and password length validation.

Main files:
password_tools.py
validators.py

7.2 Account Management Module

This module handles account creation, login, password changes, and account information.

Main file:
account.py

7.3 Security and Reporting Module

This module handles OTP verification, login attempt control, and the security report.

Main files:
security.py
report.py
