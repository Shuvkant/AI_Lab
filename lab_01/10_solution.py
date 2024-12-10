"""
10)WAP program to get the largest number from a list.
    """

numbers =[52,54, 90, 67, 80,11,13,51, 1]
sorted=[]
size=len(numbers)
for i in range(size):
        for j in range(0, size-i-1):
            if(numbers[j]>numbers[j+1]):
                numbers[j], numbers[j+1]=numbers[j+1], numbers[j]
print(f"The largest number is {numbers[size-1]}")
