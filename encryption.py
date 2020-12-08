from cryptography.fernet import Fernet
from getpass import getpass
from os.path import exists
import json

credential = {
    "username": None,
    "password": None
}

key = Fernet.generate_key()
cipher = Fernet(key)

def get_credential():
    username = input("Username:")
    password = getpass()
    return username, password
print(get_credential())

if not exists("encrypt.json"):
    credential['username'], credential['password'] = get_credential()
    credential_byte = json.dumps(credential).encode('utf-8')
    cred_enc = cipher.encrypt(credential_byte)
    with open("encrypt.json", "wb") as file_enc:
        file_enc.write(cred_enc)

 
with open("encrypt.json", "rb")as file_dec:
    cred_decrypt = file_dec.read()
data = cipher.decrypt(cred_decrypt).decode('utf-8')
print(data)