#Movie Recommendation System: 
#Create a program that recommends movies based on user preferences. Use variables to store genre,
#rating, and release year. Write expressions to compare movies and suggest matches.
year=int(input("enter your preferred year for your movie(from 1980-2024)"))
genre=input("enter the preferred category for your movie(action/comedy/romantic)")
rating=int(input("entre the preferred rating for your movie(60% to 100%)"))
def action():
    #action movies release year 1980-2000,rating is above 50 and less than70%
    print("here is a list of some movies,preference based on rating so please watch any of them")
    print("1.name=COMMANDO,release year=1985,rating=69%")
    print("2.name=ROBOCOP,release year=1987,rating=68%")
    print("3.name=LOCK UP,release year=1989,rating=67%")
    print("4.name=KICKBOXER,release year=1989,rating=65%")
    print("5.name=THE RUNNING MAN,release year=1987,rating=63%")
    print("6.name=RED HEAT,release year=1988,rating=61%")
    print("7.name=RAW DEAL,release year=1986,rating=60%")
    print("8.name=NAVY SEALS,release year=1990,rating=58%")
    print("9.name=ABOVE THE LAW,release year=1988,rating=57%")
    print("10.name=Demolitian Man,release year=1993,rating=60%")
    print("11.name=Out for Justic,release year=1991, rating=51%")
def comedy():
    #comedy movies release year 1980-2000,rating is above 50 and less than70%
    print("here is list of comedy movies rating is from 50-80%, year of release is from 1980-2000 ")
    print("1.name=Three men and a little lady,release year=1990,rating=63%")
    print("2.name=The great outdoors,release year=1988,rating=64%")
    print("3.name=Junior,release year=1994,rating=60%")
    print("4.name=mixed nuts,release year=1994,rating=60%")
    print("5.name=blank check ,release year=1994,rating=50%")
    print("6.name=Dracula:Dead and loving it,release year=1995,rating=58%")
    print("7.name=Kingpin,release year=1996,rating=50%")
def romantic():
    print("here is list of romantic movies rating is from 50-80%, year of release is from 1980-2000 ")
    print("1.name=Return to me,release year=2000,rating=61%")
    print("2.name=Speechless,release year=1994,rating=50%")
    print("3.name=It could happen to you,release year=1994,rating=71%")
    print("4.name=Forget Paris,release year=1995,rating=56%")
    print("5.name=Only you,release year=1996,rating=56%")
def action_update():
    print("here is list of action movies rating is from 70-100%, year of release is from 2000-2024")
    print("1.name=The dark knight,release year=2008,rating=94%")
    print("2.name=Mad Max:Fury road,release year=2015,rating=90%")
    print("3.name=Inception,release year=2010,rating=87%")
    print("4.name=gladiator,release year=2000,rating=76%")
    print("5.name=the bourne ultimatum,release year=2007,rating=92%")
    print("6.name=Black Panther,release year=2018,rating=96%")
    print("7.name=the revenant,release year=2015,rating=78%")
    print("8.name=The Avengers,release year=2012,rating=92%")
    print("9.name=Mission Impossible-Fallout,release year=2018,rating=97%")
    print("10.name=Spider-man:Into the spider-verse,release year=2018,rating=97%")
def comedy_update():
    print("here is list of comedy movies rating is from 70-100%, year of release is from 2000-2024")
    print("1.name=The grand budapest hotel,release year=2014,rating=91%")
    print("2.name=The Intouchables,release year=2007,rating=75%")
    print("3.name=juno,release year=2007,rating=94%")
    print("4.name=superbad,release year=2007,rating=88%")
    print("5.name=Zootopia,release year=2016,rating=98%")
def romantic_update():
    print("here is list of romantic movies rating is from 70-100%, year of release is from 2000-2024")
    print("1.name=Call me by your name,release year=2017,rating=95%")
    print("1.name=Before sunset,release year=2004,rating=95%")
    print("1.name=Uternal shine of the spotless mind,release year=2004,rating=93%")
    print("1.name=Her,release year=2013,rating=94%")
    print("1.name=Silver lining playbook,release year=2012,rating=92%")
if year>=1980 and year<=2000 and genre.lower()=="action" and rating>=50 and rating<=70:
    action()
if year>=1980 and year<=2000 and genre.lower()=="comedy" and rating>=50 and rating<=70:
    comedy()
if year>=1980 and year<=2000 and genre.lower()=="romantic" and rating>=50 and rating<=70:
    romantic()
if year>=2000 and year<=2024 and genre.lower()=="action" and rating>=70 and rating<=100:
    action_update()
if year>=2000 and year<=2024 and genre.lower()=="comedy" and rating>=70 and rating<=100:
    comedy_update()
if year>=2000 and year<=2024 and genre.lower()=="romantic" and rating>=70 and rating<=100:
    romantic_update()
    


   

    
    

