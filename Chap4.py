#Numbers
print(len(str(2** 10000)))
print(3.1415 * 2)
import math 
print(math.pi)
dem = 323
f = 3522
d = dem * f 
print(math.pi * d)
print(math.sqrt(d))
import random 
print(random.random())
print(random.choice([1, 2, 3, 4]))
#Strings 
S = 'Spam'
len(S)
print(S[0])
print(S[len(S)-1])
print(S[1:])
print(S[:])
print(S + 'xyz')
print(S * 8)
K = 'z' + S[1:]
print(K)
Kl = list(S)
print(Kl)

print('c'.join(K))
S.find('pa')
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))
print(S)
line = 'aaa,bbb,ccccc,dd'
line.split()
print(line.split(','))
S.isalpha()
print(S.isalpha())
print(S.isdigit())
(print(line.rstrip()))
print(' %s, eggs, and %s!' % ('spam', 'SPAM'))
print('{}, eggs, and {}' .format ('spam', 'spam'))
print('{:,.2f}'.format(296999.2567))
print(dir(S))
K = 'A\nB\tC'
print(K)
print(ord('u'))
import re
lin = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', lin, re.M|re.I)


if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("mathcObj.group() : ", matchObj.group(1))
    print("matchObj.group() : ", matchObj.group(2))
else: 
    print("No match!!")

M = [[1,2,3], [4,5,9], [7,8,9]]
print(M[1][2])

col2 = [row[1] for row in M]
print(col2)
col1 = [row[1] + 1 for row in M]
print(col1)

col3 = [row[1] for row in M if row[1] % 2 == 0]
print(col3)
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c *  2 for c in 'spam']
print(doubles)

print([[x**2, x**3] for x in range(4)])
print([[x, x/2, x*2] for x in range(-6, 7, 2) if x > 0])

D = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink', }
print(D['quantity'] + 1)
kk = D['quantity'] 
print(kk)
T = {}
T['Name'] = 'Bob'
T['Job'] = 'IT'
T['Age'] = 40
print(T)
print(T['Name'])
Tk = {'name' : {'first' : 'Bob', 'last': 'Smith'}, 'jobs' : ['dev', 'mgr'], 'age': 40.5}
print(Tk)
print(Tk['name']['last'])
print(Tk['jobs'][-1])
f = open('data.txt', 'w')
f.write('Hello\n')
print(f.write)