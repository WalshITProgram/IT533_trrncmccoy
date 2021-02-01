import base64
import pyDes
import onetimepad
import os 
import uuid
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, MultiFernet
from itertools import cycle
import itertools
from timeit import timeit 
"""
ECB is divided into blocks and encrypted separatley.
Create Key Generator that creates base64 encoded 32-byte.
Create a instance for Fernet class 
Call Encryption method:
1. Encrypt Message
2. Return message back in bytes
Advantages of using ECB:
* Parallel Encryption of blocks of bits is possible
Disadvantages of using ECB:
* Direct Relationship to the plaintext and ciphertext 
"""
print("ECB")
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
print("")

"""
Cipherblock is produced by encrypting a XOR output of previous cipher block
Create a MultiFernet Class:
1. Implement a initialization vector:
* Both Keys Encrypt
* Both Keys Decrypt
Create two key generators 
Set keys as parameters 
XOR algorithm of encryption and decryption converts the plain text in the format ASCII bytes 
XOR procedure to convert it to a specified byte 
It offers the following advantages to its users:
Fast computation
No difference marked in left and right side
Easy to understand and analyze
"""  
print("CBC")
data = "CBC Messages are padded!"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)

print("Encrypted: %r" % d)
print("Decrypted: %r" % k.decrypt(d))
print("")



"""
CTR turns block cipher into a stream cipher
Generates the next key stream block 
By encrypting successive values of a counter
The counter can be any function which produces a sequence
Advantages:
* CBC works well for input greater than b bits
* CBC is a good authencation mechanism
* Stronger than ECB
"""
print("CTR")
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])
token = f.encrypt(b"CTR turns block cipher into a stream cipher!")
print(token)
print(f.decrypt(token))
print("")

"""
Cipher Feedback Mode(CFB)
The cipher is given as feedback to the next block of encryption:
First an initial vector IV is used for first encryption
Output bits are divided as set of sandb-s bits the left hand side sbits are selected
Are applied an XOR operation with plaintext bits
Advantage:
* There is some data loss due to use of shift register
* Difficult for applying Cryptanalysis 
"""
print("CFB")
def hash_password(password):
   # uuid is used to generate a random number of the specified password
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')

if check_password(hashed_password, old_pass):
   print('You entered the right password')
else:
   print('Passwords do not match')
print("")

"""
Output Feedback Mode
Follows nearly same process as the Cipher Feedback Mode
Except that it sends the encrypted output 
The actual cipher which is XOR output
All bits of the block are send instead of sending selected s bits
"""
print("OFM")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"The output feedback mode makes a block cipher into a synchronous stream cipher")
plain_text = cipher_suite.decrypt(cipher_text)
print(cipher_text)
print(plain_text)
print("")

cipher = onetimepad.encrypt('One Time Cipher', 'random')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)
print("")

encoded_data = base64.b64encode(b"CBC takes each block of plain text before encrypting")
print("The encrypted message:")
print(encoded_data)

decoded_data = base64.b64decode(encoded_data)
print("The plain text fetched:")
print(decoded_data)