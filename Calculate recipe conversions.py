#Calculate recipe conversions: Write a program to convert between
#units like teaspoons and tablespoons, grams and ounces, for easier cooking.
def gram_ounce():
    
   change_in=input("enter in which unit of measurement you want to convert{gram,ounce}")
   change_from=input("enter from which unit of measurement you want to convert{gram,ounce}")

   if change_in=="ounce" and change_from=="gram":
       grams=int(input("enter the grams you want to convert in grams"))
       print(grams,"grams = ",grams/28.349,"ounces")
   if change_in=="gram" and change_from=="ounce":
       ounce=int(input("enter the ounces you want to convert in grams"))
       print(ounce,"ounces =",ounce*28.349,"grams")
def tea_tablespoon():
    
   change_in=input("enter in which unit of measurement you want to convert{teaspoon,tablespoon}")
   change_from=input("enter from which unit of measurement you want to convert{teaspoon,tablespoon}")
    
   if change_in=="teaspoon" and change_from=="tablespoon":
       tablespoon=int(input("enter the tablespoons you want to convert in teaspoons"))
       print(tablespoon,"tablespoon = ",tablespoon*3,"teaspoon")
   if change_in=="tablespoon" and change_from=="teaspoon":
       teaspoon=int(input("enter the teaspoons you want to convert in tablespoons"))
       print(teaspoon,"teaspoons =",teaspoon/3,"tablespoons")
while True:
    print("\ cooking unit converator")
    print("1. gram to ounce and viceversa")
    print("2. teaspoon to tablespoon and vice versa")
    print("3. Exit")
    choice=input("which conversion you want?(enter 1,2 or 3)")
    if choice =="1": #will call gram ouncce function
        gram_ounce()
    if choice=="2":   #will call tea tablespoon function
        tea_tablespoon()
    if choice=="3":
        break     #exit the code
    elif choice not in ("1","2","3"):
        print("invalid choice,please try again")



