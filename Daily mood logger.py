#create a basic mood logging app.Users can input their mood for the day
#and add a short note.
def mood_app():
    if mood=="happy" or mood=="glad":
        print("to be always happy like today,work hard")
    if mood=="angry":
        print("drink water,sit if you are standing and sleep if you are sitting")
    if mood=="sad"or mood=="upset":
        print("Remember ALLAH,HE will do everything better")
    if mood=="jealous" or mood=="envoy":
        print("you are a perfect person.This is  the best blessing that you have")
mood=input("enter tell your mood today")
mood_app()
        
