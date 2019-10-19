'''
Program to calculate the area of a triangle using Heron's formulae
'''

# Get inputs
a = float(input("Enter the side 'a' of the triangle:"))
b = float(input("Enter the side 'b' of the triangle:"))
c = float(input("Enter the side 'c' of the triangle:"))

# Calculate the perimeter
p = (a + b + c)

# Calculate the semi-perimeter
s = p/2
# s = p*0.5

# Find the Area
Area = (s*(s-a)*(s-b)*(s-c))**0.5

# Print the result
print(f"The area of the triangle with sides a = {a}, b = {b}, and c = {c} is {Area} sq.units")
