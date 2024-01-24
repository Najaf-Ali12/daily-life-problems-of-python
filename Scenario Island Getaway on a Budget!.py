#Scenario: Island Getaway on a Budget!
#You're a travel consultant for budget-conscious globetrotters,
#and Maya, a recent graduate, wants to book a dream vacation to Bali for
#two weeks next summer. She has some flexibility with her travel dates and is looking for the
#absolute cheapest flight option. Help Maya find the
#perfect flight deal by creating a Python function
#find_cheapest_flight(destination, flexibility_days, budget, preferred_airlines).
#Conditions:
# Destination: Set to "Bali" for this scenario.
# Flexibility Days: Maya can adjust her travel dates by this number of days (e.g., +/- 3 days).
# Budget: Maya's maximum budget for round-trip flights is $2,000.
# Preferred Airlines: Maya has some favorite airlines (e.g., Garuda Indonesia, Singapore Airlines),
#but is open to other options if they're significantly cheaper.
#Additional Considerations:
# Use if-else statements to compare prices from different airlines and booking platforms for various
#departure and return dates within the flexibility range.
# Implement a loop to iterate through these dates and find the flights that fall within Maya's budget.
# If multiple flights meet the budget criteria, prioritize options from preferred airlines (using nested if statements).
# Consider incorporating additional factors like baggage allowance, layover duration, and overall flight rating to refine the recommendations.
#Bonus:
# Display the top 3 cheapest flight options along with their details (airline, price, dates) for Maya to compare.
# Allow Maya to specify preferred airports or stopover cities if desired.
#By solving this problem, you will practice using functions,
#conditionals, loops, and data manipulation in a real-world travel scenario.
#You'll also develop problem-solving skills by considering various factors and optimizing your code for efficiency.
def find_cheapest_flight(destination,flexibility_days,budget,preferred_airlines):
           if price<1500 and price>1000:
               if  startdate==10:
                   if airline.lower()=="garuda indonesia" or airline.lower()=="singapore airlines":
                       print("this is the best oportunity you can avail")
                   else:
                       print("this is the best oportunity because focus on vacations not on flight")
               elif startdate>10 and startdate<=13 or startdate>=7:
                   print("good option and time is also in range")
               else:
                   print(f"Maya is not available on{startdate}")
           elif price>1500 and price<=2000:
               if  startdate==10:
                   if airline.lower()=="garuda indonesia" or airline.lowe=="singapore airlines":
                       print("this is the best oportunity you can avail")
                   else:
                       print("this is the best oportunity because focus on vacations not on flight")
               elif startdate>10 and startdate<=13 or startdate>=7:
                   print("good option and time is also in range")
               print("it is expensive but not out of range,so i suggest you to buy it")
           else:
               print(price,"dollars  are out of range of maya")
destination="bali"
price=int(input("enter the price of round trip flights"))
startdate=int(input("enter that on which date of june 2024 trip starts"))
enddate=startdate+15,"of june 2024"
airline=input("enter the name of airline available")
find_cheapest_flight(destination,startdate,price,airline)


                      
#startdate=jun10 ,enddate=20+startdate
#budget=2000
#garuda indonesia ,singapore airlines
