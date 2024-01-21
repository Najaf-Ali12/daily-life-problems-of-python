#find the average of n numbers where n is inputted by user
#using for loop
num=int(input("enter the number of digits whose average you want"))
s=0 # s variable will store sum of numbers
for i in range(num): 
    digits=int(input("enter a number")) #asked n times
    s=s+digits #sum of numbers is stored
avr=s/n
print("average of numbers is ",avr)


#using while loop
lst=[]
suma=0
num=int(input("enter the number of digits"))
t=0 #this will help in stoping while loop
while t!=num:
    digit=int(input("enter the digit"))
    lst.append(digit)
    suma=suma+digit
    t+=1 #increasement of 1 make t equals to n
average=suma/n
print(f"average of numbers is {average}")
print(f"list of numbers is {lst}")
