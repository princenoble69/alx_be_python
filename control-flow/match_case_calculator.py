
try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    
   
    num1 = float(num1_str)
    num2 = float(num2_str)
    
except ValueError:
    print("Error: Invalid number entered. Please enter numerical values only.")
    exit() 

operation = input("Choose the operation (+, -, *, /): ")
result = None # Initialize result variable

# 2. Control Flow using match-case
match operation:
    case '+':
        result = num1 + num2
    
    case '-':
        result = num1 - num2
    
    case '*':
        result = num1 * num2
    
    case '/':
        # Case for division: requires a check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            result = "Undefined"
    
    case _:
        # The wildcard case: handles any operation input that doesn't match the above
        print("Error: Invalid operation choice.")

# 3. Output the Result
if result is not None and result != "Undefined":
    print(f"The result of {num1} {operation} {num2} is: {result}")
elif result == "Undefined":
     # This prints only if the division by zero error occurred
     pass