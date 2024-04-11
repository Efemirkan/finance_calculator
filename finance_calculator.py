import math

def main():

    print("""
Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan

""")

    # Take user's input
    user_choice = string_exception("investment", "bond")

    # If user chooses "investment"
    if user_choice == "investment":

        # Take user's inputs
        deposit = numeric_exceptions("How much would you like to deposit? ")
        rate_investment = numeric_exceptions("Enter the interest rate: ")
        year = numeric_exceptions("How many years are you planing to interest? ")
        print("""
- Simple interest is continually calculated on the initial amount invested and
is only calculated once per year.
- Compound interest is different, in that the interest is calculated on the
current total known as the accumulated amount.
""")
        interest_type = string_exception("simple", "compound")

        # If user chooses "simple"
        if interest_type == "simple":

            # Call simple_interest function to calculate simple interest then print as formatted
            simple_interest_value = simple_interest(deposit, rate_investment, year)             
            print(f"The amount of interest you'll earn on your investment: {simple_interest_value:,.3f}")

        # If user chooses "compound"    
        else:

            # Call compound_interest function to calculate compound interest then print print as formatted        
            compound_interest_value = compound_interest(deposit, rate_investment, year) 
            print(f"The amount of interest you'll earn on your investment: {compound_interest_value:,.3f}")

    # If user chooses "bond" 
    else:

        # Take user's inputs
        house_value = numeric_exceptions("How much is house\'s present value? ")
        rate_bond =  numeric_exceptions("Enter the interest rate: ")
        months =  numeric_exceptions("How many months are you planning of taking repayment? ")
        
        # Call repayment function to calculate repayment then print as formatted   
        repayment_value = repayment(house_value, rate_bond, months)   
        print(f"You will have to repay each month: {repayment_value:,.3f}")

# Define simple_interest(p, r, t) function to calculate simple interest 
def simple_interest(p, r, t):

    '''         
    "t" is the number of years that the money is being invested.
    "P" is the amount that the user deposits.
    "r" is the interest.
    "A" is the total amount once the interest has been applied.
    '''
    # 𝐴 = 𝑃(1 + 𝑟 × 𝑡) formula 
    return p * (1 + ((r / 100) * t))

def compound_interest(p, r, t):

    '''         
    "t" is the number of years that the money is being invested.
    "P" is the amount that the user deposits.
    "r" is the interest.
    "A" is the total amount once the interest has been applied.
    '''
    # 𝐴 = 𝑃(1 + 𝑟)**𝑡 formula 
    return p * math.pow((1 + (r / 100)), t)

# Define repayment(p, i, n) function to calculate repayment
def repayment(p, i, n):

    '''         
    "n" is the number of months over which the bond will be repaid.
    "P" is the present value of the house.
    "i" is the monthly interest rate
    '''
    # repayment = (i * P)/(1 - (1 + i)**(-n)) formula
    return ((i / 1200) * p) / (1 - math.pow((1 + (i / 1200)), -n))

# Define string_exception(option_1, option_2) funtion to handle exceptions releated to ValueError 
def string_exception(option_1, option_2):

    # While loop to ask user continuesly until they enter required input
    while True:
    # Take user's input and case-insensitive
        try:
            user_choice = input(f"Enter either '{option_1}' or '{option_2}' from the menu above to proceed: ").lower()
            
            # If user's input not "investment" or "bond" raise ValueError otherwise return option value
            if user_choice not in [option_1, option_2]:
                raise ValueError(f"PLease enter ONLY '{option_1}' or '{option_2}'")
            
            return user_choice
    
        # Print ValueError message
        except ValueError as e:
            print(e) 

# Define numeric_exceptions(prompt) funtion to handle exceptions releated to ValueError
def numeric_exceptions(prompt):

    # While loop to ask user continuesly until they enter required input
    while True:

        # Take user's input
        try:
            user_input = float(input(prompt))
            return user_input
        # Handle expection ValueError and Print error message
        except ValueError:
            print("PLease enter a number of value")

if __name__ == "__main__":
    main()