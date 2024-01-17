#Question 2: Library Book Reservation System
#Design a Python program for a Library Book Reservation System.
#Create a function reserve_book(book_title, student_status) that
#allows students to reserve a book. If the book is available and
#the student is a regular student, reserve the book; if the student
#is a VIP student, provide instant reservation. Handle cases
#where the book is not available.
def reserve_book(x,y):
    if book=="available":
        if student_status=="regular":
            print("book will be reserved soon")
        if student_status=="VIP":
            print("book is reserved")
    else:
        print("sorry,book is not present at the moment")
book_title=input("enter the name of the book wanted")
book=input("enter the book is available or not ")
student_status=input("enter whether the student is VIP or regular")
reserve_book(book_title,student_status)


