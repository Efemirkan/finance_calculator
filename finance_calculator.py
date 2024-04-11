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