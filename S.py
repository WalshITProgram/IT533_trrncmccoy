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


