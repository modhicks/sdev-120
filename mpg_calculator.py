#Author: Moniquia Hicks
#Date: 1/25/2025
#Program: MPG Calculator
#Version: 1.0

#This program calculates miles per gallon

#initialization
gallonsOfGas = 0.0
milesDriven = 0.0
milesPerGallon = 0.0

#get data
gallonsOfGas = float(input("Please enter the gallons of gas used: "))
gallonsOfGas = float(gallonsOfGas)
milesDriven = float(input("Please enter the miles driven: "))
milesDriven = float(milesDriven)

#process data
milesPerGallon = milesDriven / gallonsOfGas

#output information
print("Your total miles driven: ", milesDriven)
print("Gallons of gas used: ", gallonsOfGas)
print("Your total MPG: ", milesPerGallon)