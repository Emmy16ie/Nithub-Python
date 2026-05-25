# Write a function called divide_or_square that takes one argument (a
# number), and returns the square root of the number if it is divisible by
# 5, returns its remainder if it is not divisible by 5. For example, if you
# pass 10 as an argument, then your function should return 3.16 as the
# square root.

# Check if num is divisible by 5
# if no: Do num mod 5 and return reult
# if yes: Do square root num and return result
# P.S: Number Restricted to positive integers 

def divide_or_square(num):
    # # Handling restrictions:
    # if num < 0:
    #     return "Positive Integers Only"
    # Check divisibility condition: Is Num divisible by 5 ?
    if num % 5 == 0: # if yes:
        return f"{num} is divisible by 5, the square root of {num} is: {((num) ** 0.5)}"
    else: # if No 
        return f"{num} is not divisoble by 5, the remainder after dividing {num} by 5 is {(num % 5)}"
    
try:
    number = int(input("Input your number(Integers Only): "))
    print(divide_or_square(number))
except ValueError:
    print("Input a Number!")






