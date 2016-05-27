# Problem Set 1
# Name: Markell
# Collaborators: N/A
# Time Spent: 30 mins
#

from __future__ import print_function

outstanding = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
min_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

# First we calculate the monthly payment: month_pay = min_payment_rate * outstanding
# Second we calculate the monthly interest: interest_pay = outstanding * annual_rate / 12
# Third calculate the prinicipal paid: principal = month_pay - interest_pay
# Finally calculate the remaining balance: remaining = outstanding - principal

total_amount = 0
for x in xrange(1,13):
  print("Month: %i" % x)
  month_pay = round(min_payment_rate * outstanding, 2)
  total_amount += month_pay
  
  print("Minimum monthly payment: $%0.2f" % month_pay)
  interest_pay = round(outstanding * annual_rate / 12, 2)
  principal = month_pay - interest_pay
  
  print("Principal paid: $%0.2f" % principal)
  remaining = outstanding - principal
  
  print("Remaining balance: $%0.2f" % remaining)
  outstanding = remaining
  
print("\nRESULT")
print("Total amount paid: $%0.2f" % total_amount)
print("Remaining balance: $%0.2f" % remaining)
