#Shopping List: Write a program to manage a shopping list. Use variables to store item names,
#quantities, and prices.Calculate the total cost of items and check if you have enough budget.
shopping_list=[]
total=0
budget=int(input("enter your budget here"))
number=int(input("enter the number of items you want to add in your shopping list"))
for  i in range(number):
    name=input(f"enter the name of item {i+1}:")
    shopping_list.append(name)
    quantity=int(input(f"enter the quantity of {name}:"))
    price=int(input(f"enter the price of one {name}:"))
    bill=quantity*price
    print(f"bill of {name} is {bill}")
    total+=bill
print(f"your shopping list is {shopping_list}")
print(f"total bill of items in list is {total}")
if total>budget:
    print(f"You should increase your budget because your budget is {budget} and total bill is {total}")
else:
    print("You have enough budget")
