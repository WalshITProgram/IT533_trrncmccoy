import crypt
import pwd
import getpass
from hmac import compare_digest as compare_hash
import cryptography
import string
# Reverse Cipher 
'''
message = input("Enter Message:")
translated = ''
untranslate = ' '
i = len(message) - 1 

while i >= 0:
    translated = translated + message[i]
    i = i - 1
print(translated)

'''
# Caesar Cipher 

record = ' '
message = input("Enter Message:")
key = int(input("Enter Number:"))
for x in message:
    if x.isupper():
        x_index = ord(x) - ord("A")
        x_in = x_index + key % 26 + ord("A")
        x_i =  chr(x_in)
        record += x_i
    if x.islower():
        x_index = ord(x) - ord("a")
        x_in = x_index + key % 26 + ord("a")
        x_i = chr(x_in)
        record += x_i
    if x.isdigit():
        a_index = (int(x) + key) % 10
        record += str(a_index)
print(record)   

message = record
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    print(key)
    translated = ' '
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num1 = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
print('Hacking Key %s %s' % (key, translated))
print("--------------------------------------------")
