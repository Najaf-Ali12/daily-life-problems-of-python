    #HEALTHY LIFE STYLE
#2. Sleep Tracker: Create a program that asks the user for their bedtime and 
#wake-up time, then calculates their total sleep duration. Use if statements
#to determine if they met the recommended sleep amount and provide feedback accordingly.
bedtime=int(input("enter your sleeping time"))
wakeup=int(input("enter your wakeup time"))
duration=abs(wakeup+(12-bedtime))
print("you slept for",duration,"hours")
if duration>5 and duration<=7:
    print("your sleeping duration is healthy")
if duration>7:
   print("Don't sleep too much it is not good for you")
if duration<=5:
    print("sleep more without sufficient sleep your body will not work properly")
#3. Hydration Helper: Design a program that prompts the user for their
#weight and desired level of hydration (e.g., light, moderate, 
#intense exercise). Use nested if-else statements to suggest the amount of 
#water they should drink throughout the day.
weight=int(input("enter your weight(45,54,64,73,82,91,100,109,118)"))
hydration=float(input("how many litres of water you have daily"))
if (weight==36 and hydration==1.2 or
weight==45 and hydration==1.5 or 
weight==54 and hydration==1.8 or
weight==64 and hydration==2.1 or
weight==73 and hydration==2.4 or
weight==82 and hydration==2.7 or
weight==91 and hydration==3.0 or
weight==100 and hydration==3.3 or
weight==109 and hydration==3.6 or
weight==118 and hydration==3.9):
    print("your hydration level is good")
if (weight==36 and hydration<1.2  or
weight==45 and hydration>1.2 and hydration<1.5 or 
weight==54 and hydration<1.8 and hydration>1.5 or
weight==64 and hydration<2.1 and hydration>1.8 or
weight==73 and hydration<2.4 and hydration>2.1 or
weight==82 and hydration<2.7 and hydration>2.4 or
weight==91 and hydration<3.0 and hydration>2.7 or
weight==100 and hydration<3.3 and hydration>3.0 or
weight==109 and hydration<3.6 and hydration>3.3 or
weight==118 and hydration<3.9 and hydration>3.6):
    print("hydration level is low,need more water ")
                