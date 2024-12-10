"""
6)WAP to calculate the factorial of an input number.
"""
factorial_number=int(input(f"Enter the number "))
def find_factorial(number):
    if(number==0 or number==1):
        return 1
    else:
        return number*find_factorial(number-1)
#result=find_factorial()
print(f"The factorial of {factorial_number} is {find_factorial(factorial_number)}")

