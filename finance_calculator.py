import math

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