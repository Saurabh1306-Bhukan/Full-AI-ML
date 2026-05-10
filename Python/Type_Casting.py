# Type Conversion
# Implicit Type Conversion
x = 5
y = 3.14
result = x + y            # x is implicitly converted to float
print("Result of implicit type conversion:",type(result),"=", result)


# Type Casting (Explicit Type Conversion)
a = 10
b = 3.14
result1 = a + b  
# print(type(int(result1))) 

a = int(result1)
print(a)
print(type(a)) 


val = int("123")  # String to Integer
print(val, type(val))

val1 = bool(0) # Zero is considered False
print(val1, type(val1))

val2 = bool(10)  # Non-zero values are considered True
print(val2, type(val2))