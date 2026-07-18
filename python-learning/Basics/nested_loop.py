#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                  inner loop:

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for x in range(row):
    for y in range(column):
        print(symbol, end="")
    print()