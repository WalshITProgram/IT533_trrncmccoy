#Store first and last name as a variable
terrance = "terrance "
mccoy = "MCCOY "

#Print Uppercase, Lowercase, Two Newlines
print(f"Hello \n{terrance.upper()} \n{mccoy.lower()} ")

#Store first and last name with space between parts
name = terrance + " " + mccoy
print(name)

#Store slices of last name in Variable
name1 = name[10:-2]
print(name1)

#Replace last name 
name2 = name[8:-1] + " Walsh College Student"
print(name2)

#Print qoute with qoutation marks
qoute = "\"Start by doing what's necessary; then do what's possible and suddenly you are doing the impossible\"" 
print(qoute)

#Store decimal as Variable 
import math
from decimal import Decimal
 
dem = Decimal('2.3') 
dem1 = Decimal('8.5')

#Store one addition Variable
add = dem1 + dem
print(add)

#Store one subtraction Variable
sub = dem - dem1
print(f"The answer is {sub}")


#Store one multiplication Variable
multip = dem * dem1
print(f"The answer is {multip}")

#Store one division Variable
div = dem / dem1
print(div)

#Store sqaure root Variable

sq_root = math.sqrt(multip)
print(f"The sqaure root of {multip} = {sq_root}")

#Store current month as string variable
month = "September"
day = 27

#Print Qoute
print("Today is day {} of the month of {}. ".format(day, month))
