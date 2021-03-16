from Classes.database_access import *
from Classes.GUI import * 
import pymysql

GUI()
'''
my_db = DB_Connect('root', '', 'Python_Books', 3307)
my_result = my_db.executeSelectQuery("SELECT * FROM Book_Table")
#print(my_result)

for record in my_result:
    print(record[0])
    print(record[1])
    print(record[2])
    print(record[3])
    print(record[4])
    print(record[5])
    print(record[6])
'''