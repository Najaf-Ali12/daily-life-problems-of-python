numbers=int(input("enter the number of  total ingredients that you have:"))
recipes=int(input("enter the number of recipes:"))
for i in range(recipes):
    recipe=input(f"enter the name of recipe{i+1}:")
    num=int(input(f"enter the number of ingredients required for {recipe}:"))
    if numbers>num:
        recipe1=0
        while num>0:
            ingredient=input(f"enter the ingredient{num}:")
            amount=int(input(f"enter the amount of {ingredient}:"))
            num-=1
            recipe1+=amount
        print("the total cost of",recipe," is" , recipe1)
    else:
        print("you need",abs(numbers-num)," extra ingredient for",recipe)
    
    

