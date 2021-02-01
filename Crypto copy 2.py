import base64
import os 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, MultiFernet

"""
ECB is divided into blocks and encrypted separatley.
Create Key Generator that creates base64 encoded 32-byte.
Create a instance for Fernet class 
Call Encryption method:
1. Encrypt Message
2. Return message back in bytes
"""
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"ECB encryption lacks diffusion.")
print(token)
"""
Key can encrypt and decrypt.
Call decryption method to decrypt the message
"""
f.decrypt(token)
print(f.decrypt(token))

"""
CBC takes each block of plain text before encrypting 
Create a MultiFernet Class:
1. Implement a initialization vector:
* Both Keys Encrypt
* Both Keys Decrypt
Create two key generators 
Set keys as parameters 
""" 
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])
token = f.encrypt(b"CBC Messages are padded! ")
print(token)
print(f.decrypt(token))

"""
CTR generates the next key stream block by 
encrypting successive values of a counter
"""
password = b"CTR mode turns block cipher into a stream cipher"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
 )
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
token = f.encrypt(b"CTR mode turns block cipher into a stream cipher")
print(token)

f.decrypt(token)
