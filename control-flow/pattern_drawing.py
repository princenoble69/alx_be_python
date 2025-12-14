size = 0 
pattern = 0

try:
    size = input("Enter the size of the pattern:")
    pattern = int(size)

except ValueError:
    print("ERROR: ENTER NUMERICAL VALUES ONLY")
    exit()

if pattern <= 0:
    print("Error: number must be positive")
    exit()

ash = '*'
row = 0

while row < pattern:
    
    for col in range(pattern):
        print(ash, end="") 
    
    print()
    
    row += 1