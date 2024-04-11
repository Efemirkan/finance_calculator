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
