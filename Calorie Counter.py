#1. Calorie Counter: Write a program that asks the user for their age,
# weight, and activity level, then calculates their daily calorie goal
# based on recommended guidelines. Use if-else statements to adjust the 
#goal based on the user's activity level.
age=int(input("enter your age"))
weight=int(input("enter your weight in kilograms"))
activity_level=int(input("enter your activity level percentage")) 
if activity_level>0 and activity_level<=30:
    print("no need to burn a lot of calorie:")
if activity_level>30 and activity_level<=60:
    print("burn your calorie in medium level so that the fat not disturbs you")
else:
    print("burn too much calories as you have have to work a lot")