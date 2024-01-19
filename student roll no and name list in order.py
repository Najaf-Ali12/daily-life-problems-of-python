numbers = []
n=int(input("enter the number of elements you want to add in list"))
for i in range(n):
    student=input("enter name you want to add in the list")
    rollno=input(f"enter the roll no of {student}")
    numbers.append(student)
    numbers.append(rollno)
numbers.sort()
print(numbers,"is in ascending order")
print(numbers[::-1],"is in descending order")


