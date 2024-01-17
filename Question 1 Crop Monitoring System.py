#Question 1: Crop Monitoring System
#Imagine you are developing a Crop Monitoring System for farmers.
#Write a Python function monitor_crop(temperature, humidity, rainfall)
#that takes environmental conditions as input and returns "Watering needed"
#if the humidity is low and rainfall is below average, and "Optimal conditions" otherwise.
def crop_monitor(x,y,z):
    if humidity=="low" and rainfall=="below":
        return "watering needed"
    else:
        return "optimal conditions"
temperature=int(input("enter the temperature in degree celsius"))
humidity=input("tell whether the humidity is low or high")
rainfall=input("enter whether the rainfall is below or above average")
t=crop_monitor(temperature,humidity,rainfall)
print(t)
