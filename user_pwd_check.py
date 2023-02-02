pwd = input("Enter your password: ")

if(pwd.isalnum()):
    print("Your password is okay i.e. "+str(pwd))
else:
    print("Sorry we don't allow other than alphabet and number")