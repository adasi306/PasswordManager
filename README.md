# Password Manager Application

This is a desktop application built using Python and Tkinter. The application helps users securely manage their passwords with features like password generation, encryption, storage, and retrieval.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Project Description

The password manager allows users to:
- Generate strong random passwords.
- Save passwords securely with encryption using a master password.
- Search and retrieve passwords for specific websites.

Passwords are encrypted with the user's master password, ensuring secure storage and retrieval.

## Features

1. **Password Generation**:
   - Generate strong random passwords containing letters, numbers, and symbols.
2. **Password Encryption**:
   - Encrypt passwords using a master password and the Fernet encryption method.
3. **Secure Storage**:
   - Store passwords in a JSON file with encryption.
4. **Search Functionality**:
   - Retrieve stored passwords by decrypting them using the master password.

## Requirements

- Python 3.x
- Required Python libraries:
  - `cryptography`

## Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd <project-directory>
```
2. Install the required libraries:
```bash
   pip install -r requirements.txt
```
3. Ensure the following files are in place:
   - `data.json` (to store encrypted passwords, can be an empty file initially).
   - `logo.png` (the logo for the application, placed in the same directory as the script).

## Running the Application

1. Run the script:
```bash
   python main.py
```
2. The application window will open with the following functionalities:
   - Add new passwords.
   - Generate strong random passwords.
   - Search for stored passwords.

3. When prompted, use a master password to encrypt or decrypt your stored passwords.

## Project Structure

project/
├── data.json                 # JSON file to store encrypted passwords
├── logo.png                  # Logo for the application
├── main.py                   # Main script for the application
└── README.md                 # Documentation

## Security Notes

- The master password is used to generate an encryption key, which is crucial for decrypting the stored passwords. Keep it safe and do not forget it.
- The application does not store the master password, so losing it means you cannot access your saved passwords.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.
