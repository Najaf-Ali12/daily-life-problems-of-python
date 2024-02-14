    #LOGICAL PROBLEMS OF CONTROL-FLOW
#1. Write a Python program to check if a given number is positive,
# negative, or zero.
num=int(input("enter a number"))
if num>0:
    print(num,"is a positive number")
elif num==0:
    print(num,"is zero")
else:
    print(num," is a negative number")
# 2. Create a program that asks the user to enter their age and
#prints out whether they are a child,teenager, adult, or senior citizen.
age=int(input("enter how many years old are you"))
if age<18 and age>0:
    print("you are still green")
elif age>=18 and age<=20:
    print("You are teenager")
elif age>20 and age<=60:
    print("You are adult")
elif age>60:
    print("you are a senior citizen")
else:
    print("this age is impossible")
#3. Develop a program that prompts the user to enter two numbers
    # and prints out the larger of the two.
num1=int(input("enter a number"))
num2=int(input("enter a number"))
if num1!=num2:
    if num1>num2:
        print(num1,"is greater than",num2)
    else:
        print(num2,"is greater than ",num1)
#4. Write a Python script to determine whether a given year is a leap year or not.
year=int(input("enter the year"))
if year%4==0:
    print("it is a leap year")
else:
    print("not a leap year")
#5. Implement a program that takes a user's input of three numbers and 
    #prints out the maximum and minimum among them.
n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
if n1>n2: 
    if n3>n1:
        print(n3,"is the maximum number")
    elif n1>n3:
        print(n1,"is the maximum number")
if n2>n1:
    if n3>n2:
        print(n3,"is the maximum number")
    elif n2>n3:
        print(n2,"is the maximum number")
if n1<n2: 
    if n3<n1:
        print(n3,"is the minimum number")
    elif n1<n3:
        print(n1,"is the minimum number")
if n2<n1:
    if n3<n2:
        print(n3,"is the mminimum number")
    elif n2<n3:
        print(n2,"is the minimum number")
totalmarks=int(input("enter your total marks"))
obtainedmarks=int(input("enter your obtained marks"))
if totalmarks>obtainedmarks:
    percent=obtainedmarks*100/totalmarks
    if percent>=90 and percent<100:
        print(" A GRADE")
    if percent>=80 and percent<90:
        print(" B GRADE")
    if percent>=70 and percent<80:
        print(" C GRADE")
    if percent>=60 and percent<70:
        print(" D GRADE")
    if percent<60:
        print(" F GRADE")
