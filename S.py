#Chapter 10 
# Statements are the thingd you write to tell Python what your programs should do. 
#Python is a procedural, statement based langauge; by combining statements, you specify a procedure that Python performs to satisfy a program's goal.
# The Python Conceptual Hierarchy 
# 1 Programs are composed of modules.
# 2 Modules contain statements.
# 3 Statements contain expressions. 
# 4 Expressions create and process objects. 

# Statement # Role # Example
# Assignment Creating a reference  a, b = 3, 4
# Calls and other expressions Running Functions log.write("spam", "candy")
# print calls print()
# if/elif/else select actions 
# for/else Iteration

#while/else General Loops while x > y: print("hello")
# pass empty placeholder while True: pass

# Interactive Loop
#while True:
    #x = input('Enter Text:')
    #reply = x
    #if int(reply) > 22 : break
    #print(int(reply)** 2)
#n = 5
#while n > 0:
   # n -= 1
   # print(n)
S = "123"
T = 'XXX'
S.isdigit()
T.isdigit()
print(S.isdigit())
print(T.isdigit())

a = 33
b = 33
while a == b:
    if b > a:
     print("d")
    elif a == b:
     print("Cl")
     break

while True:
    reply = input('Enter Text:')
    if int(reply) > 30: break
    print("correct")
    try: 
        reply = 22
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
    else: 
        print('Bye')
