try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    num1 = float(num1_str)
    num2 = float(num2_str)

except ValueError:
    print("Error: Enter numerical values only.")
    exit() # Exit the script if input is bad

operation = input("Choose an operation (+, -, *, /): ")
result = None # Initialize result

# --- MATCH-CASE: CALCULATION ONLY ---
match operation:
    case '+':
        result = num1 + num2
    
    case '-':
        result = num1 - num2
    
    case '*':
        result = num1 * num2
    
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            # Set result to a specific string to signal error
            result = "DIVISION_ERROR"
    
    case _:
        # Handles invalid operation input
        print("Error: Enter a valid operation (+, -, *, /).")
        # Set result to None or "INVALID" to prevent the final print
        result = "INVALID_OP" 

# --- CENTRALIZED OUTPUT ---
# Only print the result if a valid calculation was performed (result is a number)
if isinstance(result, (float, int)):
    print(f"The result is: {result}")