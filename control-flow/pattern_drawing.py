pattern = 0

try:
    pattern = int(input("Enter the size of the pattern: "))

except ValueError:
    print("ERROR: ENTER NUMERICAL VALUES ONLY.")
    exit()

if pattern <= 0:
    print("Error: The number must be a positive integer.")
    exit()

ASH = '*'
row = 0

while row < pattern:
    
    for col in range(pattern):
        print(ASH, end="") 
    
    print()
    
    row += 1
