# Key Factors
import math
#Simple Interest
# Principle Variable
Principal = P = 100000
# Number of Years on Loan
number_of_years_on_loan = n = 10
# Interest Rate On Loan
intrest_rate_on_loan = i = 10 / 100
# To find the amount after certain amount of years: Principal(1 + (number of years * interest rate)
A = P * (1+( n * float(i)))
print(A)
interest_gained = A - P 
print(interest_gained)
Principal1 = A / (1+n*i)
print(Principal1)
from decimal import *
ExtendedContext
Context(prec= 5, rounding= ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999,
        capitals=1, flags=[], traps=[Overflow, DivisionByZero, InvalidOperation])
setcontext(ExtendedContext)
getcontext().prec = 4
p = Decimal(4) / 100
print(p)
interest_rate1 = (A/P-1)/n
print(interest_rate1)
number_of_years_on_loan1 = ((A/P)-1)/i
print(math.ceil(number_of_years_on_loan1))
#Year = input("What is your loan term?")
#days = year * 365

#loan_days = math.ceil(APR/365) 

#addtional_fees = amount_loan / loan_days
#Payment = input("Payment:")
#Present_Value = input("Present Value:")
#number_of_periods = input("Number of periods:")
#Loan_Payment = payment * ((rate_per_periods) * int(Present_Value) / 1 - (1 + int(math.pow(int(rate_per_periods), int(number_of_periods))))

# Compound Interest
Principal = P = 10000
Annual_Interest_Rate = i = 10
one = 1
ii = i/100
c = (100000) * (1 + 0.1)**10 - (1)
print(math.floor(c))
Number_of_compounding_periods = n = 3
cii = (100000) * (1 + 0.1)**10 - 100000
print(math.floor(cii))
ci = P * (1 + ii**n - 1)
print(10000 * (1 + 0.05)**3-1)
print(ci)

Deposit = 1000
inter = 0.05

year = [2020, 2021, 2022, 2023, 2024]

for x in year:
        prin = 100000
        nn = 0.05 
        FV = prin * (1 + nn)**5
        if FV == 2020: print(FV)
        prin1 = FV
        FV1 = prin1 * (1 + nn)**5
        if FV1 == 2021: print(FV1)
        
