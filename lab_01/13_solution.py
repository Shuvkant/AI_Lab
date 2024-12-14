"""
13) You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.
    """
user_input_string=str(input("Enter a string "))
def swap_string(string):
    return string.swapcase()

swapped_string=swap_string(user_input_string)
print(f"Original String= {user_input_string}")
print(f"Swapped String= {swapped_string}")
