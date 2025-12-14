try:
 number = input("Enter a number to see its multiplication table:")
 num = int(number)
except ValueError:
   print("ERROR:ENTER NUMERICAL VALUES ONLY")


for multiplier in range(1,11):
    result= num*multiplier
    print(f"{num}x{multiplier} ={result} ")
