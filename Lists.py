#Operation
L = [] # Empty List
L = [123, 'abc', 1.23, {}] #four items:indexes 0-3
# A list can respond to seqeunce of operations such strings, concatenation, 
L = ['Bob', 40.0, ['dev', 'mgr'], ['t', 'k']] # Nested sublists 
#Index of a Index 
L[0][0]
print(L)
L = list('spam')
print(L)
# Convert List into a string by using str()
J = [1, 2, ]
#K = str(J) + "34"
#print(K)
#List out the 
J = [1, 2] + list("6")
print(J)

print(3 in [1, 2, 3, 4]) # Bool
for x in [1, 2, 3]: # Iteration
    print(x, end='')

# List Comprehensions
res = [c * 4 for c in L]
print(res)
print(list(map(abs, [-1, -2, 0, 1, 2])))

# Index Operations 
matrix = [[1,2,3], [4, 5, 6], [7, 8, 9]]
matrix1 = ["jake", "Kane", "Devon"]
print(sorted(matrix1, key=str.lower,reverse=True))
print(sorted([x.upper() for x in matrix1], reverse=True))

print(matrix[1][0])
# Insert all at :0, an empty slice at front
matrix[:0] = [3, 4]
# Insert all at len(L):, an empty slice at end
matrix[len(matrix):] = [5, 6, 7]
# Insert all at end, named method 
matrix.extend([8,9, 10])
print(matrix.extend([8, 9, 10]))
print(matrix1.index("jake"))
print(matrix1.remove("Kane"))

print(matrix1)



