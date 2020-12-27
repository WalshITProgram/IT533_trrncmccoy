from time import sleep
class Encryption:
    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = key
        
    def encrypt(self):
        encrypting = " "
        for a in plain_text:
            if a.isupper():
                index_distance = ord(a) - ord('A')
                index_shift = (index_distance + key) % 26
                equation = index_shift + ord('A')
                char = chr(equation)
                encrypting += char
                
            elif a.islower():
                index_sub = ord(a) - ord('a')
                shift_eq = (index_sub + key) % 26
                equation = shift_eq + ord('a')
                char = chr(equation)
                encrypting += char
                
            elif a.isdigit():
                a_new = (int(a) + key) % 10
                encrypting += str(a_new)
                
            else:
                encrypting += a
            
        return encrypting
class Decryption(Encryption):
    def __init__(self, ciphertext, key):
        self.ciphertext = ciphertext
        self.key = key
        
    def decrypting(self):
        decryption = " "
        for x in ciphertext:
            if x.isupper():
                deshift = ord(x) - ord("A") 
                deshift_eq = (deshift - key) % 26 
                sec = deshift_eq + ord("A")
                dec = chr(sec)
                decryption += dec
            
            elif x.islower():
                deshift = ord(x) - ord("a")
                deshift_eq = (deshift - key) % 26 
                sec = deshift_eq + ord("a")
                dec = chr(sec)
                decryption += dec 
            elif x.isdigit():
                x_new = (int(x) - key) % 10
                decryption += str(x_new)

            else:
                decryption += x
        return decryption 

Encryption_list = " "
Decryption_list = " "

while True:
    plain_text = input("Enter Message:")
    key = int(input("Key Shift:"))
    encryption = Encryption(plain_text, key)
    encryption.encrypt()
    ciphertext = encryption.encrypt()
    decryption = Decryption(ciphertext, key)
    decryption.decrypting()
    repeat = input("Would you like to encrypt another program?")
    if repeat == "yes":
        bad_char = True
    if repeat == "yes":
        bad_char = False
        break

print("Encrypting Information.....")
sleep(3)
print(encryption.encrypt())
print1 = input("Would you like to decrypt this message?")
if print1 == "yes":
    print("Decrypting Information......." )
sleep(3)
print(decryption.decrypting())