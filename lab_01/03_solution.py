"""
3)WAP to calculate sum, diff, product and quotient between two input numbers using a single
function.
"""
num_one=float(input("Enter the first number "))
num_two=float(input("Enter the second number "))

def operations(num1, num2):
    sum=num1+num2
    diff=num1-num2
    product=num1*num2
    quotient=int(num1/num2)
    print(f"Sum of {num1} and {num2} is {sum}")
    print(f"Difference of {num1} and {num2} is {diff}")
    print(f"Product of {num1} and {num2} is {product}") 
    print(f"Quotient of {num1} and {num2} is {quotient}") 

operations(num_one, num_two)
