#product of n natural number using functions and
#1:for loop
def pro():
 product=1
 num=int(input("enter the number of real numbers"))
 for i in range(1,num+1): #it will take digit num times
     digit=int(input(f"enter your real number at place {i}:"))
     product=product*digit
 print("product of ",num,"real numbers is ",product)
pro()


#2:while loop
def product(x):
    pro=1
    t=number
    while t!=0:
        digit=int(input("enter the digit"))
        t-=1
        pro=pro*digit
    return pro
number=int(input("enter the number of real numbers"))
store=product(number) #store will store value that return function will return
print("product of ",number,"real numbers is",store)
        
        
