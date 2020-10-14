Weights = [1, 2, 3, 4, 5]
set1, set2, set3, set4, set5, = Weights
Weight = set2 + set4 + set5
set1, set2, set3 = Weights[0], Weights[1], Weights[2:]
print(set1, set2, set3)
set1, *set2 = Weights
print(set1)
print(*set2)
while Weights:
    front, Weights = Weights[0], Weights[1:]
    print(front, Weights)
#import mysql.connector

#cnx = mysql.connector.connect(user = 'root' , password = 'Takegrantmodel1!', host = '127.0.0.1', database = 'MyFruitDatabase')

#cnx.close(
cash = 45
bills = 34
if (cash > 40 and 
    bills < 100 ):
    print(cash)
if x == 4 : print(x, y; x, y = y, x)