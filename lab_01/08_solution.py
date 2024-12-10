"""
8)WAP to sort the list {5, 4, 11, 13, 51}
    """
numbers =[52,4,11,13,51, 1]
sorted=[]
size=len(numbers)
print(f"size is {size}")
for i in range(size):
        for j in range(0, size-i-1):
            if(numbers[j]>numbers[j+1]):
                numbers[j], numbers[j+1]=numbers[j+1], numbers[j]
                print(numbers)
    
print(f"Final answer is {numbers}")
