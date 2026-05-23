# Constructor: A constructor is a special method in a class that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the object.
# In Python, the constructor method is defined using the `__init__` method.

class Student:
    def __init__ (self, name):   
        self.name = name 

stu1 = Student("Alice")  # when we create an object of the class, the constructor method is automatically called
stu2 = Student("Bob")  
stu3 = Student("Charlie") 

print(stu1.name)  # prints "Alice"
print(stu2.name)  # prints "Bob"
print(stu3.name)  # prints "Charlie"


# Types of constructors:
# 1. Default constructor: A constructor that takes no parameters and initializes the attributes with default
# 2. Parameterized constructor: A constructor that takes parameters and initializes the attributes with the values passed as arguments

class Student1:
    def __init__ (self, name):  # parameterized constructor  
        self.name = name 

    def __init__(self):  # default constructor
        print("This is a default constructor")
        