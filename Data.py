import dbm 
import base64
import pickle
import shelve



[egServer50]
	host = symachine.domain.com
	port = 5000
	tds version = 5.0

# A typical Microsoft server
[egServer73]
	host = ntmachine.domain.com
	port = 1433
	tds version = 7.3



'''
class person():
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job 
        self.pay = pay 
    def tax(self):
        return self.pay * 0.25
    def info(self):
        return self.name, self.job, self.pay, self.tax()

bob = person('bob', 'Doctor', 8000)
kas = person('Jame', 'Programmer', 9000)

dbase = shelve.open('cast')
for obj in (bob, kas):
    dbase[obj.name] = obj
dbase.close()
dbase = shelve.open('cast')
print(dbase['bob'].tax())

dbase = shelve.open("mydbase")

object1 = ['The', 'bright', ('side', 'of'), ['life']]
object2 = {'name': 'Brain', 'age' : 33, 'motto': object1}
del dbase['key']
dbase['brain'] = object2
dbase['knight'] = {'name': 'Knight', 'motto': 'Ni!'}

dbase.close()


dbase = shelve.open("mydbase")
print(len(dbase))
print(list(dbase.keys()))
print(dbase['knight'])

for row in dbase.keys():
    print(row, '=>')
    for field in dbase[row].keys():
        print(' ', field, '=', dbase[row][field])


class Rec:
    def __init__(self, books):
        self.books = books
    def pay(self, rate=30):
        return self.books * rate
bob = Rec(40)
pickle.dump(bob, open('bobrec', 'wb'))

rec = pickle.load(open('bobrec', 'rb'))
print(rec.pay())

table = {'a': [1,2,3],
              'b': ['spam', 'eggs'],
              'c': {'name': 'bob'}}
# mydb binary mode
mydb = open('dbase', 'wb')
# Source, Destination
pickle.dump(table, mydb)

mydb = open('dbase', 'rb')
table = pickle.load(mydb)
print(table)

print(mydb == table, table is mydb)

def save(filename, object):
    #Save object to the file"
    file = open(filename, 'wb')
    pickle.dump(object, file)
    file.close()

def load(filename):
    file = open(filename, "rb")
    object = pickle.load(file)
    file.close()
    return object
L = [0]
D = {'x':0, 'y':L}
table = {'A':L, 'B':D}

if __name__=='__main__':
    save('myfile', table)
    print(load('myfile'))

file = dbm.open('Books', 'c')
file['Kevin Durant'] = 'Nets'
file.keys()
# pg 1978
who = ['Lonzo Ball', 'Kobe Bryant', 'Michael Jordan']

what = ["Hornets", "Lakers", "Bulls"]
for i in range(len(who)):
    file[who[i]] = what[i]
    print(file[who[i]])
print(file.keys())

print(len(file), 'Lakers' in file, file['Michael Jordan'])
for key in file.keys(): print(key, file[key])
'''