"""
12)WAP to find the sum of all items in a dictionary
"""

def sum_of_dictionary(dictionary):
    return sum(dictionary.values())

mydict1={'a': 100, 'b':200, 'c':300}
mydict2={'x': 25, 'y':18, 'z':45}
total_sum={}

for i in range(1,3):
    if(i==1):
        currentdict=mydict1
    else:
        currentdict=mydict2
    total_sum[i]=sum_of_dictionary(currentdict)
    print(f"The total sum of dictionary {currentdict} is {total_sum[i]}")


