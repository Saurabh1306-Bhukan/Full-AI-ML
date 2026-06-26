# try, except, else, finally

try:
    x = int(input("Enter a number:"))
    ans = 10 / x

except ZeroDivisionError:
    print("Divide by zero is not allowed")

except ValueError:
    print("Invalid Input")

else:
    print(f"Answer is = {ans}")

finally:
    print("This is a end of program")