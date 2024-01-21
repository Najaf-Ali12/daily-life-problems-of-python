#make a programme that will take geometric mean of n numbers
#using for loop
num=int(input("enter the number of numbers"))
p=1
for i in range(num):
    digit=int(input("enter the digit"))
    p=p*digit #it takes product of digits 
GM=pow(p,1/num)#mathematically GM=product of digits whole power 1/number of digits
print("the geometric mean of n numbers is ",GM)

#using while loop
number=int(input("enter number of numbers"))
t=0
product=1
while t<number:
    digit=int(input("enter the number"))
    t+=1
    product=product*digit
G_mean=pow(p,1/number)  #syntax of pow function is pow(number,power)
print("the geometric mean of ",number,"numbers is" ,G_mean)
    
