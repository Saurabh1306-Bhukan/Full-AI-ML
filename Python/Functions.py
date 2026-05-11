# Functions :- 
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def hello():
    print("Hello, World!")

hello()  # calling the function


# =-----------------------------------------------

def sum(a, b):
    s = a + b
    return s

ans = sum(5, 10)  # calling the function with arguments
print("The sum is:", ans)

# --------------------------------------------------

# QS. calculate average of three numbers using function.

def cal_avg(a, b, c):
    avg = (a+b+c)/3
    return avg

print(cal_avg(10,20, 30))


# ====================================================

# default value

def add(a, b=1):
    return a + b

print(add(5))  # b will take default value 1
print(add(5, 10))  # b will take value 10


# ----------------------------------------------------

# Types of functions :- 
# 1. Built-in functions
# 2. User-defined functions
# 3. Anonymous functions (lambda functions)


# lambda function :-
# A lambda function is a small anonymous function that can take any number of arguments, but can

# lambda functions can only have one expression. They are often used for short, simple functions that are not worth defining with a full function definition.

sum = lambda c,d: (c + d)
print(sum(5, 10))

# uses:- 
# 1. They are used when we need a small function for a short period of time.
# 2. They are used in higher-order functions like map(), filter(), and reduce() to create small, throwaway functions that are not worth defining with a full function definition.


# QS. WAF to print factorial of 'n'.

def cal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

n = int(input("Enter a number: "))

print(cal_factorial(n))
