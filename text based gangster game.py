#make a text based game in which user can play and choose different domains

def home(): #function will bring player in game
    choice=input("what do you want to do in your home,(sleep,exercise,study,or have bath)")
    if choice=="sleep":
        print(name,"don't play game because  you are sleeping")
    elif choice=="exercise":
        print(name,",you are taking exerisse this is good for you health")
    elif choice=="study":
        print("nice",name,"good to prepare for your exams")
    elif choice=="have bath":
        print(name," bath daily like this.It makes you fresh")
    else:
        print(choice,"is  not included in your home")
def hospital(): #function defines entire environment of hospital 
    choice=input(name,"enter what services can you provide in hospital,(be nurse,be ambulance driver)")
    if choice=="be nurse":
        print(name,"a patient needs your help in room 18,go and take his care")
    elif choice=="be ambulance driver":
        print(name,"take the patient to the civil hospital",city)
    else:
        print(choice," is not available at the moment")
def car(): #function defines entire environment of car and directions
    choice=input(f"{name} where you want to go,left or right")
    if choice=="left":
        print("oh no,the car is going into the water")
    elif choice=="right":
        print("oh no police is on the right side")
    else:
        print(name,"you cannot take you car to",choice)
def fight(): #functions shows player in action 
    choice=input(f"{name} which instrument you want to take,(AK47,Pistol,G3,Sniper,knife,kick)")
    if choice=="pistol":
        print(name,",the enemy has died in 6 fires")
    elif choice=="AK47":
        print(name,",enemy died in 4 fires")
    elif choice=="G3":
        print(name,"your two fires ended the enemy")
    elif choice=="sniper":
        print(name,",enemy has died of one fire")
    elif choice=="knife":
        print(name,"keep attecking the enemy is about to die")
    elif choice=="kick":
        print(name,"kick continuously")
    else:
        print(name,"you cannot kill him with",choice)
name=input("tell the name of your player")
city=input("tell the name of city where you want to play")
while True:
    print("welcome to",city,",the city of players")
    print(name,"where you want to go in",city,)
    print("1:home")
    print("2:hospital")
    print("3:car")
    print("4:fight")
    print("5:exit")
    choice=input("what do you want to do?,(enter 1,2,3,4,5)")
    if choice=="1":#take to function of home
        home()
    elif choice=="2": #take to function of hospital
        hospital()
    elif choice=="3": #take to function of car
        car()
    elif choice=="4": #take to function fight
        fight()
    elif choice=="5": #take to exit
        break
    else:          #take back
        print("invalid choice,please try again")
        
    
