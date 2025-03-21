# Simple Password Manager with Master Password

This is a simple, command-line password manager written in Python that allows users to securely store, retrieve, and manage passwords for different services. The password manager uses encryption (Fernet from the `cryptography` library) to securely store passwords in a JSON file.

## Features
- **Encryption**: Passwords are encrypted before being stored on the disk using symmetric encryption (AES).
- **Master Password**: Users can set a common master password to access and manage all stored passwords.
- **Password Storage**: Passwords are stored in a JSON file, each associated with a service name.
- **Password Retrieval**: Easily retrieve encrypted passwords for a given service.
- **Platform Compatibility**: Supports both Windows and Unix-like systems (Linux, macOS).
- **Secure Password Input**: Passwords are hidden during input to prevent visibility on the screen.

## How It Works
1. **Master Password**: The user can set a master password to access the password manager. This password is used to encrypt and decrypt the keys used for service passwords.
2. **Password Storage**: After entering the master password, users can store passwords for different services (e.g., email, social media, etc.).
3. **Password Retrieval**: Users can retrieve the stored passwords securely by entering the service name.

### Key Components:
- **Fernet Encryption**: Ensures that passwords are stored in an encrypted format.
- **Secure Input**: Uses `msvcrt` (Windows) or `termios` (Unix-like) to securely read passwords from the terminal without displaying them.
- **JSON Storage**: Passwords are saved in a JSON file for easy management and retrieval.

## Installation

### Prerequisites:
- Python 3.x
- `cryptography` library

Install the required libraries using pip:

```bash
pip install cryptography
```

## Usage

1. **Run the script**:

```bash
python password_manager.py
```

2. **Set a Master Password**: When prompted, set a master password to access the password manager. This password will be used to encrypt and decrypt your service passwords.
3. **Store Passwords**: You can add passwords for different services after entering the master password.
4. **Retrieve Passwords**: Retrieve passwords for a specific service by entering the service name.

## Future Improvements
- **Password Strength Meter**: Implement a password strength checker to ensure strong passwords are used.
- **Backup and Restore**: Implement backup and restore functionalities for secure password management.
- **GUI Support**: Add a graphical user interface (GUI) for better usability.

---

Feel free to update the description based on additional features or modifications you've made to the script!
