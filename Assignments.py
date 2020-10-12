Spam = 'spam' # Basic Form 
spam, ham = 'yum', 'YUM' # Tuple assignment(positional)

print(spam, ham)
[spam, ham] = ['yum', 'YUM'] # List assignment(positional)
print([spam, ham])
a, b, c, d = 'spam' # Sequence Assignment 
print(a, b, c, d)
a, *b = 'slim' # Extended sequence unpacking
print(a, *b, c, d)
spam = ham = 'lunch' # Multiple-target assignment
ham = 'turkey' + spam
print(ham)
y = 23 += 42 #Augmented Assignment(equivalent to spams = spams + 42)
print(y)

