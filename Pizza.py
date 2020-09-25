toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
toppings.sort()
prices = [2, 6, 1, 3, 2, 7, 2]
prices.sort()
num_pizzas = len(toppings)
print("We sell %s different kinds of pizza!" % num_pizzas)
pizzas = list(zip(toppings, prices))
print(pizzas)
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
most_expensive = pizzas[6]
print(most_expensive)
three_cheapest = pizzas[0:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)