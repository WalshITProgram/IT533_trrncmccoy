import itertools
import time
import hashlib
from binascii import hexlify
import shutil
import os

pw = input("Enter Password:")
pw = pw.encode('utf-8')
pwHashHex = hashlib.sha3_512(pw).hexdigest()
print(pwHashHex)

# Function to brute force the password
def tryPassword(pwHashHex):
    start = time.time()
 
    # Allowed characters in the password
    alphabet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    
    attempts = 0

    for value in range(1, 800):
        # Build up a string to test against, character by character
        for pwCandidate in itertools.product(alphabet, repeat=value):
            attempts += 1
            pwCandidate = ''.join(pwCandidate)
            pwCandidate = pwCandidate.encode('utf-8')

            #if the string we are building matches the password given to us, return from the function
            if hashlib.sha3_512(pwCandidate).hexdigest() == pwHashHex:
                end = time.time()
                distance = end - start
                return (pwCandidate, attempts, distance)

pwFound, tries, timeAmount = tryPassword(pwHashHex)
print("The password %s was cracked in %s tries and %s seconds!" % (pwFound, tries, timeAmount))


