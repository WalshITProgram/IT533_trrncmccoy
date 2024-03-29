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
    K = (f"Transaction Date:{tran['Transaction_date']} : Product Type: {tran.get('Product')} : Price: {tran.get('Price')} : Payment Type: {tran.get('Payment_Type')} : Name: {tran.get('Name')} : City: {tran.get('City')} : State: {tran.get(' State')} : Country: {tran.get(' Country')}")
    print(K)
print(sales_data)

# Solution Method 2 
# Open the csv file
csv_file = open("SalesJan2009.csv")
# Loop through lines in the csv file & performing to eliminate extra "Characters"
for file in csv_file:
    tmp_file = file.split(",")
    tmp_file[0] = tmp_file[0][1:-1]
    tmp_file[1] = tmp_file[1][1:-1]
    tmp_file[2] = tmp_file[2][1:-1]
    tmp_file[3] = tmp_file[3][1:-1]
    tmp_file[4] = tmp_file[4][1:-1]
    tmp_file[5] = tmp_file[5][1:-1]
    tmp_file[6] = tmp_file[6][1:-1]
    tmp_file[7] = tmp_file[7][1:-2]
    tmp_file1 = tmp_file[0]
    tmp_file2 = tmp_file[1]
    tmp_file3 = tmp_file[2]
    tmp_file4 = tmp_file[3]
    tmp_file5 = tmp_file[4]
    tmp_file6 = tmp_file[5]
    tmp_file7 = tmp_file[6]
    tmp_file8 = tmp_file[7]
    tmp_file9 = tmp_file1 + " " + tmp_file2 + " " + tmp_file3 + " " + tmp_file4 + " " + tmp_file5 + " " + tmp_file6 + " " + tmp_file7 +  " " + tmp_file8
    print(tmp_file9) # Character Eliminated 
    sales_data1 = []
    sales_data1.append(tmp_file9)
    #print(sales_data1)


# Solution Method 3
Transaction_date = ['1/2/2009 6:17', '1/2/2009 4:53', '1/2/2009 13:08', '1/3/2009 14:44', '1/4/2009 12:56', '1/4/2009 13:19', '1/4/2009 20:11', '1/2/2009 20:09', '1/4/2009 13:17']
Product_type = ['Product1', 'Product1', 'Product1', 'Product1', 'Product2', 'Product1', 'Product1', 'Product1', 'Product1']
Price = [1200, 1200, 1200, 1200, 3600, 1200, 1200, 1200, 1200]
Payment_Type = ['Mastercard', 'Visa', 'Mastercard', 'Visa', 'Visa', 'Visa', 'Mastercard', 'Mastercard', 'Mastercard']
Name = ['Carolina', 'Betina', 'Federica E Andrea', 'Gouya', 'Gerd W', 'Laurence', 'Fleur', 'Adam', 'Renee Elisabeth']
City = ['Basildon', 'Parkville', 'Astoria', 'Echuca', 'Cahaba Heights', 'Mickleton', 'Peoria', 'Martin', 'Tel Aviv']
State = ['England', 'MO', 'OR', 'Victoria', 'AL', 'NJ', 'IL', 'TN', "Tel Aviv"]
Country = ['United Kingdom', 'United States', 'United States', 'Australia', 'United States', 'United States', 'United States', 'United States', 'Israel']
Sales_data4 = []
count_index = 0
for i in Transaction_date:
    Sales_data4.append({'Transaction_date' : i, 'Product Type' : Product_type[count_index], 'Price' : Price[count_index], 'Payment Type' : Payment_Type[count_index], 'Name' : Name[count_index], 'City' : City[count_index], 'State' : State[count_index], 'Country' : Country[count_index]})
    count_index = count_index + 1
for tran in Sales_data4:
    K = (f"Transaction Date : {tran['Transaction_date']} : Product Type: {tran.get('Product Type')} : Price: {tran.get('Price')} : Payment Type: {tran.get('Payment Type')} : Name: {tran.get('Name')} : City: {tran.get('City')} : State: {tran.get('State')} : Country: {tran.get('Country')}")
    print(K)
print(Sales_data4)


# Solution Method 4
# Create a Nested Dictionary Keys : 1 & Values : "Transaction Date"
people = { 1: {"Transaction_date": "1/2/2009 6:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Carolina", "City": " Basidon ", " State": " England", " Country": "United Kingdom"},
   2: {"Transaction_date" : "1/2/2009 4:53", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": "Betina", "City": " Parkville ", " State": "MO", " Country": "United States"},
   3: {"Transaction_date" : "1/2/2009 13:08", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": "Federica e", "City": " Andrea ", " State": " Astoria", " Country": "United States"} ,
   4: {"Transaction_date" : "1/3/2009 14:44", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa ", "Name": " Gouya", "City": " Echuca ", " State": " Victoria", " Country": "Australia"},
   5: {"Transaction_date" : "1/4/2009 12:56", "Product": "Product2", "Price": "3600", "Payment_Type": "Visa ", "Name": " Gerd W", "City": " Cahaba Heights ", " State": "AL", " Country": "United States"}, 
   6: {"Transaction_date" : "1/4/2009 13:19", "Product": "Product1", "Price": "1200", "Payment_Type": "Visa", "Name": " Laurence", "City": " Mickleton ", " State": "NJ", " Country": "United States"}, 
   7: {"Transaction_date" : "1/4/2009 20:11", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Fleur", "City": " Peoria ", " State": "IL", " Country": "United States"},
   8: {"Transaction_date" : "1/2/2009 20:09", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Adam", "City": " Martin ", " State": " TN", " Country": "United States"},
   9:{"Transaction_date" : "1/4/2009 13:17", "Product": "Product1", "Price": "1200", "Payment_Type": "Mastercard ", "Name": " Renee", "City": " Elisabeth ", " State": "Tel Aviv", " Country": "Israel"}}

# Loop through the keys and values
for p_id, p_info in people.items():
    print(p_info)
for key in p_info:
    print(key + ':', p_info[key])
# Create the JSON File
import json
s = json.dumps(sales_data)
o = json.loads(s)
# Write to the JSON file by dumping the dictionary
json.dump(sales_data, fp=open("Transactional_data.json", 'w'), indent = 4)
json_file = open("Transactional_data.json")
print(open("Transactional_data.json").read())
config_data = json.load(json_file)
json_file.close()

