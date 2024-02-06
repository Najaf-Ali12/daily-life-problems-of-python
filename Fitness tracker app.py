#Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps,
# distance walked, and calories burned. 
#Write expressions to calculate average steps per week and total distance covered in a month.
sum=0
calorie=int(input("enter that how many calories were burnt"))
for i in range(1,31):
    distance=int(input(f"enter the distance covered on day{i}:"))
    sum+=distance
print(f"total distance covered in a month is {sum}")
for j in range(7):
    step=int(input(f"enter the steps covered on day{j+1}:"))
    sum+=step
print(f"the average steps per week are {sum/7}")
    

    