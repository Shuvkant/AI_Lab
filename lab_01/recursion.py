"""
## Bonus question
-Wap to create a module named "recursion" which has methods to compute the factorial of a number and nth fabonacci term using recursion
"""


def main():
    number = int(input("Enter the factorial number "))
    ansa = factorial(number, 1)
    print(f"The factorial is {ansa}")
    fibo_result = fiboM(number)
    print(f"The fibonacci is {fibo_result}")


def factorial(n, acc):
    if (n == 1 or n == 0):
        return acc
    else:
        return factorial(n-1, n*acc)


table = {}


def fiboM(n):
    if n == 1 or n == 0:
        return 1
    else:
        if n not in table:
            table[n] = fiboM(n-1)+fiboM(n-2)
        return table[n]


if __name__ == "__main__":
    main()
