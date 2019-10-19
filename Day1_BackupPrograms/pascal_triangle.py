def pascal(n):

    for i in range(1, n+1, 1):

        coeff = 1
        vals = [coeff]
        for j in range(1, i, 1):
            coeff = coeff*(i - j)//j
            vals.append(coeff)
        print(vals)

rows = int(input("Enter the number of rows in the pascal triangle:"))
print(f"The Pascal Triangle with {rows} rows is:")
pascal(rows)
