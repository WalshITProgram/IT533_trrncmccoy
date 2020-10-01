# Create Variables & Lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Create a Variable
total_price = 0
# Create a Loop & add each price to the variable total_price
for x in prices:
    total_price += x   
# Create a Variable called average_price
average_price = total_price // len(prices)
print("Average Price: ${0}".format(average_price))
# List Comprehension 
new_prices = [price - 5 for price in prices]
print(new_prices)
# Create a Variable 
total_revenue = 0
# Create a loop variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
# Add prices[i] & last_week[i]
    total_revenue += prices[i] * last_week[i]
print("Total Revenue ${0}".format(total_revenue))
# Find Average Daily Revenue
average_daily_revenue = total_revenue // 7 
print("Average Daily Revenue: ${0}".format(average_daily_revenue))
# Use List Comprehension [Expression, For Statement, Conditional
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)