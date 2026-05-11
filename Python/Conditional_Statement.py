# Conditional Statements :
# if, elif, else

# if statement is used to execute a block of code if a specified condition is true.

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote.")
    print("You can drive.")

else:
    print("You cannot vote.")
    print("You cannot drive.")

# ----------------------------------------------------

color = input("Enter a color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")


# ------------------------------------------------------

agee = int(input("Enter a age: "))

if agee < 13:
    print("Child")
elif agee >= 13 and agee < 18:
    print("Teeneger")
else:
    print("adult")

# ---------------------------------------------------

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful")
elif username != "admin":
    print("Invalid username")
else:
    print("Invalid password")


# Nesting in if statement

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    if username != "admin":
        print("Invalid username")
    else:
        print("Invalid password")


# Match case statement

color1 = input("Enter a color: ")

match color1:
    case"green":
        print("Go")
    case"yellow":
        print("Get ready")
    case"red":
        print("Stop")

    case _:
        print("Invalid color")
        