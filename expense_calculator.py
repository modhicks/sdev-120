#Author: Moniquia Hicks
#Date: 1/27/2025
#Program: expense_calculator.py
#Version: 1.0

#This program calculates your expenses and remaining budget.

#initialization
monthlyIncome = 0.0
totalExpenses = 0.0
remainingBudget = 0.0

#get data
monthlyIncome = float(input("Please enter your monthly income: "))
totalExpenses = float(input("Please enter your total expenses: "))

#process data
remainingBudget = monthlyIncome - totalExpenses

#output information
print("Your monthly income is: $", format(monthlyIncome, ".2f"), sep="")
print("Your total expenses are: $", format(totalExpenses, ".2f"), sep="")
print("Your remaining budget is: $", format(remainingBudget, ".2f"), sep="")