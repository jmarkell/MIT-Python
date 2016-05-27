# Problem Set 1
# Name: Markell
# Collaborators: N/A
# Time Spent: 
# Take an outstanding balance and annual interest rate and calculate the minimum
# monthly payment to pay off the balance within one year. 

from __future__ import print_function

outstanding = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# interest = outstanding * annual_rate / 12
# principal = min_payment - interest 
# balance = outstanding - principal
# outstanding = balance

min_payment = 10

flag = True

while flag:
	temp_outstanding = outstanding
	for month in xrange(1,13):
		interest = temp_outstanding * annual_rate / 12.0
		principal = min_payment - interest
		balance = temp_outstanding - principal
		
		if balance <= 0:
			print("\nRESULT")
			print("Monthly payment to pay off debt in 1 year: %0.2f" % min_payment)
			print("Number of months needed: %d" % month)
			print("Balance: %0.2f" % balance)
			flag = False
			break
		
		temp_outstanding = balance
	
	min_payment += 10
	