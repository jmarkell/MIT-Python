# Problem Set 1
# Name: Markell
# Collaborators: N/A
# Time Spent:
#

from __future__ import print_function

outstanding = raw_input("Enter the outstanding balance on your credit card: ")
annual_rate = raw_input("Enter the annual credit card interest rate as a decimal: ")
min_payment_rate = raw_input("Enter the minimum monthly payment rate as a decimal: ")

# First we calculate the monthly payment: month_pay = min_payment_rate * outstanding
# Second we calculate the monthly interest: interest_pay = outstanding * annual_rate / 12
# Third calculate the prinicipal paid: principal = month_pay - interest_pay
# Finally calculate the remaining balance: remaining = outstanding - principal

total_amount = 0
for x in xrange(12):
  print("Month: %i" % x)
  month_pay = min_payment_rate * outstanding
  total_amount += month_pay
  
  print("Minimum monthly payment: $%d" % month_pay)
  interest_pay = outstanding * annual_rate / 12
  principal = month_pay - interest_pay
  
  print("Principal paid: $%d" % principal)
  remaining = outstanding - principal
  
  print("Remaining balance: $%d" % remaining)
  outstanding = remaining
  
print("RESULT\n")
print("Total amount paid: $%d" % total_amount)
print("Remaining balance: $%d" % remaining)
