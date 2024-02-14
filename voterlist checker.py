voter_submitted_list=[]
num=int(input("enter the number of total voters given in list:"))
for i in range(num+50):
    voterlist={
    "4120195916339":{"S.No":1,"name":"Najaf ali","father name":"Ghulam Mustafa",
                     "Adress":"Alkhani street Dadu","Ward":4,
                     "poling staton":"Village Sijawal khan Alkhani"},
    "4120123259769":{"S.No":2,"name":"Ghulam Mustafa","father name":"Timoo Alkhani",
                     "Adress":"Alkhani street Dadu","Ward":4,
                     "poling staton":"Village Sijawal khan Alkhani"},
    "4120209234071":{"S.No":3,"name":"Timoo Alkhani","father name":"Atta Muhammad Alkhani",
                     "Adress":"Alkhani street Dadu","Ward":4,
                     "poling staton":"Village Sijawal khan Alkhani"}}
    card=input("enter the CNIC of the voter,(without dashes):")
    if len(card)==13: #will check CNIC validity
        if card in voterlist: #will search card presence in voter list
            if card not in voter_submitted_list:  #will check card absense in voter_submitted list
                print(voterlist[card])
                voter_submitted_list.append(card)
            else:  #will not allow to give receipt again to the same person
                print(card,"has already taken the receipt")
        else:  #will tell that the card is not present in voter list
            print(card,"is not in the voter list")
    else: #will aware user of his mistake
        print("please enter correct card number")
