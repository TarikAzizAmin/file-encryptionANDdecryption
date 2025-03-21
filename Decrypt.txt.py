#!/usr/bin/env/python3

from cryptography.fernet import Fernet

def get_key():
    with open("keyfile.key", "rb") as file:
        key = file.read()
    return key


fernet = Fernet(get_key())


def decrypt_file(file):
    try:
        key = get_key()
        with open(file, "rb") as f1:
            content = f1.read()
        decrypted_content = fernet.decrypt(content)
        print(content)
        print(decrypted_content)
        with open(file, "wb") as f2:
            f2.write(decrypted_content)
    except Exception as e:
        print(f"An error occurred while decrypting file : {str(e)}")

if __name__ == "__main__":
    filePath = input("Please enter the file location for decrypt\n")
    decrypt_file(filePath)
