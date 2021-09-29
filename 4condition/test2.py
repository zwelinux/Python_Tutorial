# user authentication program

print("Welcome from facebook")

name = "Zwe Linn Htet"
passcode = "chocolatelover1234"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == name and password == passcode:
    print("Welcome ", username)
elif username == name and password != passcode:
    print("Password incorrect")
elif username != name and password == passcode:
    print("Username incorrect")
else:
    print("Something went wrong try again")