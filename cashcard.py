balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minimum_monthly_payment = balance * monthlyPaymentRate
month = 1

while month < 13:
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(minimum_monthly_payment, 2))
    balance = (balance - (balance*monthlyPaymentRate))*(1+(annualInterestRate/12))
    minimum_monthly_payment = balance * monthlyPaymentRate
    print "Remaining balance: " + str(round(balance, 2))
    month += 1
