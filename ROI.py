ROI = {}
while True:
    Stock_price = input("Stock_price:")
    amount_of_shares = input("Amount of Shares Bought:")
    Buy_Commission = input("Buying Commission Rate:")

    if int(Stock_price) and int(amount_of_shares):
        net_buy_price = int(Stock_price) * int(amount_of_shares) + int(Buy_Commission)
        ROI["Investment Cost"] = (f"${net_buy_price}")

    Sold_price = input("Share Price Sold:")
    sold_amount_of_shares = input("Number of Shares Sold:")
    Sold_Commission = input("Selling Commission Rate:")

    net_sell_price = int(Sold_price) * int(sold_amount_of_shares) - int(Sold_Commission)
    ROI["Profit/Loss"] = (f"${net_sell_price}")
    
    if int(Stock_price) and int(Sold_price):
        Dividend = input("Dividends:")
        current_year = input("Current Year:")
        Total_year = input("Total Investment Years:")
        ROi = round(int(Sold_price) - int(Stock_price) + int(Dividend)/int(Stock_price))
        ROI["ROI"]= (f"{ROi}%")

    divid = int(Dividend) * int(amount_of_shares) * int(Total_year)
    ROI[f"Total Amount of Dividends in {Total_year} Years"] = (f"${divid}")
    Current_Value = int(Sold_price) * int(amount_of_shares)
    Final_Value = divid + Current_Value
    annual_return = round(((Final_Value / net_buy_price)**(int(current_year)/int(Total_year)) - 1)  * 100)
    ROI[f"Annual Return: Year {current_year}"] = (f"{annual_return}%")
    user = input("Would you like to enter another record?")
    if user == "no":
        break
print(ROI)



