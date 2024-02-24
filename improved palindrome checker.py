def palindrome_checker():
    name=input("enter a word:")
    if name[::-1].lower().replace(" ","")==name.lower().replace(" ",""):
        print("yes it is a palindrome")
    else:
        print("it is not a palindrome")
palindrome_checker()
    