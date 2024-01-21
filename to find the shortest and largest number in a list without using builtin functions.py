#Python program to find the largest number
#in a list without using built-in functions
numbers=[1,2,3,4,7,8,99,9,6,5,12,45]
biggest=numbers[0] #it is not compulsory to keep zero here, any value can be kept
for i in numbers:  #each member will be assigned to i individually
    if i>biggest:
        biggest=i
print("largest number in ",numbers,"is ",biggest)


#Python program to find the shortest number
#in a list without using built-in functions
numbers=[3,2,0,9,8,0,9,47,8,9]
smallest=numbers[9]
for i in numbers:
    if i<smallest:
        smallest=i
print("the shortest number in ",numbers,"is",smallest)

