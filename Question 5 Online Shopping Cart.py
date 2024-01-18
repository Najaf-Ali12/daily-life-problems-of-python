#given by sir owais for mid preparation
#Question 5: Online Shopping Cart 
#Develop a Python program for an OnlineShopping Cart.
#Create a function checkout(cart_total) that takes the
#total cost of items in the cart and applies a discount
#based on the user's membership level. Regular members get
#a 5% discount, premium members get a 10% discount, and VIP members get a 15% discount.
def checkout(v):
    if member=="regular":
        return totalcost-(totalcost*0.05)
    if member=="premium":
        return totalcost-(totalcost*0.1)
    if member=="VIP":
        return totalcost-(totalcost*1.5)
totalcost=int(input("enter the total cost of items in the cart"))
member=input('enter whether the customer is regular,premium or VIP member of our store')
t=checkout(totalcost)
print("your total bill is ",totalcost)
print("as you are our ",member,"member,so,you will pay:",t)
