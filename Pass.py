import os
import json
from cryptography.fernet import Fernet
import getpass

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current directory
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Save password to a file
def save_password(service, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    data = {service: {"username": username, "password": encrypted_password.decode()}}
    
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
        passwords.update(data)
    else:
        passwords = data

    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Retrieve password from a file
def getsrv():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
        print("Available services:")
        for svc in passwords.keys():
            print(svc)
    else:
        print("No services found.")

def retrieve_password(service):
    key = load_key()
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
        
    if service in passwords:
        encrypted_password = passwords[service]["password"]
        decrypted_password = decrypt_password(encrypted_password.encode(), key)
        return passwords[service]["username"], decrypted_password
    else:
        return None, None

# Main function
def main():
    if not os.path.exists("secret.key"):
        generate_key()

    while True:
        choice = input("Would you like to:\n(1) save a new password\n"
                    "(2) retrieve an existing password? :\n"
                    "(3) quit \n")
        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            save_password(service, username, password)
            print("Password saved successfully!")
        elif choice == "2":
            getsrv()
            service = input("Enter the service name: ")
            username, password = retrieve_password(service)
            if username:
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Service not found!")
        elif choice == "3" or choice == 'q' or choice == 'quit':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()