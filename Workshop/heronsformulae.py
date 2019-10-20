a = float(input("Enter the side 'a':"))
b = float(input("Enter the side 'b':"))
c = float(input("Enter the side 'c':"))

if(a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (c + a > b)):

	s = (a + b + c)/2
	Area = (s*(s-a)*(s-b)*(s-c))**0.5
	print(f"The area of the triangle with sides a = {a}, b = {b}, c = {c} is = {Area} sq. units")

else:
	print("The triangle does not exist")
	