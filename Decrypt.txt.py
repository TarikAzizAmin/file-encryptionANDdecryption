#!/usr/bin/env/python3

from cryptography.fernet import Fernet

def get_key():
    with open("keyfile.key", "rb") as file:
        key = file.read()
    return key


fernet = Fernet(get_key())


def decrypt_file(file):
    key = get_key()
    with open(file, "rb") as file:
        content = file.read()
    decrypted_content = fernet.decrypt(content)
    with open(file, "wb") as file:
        file.write(decrypted_content)

if __name__ == "__main__":
    filePath = input("Please enter the file location for decrypt\n")
    decrypt_file(filePath)
