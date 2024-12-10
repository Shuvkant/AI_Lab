"""
4)WAP to display prime numbers from 1 to 100 
"""
initial_range=int(input("Enter the initial_range "))
final_range=int(input("Enter the final range "))
def prime_checker(number):
    if(number<2):
        return False
    for i in range(2, int(number**0.5)+1, 1):
        if(number%i==0):
            return False
    return True

print(f"The prime numbers from {initial_range} to {final_range}  are ")
for n in range(initial_range, final_range+1):
    if prime_checker(n):
        print(n, end=" ")

