"""

Operators Test Run

```python
a + b                  # Addition
a - b                  # Subtraction
a * b                  # Multiplication
a / b                  # Division
a += b # a = a+b       # Increment addition
a *= b # -=, /= exists # Increment multiplication
a ** b                 # Exponent
()                     # Parenthesis
a % b                  # Modulo Operation
<	                   # strictly less than	 
<=	                   # less than or equal	 
>	                   # strictly greater than	 
>=	                   # greater than or equal	 
==	                   # equal	 
!=	                   # not equal
or, and, not           # Logical Operators
is, is not             # Identity Operators
in, not in             # Membership Operators
```

| Operator 	|      Name      |  Operation | Example | Result |               Remark              |
|:--------:	|:--------------:|:----------:|:-------:|:------:|:---------------------------------:|
|     +    	|    Addition    |  ``a + b`` |  5 + 6  |   11   |          Normal Addition          |
|     -    	|   Subtraction  |  ``a - b`` |  5 - 6  |   -1   |         Normal Subtraction        |
|     *    	| Multiplication |  ``a * b`` |  5 * 6  |   30   |       Normal Multiplication       |
|     /    	|    Division    |  ``a / b`` |  6 / 4  |   1.5  |          Normal Division          |
|    //    	| Floor Division | ``a // b`` |  15 // 4|    3   |  Division + removes decimal part  |
|     %    	|     Modulus    |  ``a % b`` |  22 % 4 |    2   | Returns the Remainder of Division |
|    **    	| Exponentiation | ``a ** b`` |  2 ** 4 |   16   |     Same as ``2*2*2*2``. Exponent |

"""

a = 11
b = 2

print("a = ", a, " and b = ", b)

# Addition
print("a + b = ", a + b)
# Subtraction
print("a - b = ", a - b)
# Multiplication
print("a * b = ", a * b)
# Division
print("a / b = ", a / b)
# Floor Division
print("a // b = ", a // b)
# Modulus
print("a % b = ", a % b)
# Exponentiation
print("a ** b = ", a ** b)
