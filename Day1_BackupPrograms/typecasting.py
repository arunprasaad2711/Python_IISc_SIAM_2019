'''

Program to check different kinds of type casting.

'''

import numpy as np
a = 5
b = [5, 7.9, 3.4]
print(int(a), type(int(a)))           
print(float(a), type(float(a)))       
print(chr(a), type(chr(a)))          
print(str(a), type(str(a)))          
print(bool(a), type(bool(a)))        
print(list(b), type(list(b)))         
print(tuple(b), type(tuple(b)))       
print(np.array(b), type(np.array(b)))
