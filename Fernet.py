from cryptography.fernet import Fernet
from os.path import exists
import json
key = Fernet.generate_key()
f = Fernet(key)
print("Key:" + str(f))

text = b'Lebron James 23'
enc_text = f.encrypt(text)
plain_text  = f.decrypt(enc_text)
print("Encrypted: " +str(enc_text))
print("Decrypted: " + str(plain_text))

if not exists("Lokey.json"):
    encrypt = json.dumps(text).encode('utf - 8')
    lock = f.encrypt(encrypt)
with open("Lokey.json", "wb") as file_enc:
    file_enc.write(lock)


