# Polumorphism: The ability of an object to take many forms

# Function overriding: When a child class provides a specific implementation of a method that is already defined in its parent class.

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()


# Duck typing: An object’s suitability is determined by the presence of certain methods and properties, rather than the actual type of the object.



class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

acc1 = Accountant()
acc1.get_designation()