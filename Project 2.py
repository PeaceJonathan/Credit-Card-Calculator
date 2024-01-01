#Jonathan Peace

#Source Code

 

import math

maxInterestRate = 18.5 #global value

def main():
    while True:
        choice = displayMenu()
        if choice == '1':
            cardType = applyForCard()
            if cardType == 0:  #Not Approved
                print(f"Sorry, you are not approved for any credit card\n")
            else:  # Are Approved
                print(f"Congrats, you have been approved for the {cardType} credit card\n")
        elif choice == '2':
            monthlyPayment = getMonthlyLoanPayment()
            print(f"Monthly loan payment: ${monthlyPayment:.2f}\n")
        elif choice == '3':
            maturityValue = getIRAMaturity()
            print(f"Your IRA Maturity Value is: ${maturityValue:.2f}\n")
        elif choice.upper() == 'Q':
            print("Goodbye")
            break
        else:
            print(f"Invalid selection. Please choose a valid option \n")

def displayMenu():  #Menu Inputs
    print(f"Menu:\n")
    print("1. Apply for a Credit Card")
    print("2. Calculate Monthly Loan Payments")
    print("3. Calculate Maturity Value of an IRA")
    print(f"Q. Quit\n")
    return input("Please Enter your choice: ")

def applyForCard():  
    while True:
        try:
            accountBalance = int(input("Enter your account balance: $"))
            
            if accountBalance < 0:  
                print(f"Account balance cannot be negative. Please enter a positive number\n")
            else:
                cardType = 0  # Not Approved
                if accountBalance >= 15000:
                    cardType = "Platinum" 
                elif accountBalance >= 10000:
                    cardType = "Gold"  
                elif accountBalance >= 5000:
                    cardType = "Silver"  
                return cardType
        except ValueError:
            print(f"Please enter a valid positive number\n")


def getMonthlyLoanPayment():
    while True:
#Years
        years_input = input("Enter the number of years until loan maturity (default is 30 years): ")
        if not years_input:
            years = 30  # Set years to 30 with no input
        else:
            years = int(years_input)
        
        if years < 0:  
            print(f"Years until maturity cannot be negative. Please enter a non-negative number.\n")
            continue  
#Principal        
        principal_input = input("Enter the loan amount (Principal): $")
        try:
            principal = float(principal_input)
            if principal <= 0:
                print(f"Principal amount must be greater than zero. Please enter a valid amount.\n")
                continue
        except ValueError:
            print(f"Please enter a valid principal amount.\n")
            continue
#Rate        
        interestRate_input = input(f"Enter the annual interest rate (max {maxInterestRate}%): ")
        try:
            interestRate = float(interestRate_input)
            if interestRate < 0 or interestRate > maxInterestRate:
                print(f"Interest rate must be non-negative and not exceed the maximum rate. Please enter a valid rate.\n")
                continue
        except ValueError:
            print(f"Please enter a valid interest rate.\n")
            continue
            
        return calcMonthlyLoanPayment(principal, interestRate / 100, years)

def calcMonthlyLoanPayment(principal, interestRate, numYears=30):
    monthlyRate = interestRate / 12
    monthlyPayment = (principal * monthlyRate) / (1 - math.pow((1 + monthlyRate), (-12 * numYears)))  #Calculation
    return monthlyPayment

def getIRAMaturity():
#Age
    currentAge = int(input("Enter your current age: "))
    if currentAge >= 65 or currentAge < 0:
        print(f"You must be less than 65 years old and a valid age\n")
        return getIRAMaturity()
    
    yearsUntilMaturity = 65 - currentAge
    
#Desposit    
    annualDeposit = float(input("Enter the amount of annual deposit (up to $2,000): $"))
    if annualDeposit < 0 or annualDeposit > 2000:
        print(f"Please enter a valid number\n")
        return getIRAMaturity()

#Rate    
    interestRate = float(input(f"Enter the annual interest rate (max {maxInterestRate}%): "))
    if interestRate < 0 or interestRate > maxInterestRate:
        print(f"Please enter a valid number\n")
        return getIRAMaturity()
    
    maturityValue = calcIRAMaturity(yearsUntilMaturity, annualDeposit, interestRate / 100)
    return maturityValue

def calcIRAMaturity(yearsUntilMaturity, annualDepositAmt, interestRate):
    maturityValue = annualDepositAmt * ((math.pow((1 + interestRate), yearsUntilMaturity) - 1) / interestRate) #Calculation
    return maturityValue


main()

