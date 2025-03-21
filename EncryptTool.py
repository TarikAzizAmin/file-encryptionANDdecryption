#!/usr/bin/env/python3

from cryptography.fernet import Fernet

# Generate key and storing that key in a file named as keyfile.key
def gen_key():
    key = Fernet.generate_key()
    with open("keyfile.key", "wb") as keyfile:
        keyfile.write(key)
    return key

# Creating a fernet instance
fernet = Fernet(gen_key())


# Encrypting the content of the file
def encrypt_file(file):
    with open(file, "rb") as f:
        content = f.read()
    print("Before encryption...")
    print(content)
    encrypted_content = fernet.encrypt(content)
    with open(file, "wb") as f:
        f.write(encrypted_content)
    print("After Encryption...")
    print(encrypted_content)


if __name__ == "__main__":
    originalFile = input("Please enter the location of the file:\n ")
    encrypt_file(originalFile)




