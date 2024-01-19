#Create a list of numbers or names and sort
#them in ascending or descending order.

numbers = []
n=int(input("enter the number of elements you want to add in list"))
for i in range(n):
    element=int(input("what do you want to add in the list"))
    numbers.append(element)
numbers.sort()  # Sorts in ascending order
print(numbers)  # Output: [1, 2, 5, 8, 9]
print(numbers[::-1]) #sorts in descending order
