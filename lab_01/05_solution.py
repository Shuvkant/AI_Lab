"""
5)WAP to enter the marks of 10 students and display it.
"""
marks=[]
for i in range(1,11):
    mark=float(input(f"Enter the mark of {i} student "))
    marks.append(mark)

print(marks)
