loan = 1000
year = 10

print ("Loan Calculator")
print ("")
print ("$", loan,"over 10 years at 5% APR")
print ("")



for year in range (10):
  loan = loan*1.05
  print("Year", year+1, "is", round(loan,2))

loan = loan-1000
print ("You paid back $", round(loan,2), "in interest!")