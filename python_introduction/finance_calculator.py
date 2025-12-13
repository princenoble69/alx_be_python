monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))
monthly_savings = (monthly_income - monthly_expense)
simple_annual_interest_rate = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest_rate)
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {Projected_savings}")
