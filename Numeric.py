# Testing the range between three variables

# Variables
Credit_score = 620
Income = 100000
Expenses = 1000
Points = 0
P1 = 1
Credit_karma = 619
P4 = P1 + Points

# Create Function  
def test():
  if Income > Expenses and Credit_score > Credit_karma:
        print(P4)
  if Income < Expenses and Credit_karma == Credit_score:
        print("Income Point" + 0)
print(test())

# Division 
X = 20
Y = 4
# Classic Division
print(Y/X)
# Floor Division Rounds Down 
print(Y//X)
# Float Variables 
XX = 3.24
YY = 23
#Import division from _future_ import division
print(X//Y)
# Import Math
import math
math.floor(3.5)
print(math.floor(3.5))
math.trunc(3.5)
print(math.trunc(3.5))
print(4//2, 5/-2)
math.trunc(3.5/5.3)
print(math.trunc(3.5/5.3))
print(2**200)
# Complex Numbers 
print(1j * 1J)
# Subtraction 
print(1j - 1j)
# Add & Multiply
print(2 + 1j * 3)
print(2 - 1j)
# Print Hexa
print(0o1, 0o20)
# Bitwise
x = 1
print(x << 2)
print(x | 2)
print(x & 1)
print(bin(34))
# Built-in Tools 
import math 
print(math.pi)
print(math.e)
# Common constants 
# Sine, tangent, cosine
print(math.sin(2 * math.pi / 180))
# Sqaure Root
print(math.sqrt(144), math.sqrt(2))
# Exponentiation (power)
pow(2, 4), 2**4, 2.0 ** 4.0
print(pow(2, 5))
#abs
print(abs(-42.0))
print(sum((1, 2, 3, 4)))
# Minimum, Maximum
print(min(3, 1, 2, 4))
print(max(3,1, 2, 4))