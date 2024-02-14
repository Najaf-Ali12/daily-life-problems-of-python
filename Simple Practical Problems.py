#Simple Practical Problems:
#1. Design a Python program that calculates the total cost of items
# purchased by a customer based on the provided unit price and quantity,
#applying a discount of 10% if the total cost exceeds $1000.
item=input("enter the name of item")
unitprice=int(input(f"enter the price of one piece of {item}"))
quantity=int(input(f"enter the quantity of {item}"))
totalprice=unitprice*quantity
print("the total cost of ",item, "is ",totalprice)
if totalprice>1000:
    discount=10*totalprice/100
    print("your discounted price is ",totalprice-discount)
#2. Develop a program that prompts the user to enter their current 
#temperature in Celsius and prints out whether they should wear
#a jacket(if temperature is below 20°C) or not.
temp=int(input("enter your surrounding temperature in celsius"))
if temp<20:
    print("it is good to wear a jacket at",temp,"'C temperature")
else:
    print("no need to wear jacket at",temp,"'C temperature")
#3. Write a Python script that takes a user's input of three sides of a 
#triangle and determines whether it is equilateral, isosceles, or scalene.
side1=int(input("enter the length of hypotenous"))
side2=int(input("enter the length of base"))
side3=int(input("enter the length of perpendiculur"))
if side1!=0 and side2!=0 and side3!=0:
    if side1==side2==side3: #equilateral triangel=whose length of all sides is equal
        print("the triangle is an equilateral triangle")
    if side1!=side2!=side3: #scalene=whose length of all sides is not equal 
        print("the triangle is an scalene triangle")
    else: #isosceles=whose length of two sides is equal 
        print("the triangle is an isosceles triangle")
else:
    print("is not a triangle")
#4. Create a program that simulates a simple ATM machine.
#It should ask the user for their PIN, verify it, and
# then allow them to withdraw money if the balance is sufficient.
account1=int(input("enter the total amount in your account"))
account2=int(input("enter the amount you want to withdraw"))
pin=int(input("enter your 8 digit pin"))
if pin==12345678:
    if account1>account2:
        print("withdrew successfully")
        print("now your have",account1-account2,"amount in your account")
    else:
        print("you donot have sufficient amount in your account")
else:
    print("an incorrect pin was entered")
#5.Develop a Python script that takes a user's input of a month 
#(as a number) and prints out the number of days in that month
year={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
month=int(input("enter the number of a month")) 
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("there are total 31 days in ",year[month])
elif month==2:
    print("there are 28 days in",year[month])
elif month==4 or month==6 or month==9 or month==11:
    print("there are 30 days in",year[month])
else:
    print("there are only 12 months in a year")
# 6.Implement a program that takes a user's input of a year and month and 
#prints out the number of days in that month,considering leap years.
year={
   1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
years=int(input("enter the year"))
month=int(input("enter the number of a month")) 
if years%4==0 and years!=0:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("there are total 31 days in ",year[month])
    elif month==2:
        print("there are 29 days in",year[month])
    elif month==4 or month==6 or month==9 or month==11:
        print("there are 30 days in",year[month])
    else:
        print("there are only 12 months in a year")
if years%4!=0 and years!=0:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("there are total 31 days in ",year[month])
    elif month==2:
        print("there are 28 days in",year[month])
    elif month==4 or month==6 or month==9 or month==11:
        print("there are 30 days in",year[month])
    else:
        print("there are only 12 months in a year")


