#Author: Moniquia Hicks    Date: 1/25/2025
#Program: Rent Calculator  Version: 1.0

#This program calculates the daily rent of an apartment given the monthly rent and the number of days in the month.

#initialization
daysPerMonth = 0
monthlyRent = 0
dailyRent = 0

#get data
monthlyRent = input("Please enter the monthly rent: ")
monthlyRent = int(monthlyRent) #casting string => int
daysPerMonth = input("Please enter the number of days in the month: ")
daysPerMonth = int(daysPerMonth) #casting string => int

#process data
dailyRent = monthlyRent / daysPerMonth

#output information
print("Your monthly rent is $" + str(monthlyRent)) #casting int => string
print("In a " + str(daysPerMonth) + " day month, your daily rent would be $" + str(dailyRent)) #casting int => string