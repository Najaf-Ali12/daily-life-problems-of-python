#Question 3: Ride-Sharing Fare Calculator
#You are working on a Ride-Sharing Fare Calculator.
#Develop a Python function calculate_fare(distance, time_of_day)
#that takes the distance of the ride and the time of
#day as input and returns the fare. Apply a 20% surcharge
#during peak hours (8 am - 10 am and 5 pm - 7 pm) and a
#10% discount for late-night rides (10 pm - 5 am).

def calculate_fare(dis,time):
    fare = dis * 5
    hour = time.split()
    hour = int(hour[0])
    if time in ['8 am','9 am','10 am'] or time in ['5 pm','6 pm','7 pm']:
        fare += (fare * 0.2)
        return f'{fare} dollars'
    elif time in ['10 pm','11 pm','12 am','1 am','2 am','3 am','4 am','5 am']:
        fare -= (fare * 0.1)
        return f'{fare} dollars'
    else:
        return f'{fare} dollars'

distance = int(input('Enter distance in kms : '))
time_day = input('Enter time in hours : ')
time_day.lower()
print(calculate_fare(distance,time_day))

