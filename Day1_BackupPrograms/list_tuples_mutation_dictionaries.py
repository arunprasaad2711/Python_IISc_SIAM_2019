# Program to look at lists, tuples, mutation cases, avoiding mutation, and dictionaries

## Lists
## Comment out the other section while running this
x = [1, 3, 5, 7, 8]
y = [1.5, 5, 8.94, -5.78]
z = [1, 'f', True, [6.45, "six"], False]
l = [1, 3.5, 'a', "hello", ['34', 3.14, ["three"], 4], 4.21]
print("x = ", x)
print("y = ", y)
print("z = ", z)
print("l = ", l)
print(x[0])
print(x[4])
# print(y[4]) # This will throw an error: IndexError: list index out of range
print(z[3][1])
print(l[4][2][0])

## Tuples
## Comment out the other section while running this
x = (1, 3, 5, 7, 8)
y = (1.5, 5, 8.94, -5.78)
z = (1, 'f', True, (6.45, "six"), False )
l = ( 1, 3.5, 'a', "hello", ('34', 3.14, ("three"), 4), 4.21 )
print("x = ",x)
print("y = ",y)
print("z = ",z)
print("l = ",l)
print(x[0])
print(x[4])
#print(y[4] # This will throw an error: IndexError: tuple index out of range
print(z[3][1])
print(l[4][2])

## Mutation
## Comment out the other section while running this
x = [4.5, 6.7]
y = x
x.append(1)
print(x, y)

x = (4.5, 6.7)
y = x
# x.append(1) # Produces an error: tuple' object has no attribute 'append'
print(x, y)

## Avoiding Mutation
## Comment out the other section while running this
x = [4.5, 6.7]
y = x
x = [7.8, 9.6]
print(x, y)

x = (4.5, 6.7)
y = x
x = (7.8, 9.6)
print(x, y)

## Dictionary
## Comment out the other section while running this
a = {'v1':6, 'v2':10, 'lst': \
    [5.8, "hello"]}
print(a)
print(a['v1'])
print(a['lst'])
print(a['lst'][1])
