"""
4)WAP to display prime numbers from 1 to 100 
"""
initial_range=int(input("Enter the initial_range "))
final_range=int(input("Enter the final range "))
def prime_checker(number):
    if(number<2):
        return False
    if(number==int(2)):
        return True
    if(number%2==0):
        return False
    for i in range(3, int(number**0.5)+1,2 ):
        if(number%i==0):
            return False
    return True

print(f"The prime numbers from {initial_range} to {final_range}  are ")
for n in range(initial_range, final_range+1):
    if prime_checker(n):
        print(n, end=" ")

