import numpy as ny
import pandas as pd 
import numpy_financial as npf 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# Build a amortization schedule to accept three arguments:
# Three arguments(Interest Rate/Mortgage Amount/Loan Duration)

def amortization_schedule(input_intrate, mortgage, years):
#Convert Mortage Amount to negative because money is going out
 mortgage_amount = -(mortgage)
 interest_rate = (input_intrate / 100) / 12
 periods = years*12
 # Numpy
 # Create Array
 n_periods = np.arange(years * 12) + 1

 



