number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        
        print("*", end="")
    
    print()
    row += 1
