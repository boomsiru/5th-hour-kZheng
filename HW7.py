#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello Za Waurdulo!")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = False
admin = False
login  = False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
NumbOfLogin = 2
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if wifi == True:
    if login == True:
        if admin == True:
            NumbOfLogin += 1
            print("Welcome Monkey")

else:
    if wifi == False:
        print("You are missing wifi")
        exit()
    if admin == False:
        print("You are missing admin")
        exit()
    if login == False:
        print("You are missing login")

print(NumbOfLogin)



