# Program to demonstrate for-loops

# Note the indent! Break in indent means end out statements within loop.
# range syntax: start, stop + 1 unit, step
# range function delivers values from 0 to 10 in steps of 2
# i takes one value in each iteration

for i in range(0, 11, 2):
    print(i)

# Nested loops (one within the other is possible) as shown below

vp = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
for val in vp:
    print("Val = ", val)
    for num in val:
        print(num)
        # continue # to go to next iteration
        # break # to break the loop
