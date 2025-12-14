try:
    num1= input ("enter a number:")
    num2=input("enter a number:")
    num1= float(num1)
    num2=float(num2)

except ValueError:
    print("enter numerical values only")
    exit()

operation = input("choose an operation(+,-,*,/)")
result = None

match operation:
    case '+':
        result = num1 + num2
        print(f"the result is {result}")
    case '-':
        result=num1-num2
        print(f"the resultis {result}")
    case '*':
        result=num1*num2
        print(f"the result is {result}")
    case '/':
        if num2 != 0:
            result= num1/num2
            print(f"the result is {result}")
        else :
            print("ERROR: INPUT IS UNDEFINED")
            result="undefined"
    case _:
        print("ENTER A VALID INPUT")

    
        


