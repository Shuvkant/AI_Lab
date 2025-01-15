"""
2)WAP to input the percentage and display the division
"""

percentage=float(input("Enter the percentage "))
if(percentage>=80):
    print(f"You secured Distinction with: {percentage}%")
elif(percentage>=65):
    print(f"You secured First Division with: {percentage}%") 
elif(percentage>=55):
    print(f"You secured Second Division with: {percentage}%") 
elif(percentage>=40):
    print(f"You secured Third Division with: {percentage}%") 
else:
    print(f"You are failed with :{percentage}%")

