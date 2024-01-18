#given by sir owais for the preparation of mid term
#Question 6: Weather App 
#Imagine building a Weather App.
#Write a function weather_advice(temperature, precipitation)
#that provides advice based on the current weather conditions.
#If it's hot and sunny, suggest wearing sunscreen; if it's raining,
#recommend carrying an umbrella; and if it's cold, suggest dressing warmly.
def weather_advice(x,y):
    if temp=="hot" and precipitation=="sunny":
        print("wear sunscreens for the safety of your eyes")
    if precipitation=="raining":
        print("take umbrella to be safe from rain water")
    if temp=="cold":
        print("dress warmly")
    if precipitation=="raining" and temp=="cold":
        print("dress warmly and carry an umbrella")
temp=input("enter whether it is hot or cold")
precipitation=input("enter whether it is sunny or raining")
weather_advice(temp,precipitation)

    
