balance =100
annualInterestRate = 0.2

monthlyPayment = 10
monthlyInterestRate = annualInterestRate/12
newbalance = balance


while newbalance > 0:
        monthlyPayment += 10
        newbalance = balance
        month = 0
        #checking for each month from 10 till max
        while month < 12 and newbalance > 0:

            month += 1
            interest = monthlyInterestRate * newbalance
            newbalance -= monthlyPayment
            newbalance += interest

newbalance = round(newbalance,2)
