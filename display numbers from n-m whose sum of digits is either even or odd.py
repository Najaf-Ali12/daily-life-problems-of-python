#Python program to display all integers within the
#range n-m whose sum of digits is an even number
def even_sum():
    for num in range(start,stop):
  # Extract individual digits
        digit_sum = 0
        for digit in str(num):# made str because for loop doesnot work in int
             digit_sum += int(digit)
# Check if sum of digits is even
        if digit_sum % 2 == 0:
             print(num)


    
#Python program to display all integers within the
#range n-m whose sum of digits is an odd number
def odd_sum():
     for num in range(start,stop):
  # Extract individual digits
        digit_sum = 0
        for digit in str(num):# made str because for loop doesnot work in int
             digit_sum += int(digit)
# Check if sum of digits is even
        if digit_sum % 2 != 0:
             print(num)
start=int(input("enter the starting point of your range"))
stop=int(input("enter the end point of your range"))
print(" now tell that which numbers form",start,"to",stop,"you want")
print("1:whose sum of digits is even number")
print("2:whose sum of digits is odd number")
choice=input("enter 1 or 2:")
if choice=="1":
    even_sum()
elif choice=="2":
    odd_sum()
else:
    print("invalid choice")

