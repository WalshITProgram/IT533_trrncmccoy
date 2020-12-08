from time import sleep
message = input("Enter Message:")

shift = 3
encryption = " "

for c in message:
    if c.isalpha():
        c_index = ord(c)
        starting_point = ord(c) - ord("a")
        shift_eq = (starting_point + shift) % 26
        Reduce = shift_eq + ord("a")
        new_index = chr(Reduce)
        encryption = encryption + new_index

    
print("Encrypting Message.......")
sleep(3)

print("Encryption Key:", encryption)

sleep(3)

# Decryption formula - x = (c-n) % 26
encryption_text = encryption
shifts = 3
plain = " "
for x in encryption_text:
    if x.isalpha():
        x_index = ord(x)
        shiftq = ord(x) - ord("a")
        equ = (shiftq - shifts) % 26
        increase = equ + ord("a")
        index = chr(increase)
        plain = plain + index
print("Now decrypting message.....")
sleep(3)
print("Decrypt", plain)
