# user input

name = input("Enter your name: ")
age = input("Enter your age: ")
print("My name is: ", name)
print("My age is: ", age)



# sum of 2 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a+b
print("The sum is: ", sum)


# Question: WAP to print the average of 2 numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
average = (num1 + num2) / 2
print("The average is: ", average)


# QS. 
name1 = input("Enter a name: ")
age1 = int(input("Enter a age: "))

print("Hello",name1,"you are",age1,"years old!")

# QS. Take a decimal number as input (like 45.78) and output its: •integer part -45 •fractional part - .78
# Take decimal number as input
num = float(input("Enter a decimal number: "))

# Find integer part
integer_part = int(num)

# Find fractional part
fractional_part = num - integer_part

# Print results
print("Integer part =", integer_part)
print("Fractional part =", fractional_part)