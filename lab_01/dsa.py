from recursion import factorial, fiboM

number = int(input("Enter the factorial number "))
resultfactorial = factorial(number, 1)
print(f"The result is {resultfactorial}")
fab_res = fiboM(number)
print(f"The result for fibonacii is {fab_res}")
