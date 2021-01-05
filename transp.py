plain_text = input("Enter Message:")
key = int(input("Key Shift:"))
encrypting = [' '] * key 
for x in range(key):
    y = x

    while y < len(plain_text):
        encrypting[x] += plain_text[y]

        y += key

print(''.join(encrypting))

