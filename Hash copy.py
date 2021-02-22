import itertools
import time
import hashlib
from binascii import hexlify
import shutil
import os

data = input("Enter Password:")
data = data.encode('utf-8')
sha3_512 = hashlib.sha3_512(data)
sha3_512_digest = sha3_512.digest()
sha3_512_hex_digest = sha3_512.hexdigest()
print(sha3_512_hex_digest)

# Function to brute force the password
def tryPassword(passwordSet):
    start = time.time()
 
    # Allowed characters in the password
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    
    attempts = 0

    for value in range(1, 800):
        # Build up a string to test against, character by character
        for letter in itertools.product(chars, repeat=value):
            attempts += 1
            letter = ''.join(letter)

            #if the string we are building matches the password given to us, return from the function
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)



tries, timeAmount = tryPassword(sha3_512_hex_digest)
print("The password %s was cracked in %s tries and %s seconds!" % (sha3_512_hex_digest, tries, timeAmount))


