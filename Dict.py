#  Empty Dictionary 
D = {}
# Two Item Dictionary
D = {'name' : 'Bob', 'age': 40}
# Nesting
E = {'cto': {'name': 'Bob', 'age': 40}} 

print(D.keys())

people = { 1: {"Transaction_date": "1/2/2009 6:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Carolina", "City": " Basidon ", " State": " England", " Country": "United Kingdom"},
   2: {"Transaction_date" : "1/2/2009 4:53", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": "Betina", "City": " Parkville ", " State": "MO", " Country": "United States"},
   3: {"Transaction_date" : "1/2/2009 13:08", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": "Federica e", "City": " Andrea ", " State": " Astoria", " Country": "United States"} ,
   4: {"Transaction_date" : "1/3/2009 14:44", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa ", "Name": " Gouya", "City": " Echuca ", " State": " Victoria", " Country": "Australia"},
   5: {"Transaction_date" : "1/4/2009 12:56", "Product": "Product2", "Price": "3600", "Payment_Type": "Visa ", "Name": " Gerd W", "City": " Cahaba Heights ", " State": "AL", " Country": "United States"}, 
   6: {"Transaction_date" : "1/4/2009 13:19", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": " Laurence", "City": " Mickleton ", " State": "NJ", " Country": "United States"}, 
   7: {"Transaction_date" : "1/4/2009 20:11", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Fleur", "City": " Peoria ", " State": "IL", " Country": "United States"},
   8: {"Transaction_date" : "1/2/2009 20:09", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Adam", "City": " Martin ", " State": " TN", " Country": "United States"},
   9:{"Transaction_date" : "1/4/2009 13:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Renee", "City": " Elisabeth ", " State": "Tel Aviv", " Country": "Israel"}}


for p_id, p_info in people.items():
    print("\nID:", p_id)
    print(p_info)
    
for key in p_info:
    print(key + ':', p_info[key])

# Keys & Loops
table = {'1993': 'Doggystyle',
        '1996': 'Dead Presidents', 
        '1999': 'E.Enteral 1999'}
year = '1993'
movie = table[year]
print(movie)

for year in table:
    print(year)
year in table.keys()
print(year + '\t' + table[year])
print(list(table.items()))
[title for (title, year) in table.items() if year == '1993']

Jason = {}
Jason[(2, 3, 4)] = 88
Jason[7, 8, 9] = 99
X = 2; Y = 3; Z = 4
print(Jason[(X, Y, Z)])
print(Jason)

if (2, 3, 4) in Jason: 
    print(Jason[(2, 3, 4)])
else: 
    print(0)

# Solution Method 1 
# Create Empty List
sales_data = []

# Create 9 Dictionaries 
transaction_00 = {"Transaction_date": "1/2/2009 6:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Carolina", "City": " Basidon ", " State": " England", " Country": "United Kingdom"}
transaction_01 = {"Transaction_date" : "1/2/2009 4:53", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": "Betina", "City": " Parkville ", " State": "MO", " Country": "United States"}
transaction_02 = {"Transaction_date" : "1/2/2009 13:08", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": "Federica e", "City": " Andrea ", " State": " Astoria", " Country": "United States"} 
transaction_03 = {"Transaction_date" : "1/3/2009 14:44", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa ", "Name": " Gouya", "City": " Echuca ", " State": " Victoria", " Country": "Australia"}
transaction_04 = {"Transaction_date" : "1/4/2009 12:56", "Product": "Product2", "Price": "3600", "Payment_Type": "Visa ", "Name": " Gerd W", "City": " Cahaba Heights ", " State": "AL", " Country": "United States"}
transaction_05 = {"Transaction_date" : "1/4/2009 13:19", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": " Laurence", "City": " Mickleton ", " State": "NJ", " Country": "United States"} 
transaction_06 = {"Transaction_date" : "1/4/2009 20:11", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Fleur", "City": " Peoria ", " State": "IL", " Country": "United States"}
transaction_07 = {"Transaction_date" : "1/2/2009 20:09", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Adam", "City": " Martin ", " State": " TN", " Country": "United States"}
transaction_08 = {"Transaction_date" : "1/4/2009 13:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Renee", "City": " Elisabeth ", " State": "Tel Aviv", " Country": "Israel"}


# Create a copy of dictionary 
transaction_copy_00 = transaction_00.copy()
transaction_copy_01 = transaction_01.copy()
transaction_copy_02 = transaction_02.copy()
transaction_copy_03 = transaction_03.copy()
transaction_copy_04 = transaction_04.copy()
transaction_copy_05 = transaction_05.copy()
transaction_copy_06 = transaction_06.copy()
transaction_copy_07 = transaction_07.copy()
transaction_copy_08 = transaction_08.copy()

# Append dictionary to list
sales_data.append(transaction_copy_00)
sales_data.append(transaction_copy_01)
sales_data.append(transaction_copy_02)
sales_data.append(transaction_copy_03)
sales_data.append(transaction_copy_04)
sales_data.append(transaction_copy_05)
sales_data.append(transaction_copy_06)
sales_data.append(transaction_copy_07)
sales_data.append(transaction_copy_08)


for tran in sales_data:
     sales_data_2 = []
     K = (f"Transaction Date:{tran['Transaction_date']} : Product Type: {tran.get('Product')} : Price: {tran.get('Price')} : Payment Type: {tran.get('Payment_Type')} : Name: {tran.get('Name')} : City: {tran.get('City')} : State: {tran.get(' State')} : Country: {tran.get(' Country')}")
     sales_data_2.append(K)
     print(K)

list_of_names = ['brandon', 'mike', 'jasmine']
list_of_beverages = ['water', 'iced tea', 'lemonade']
list_of_mine = []
count_index = 0
for t in list_of_names:
    list_of_mine.append({'name': t, 'beverages': list_of_beverages[count_index]})
    count_index = count_index + 1
print(list_of_mine)



