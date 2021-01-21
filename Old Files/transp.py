class Encryption:
    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = key
        
    def encrypt(self, encrpter):
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

plain_text = input("Enter Message:")
key = int(input("Key Shift:"))
encrypting = [' '] * key 
for x in range(key):
    y = x

    while y < len(plain_text):
        encrypting[x] += plain_text[y]

        y += key
x = Encryption(encrypting, key)
x.encrypt(encrypting)
print(''.join(x.encrypt(encrypting)))


