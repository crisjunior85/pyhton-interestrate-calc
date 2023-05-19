#basic interest rate calculator
#collect the necessary input: principal, apr, years
#caclculate the monthly payment
#show to the user

def main():
    print("This is monthly payment loan calculator")
    print("")

    principal = float("Input the loan amount: ")
    apr = float(input("Inpout the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_month))) 
    
    print(" The monthly payment for this loan is: $%.2f" % monthly_payment)  #the %.2f rounds off into 2 decimal points

main()
