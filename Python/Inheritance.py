# Inheritance: Reusing attr & meyhods from a parent (Base) class.

#  A child class can inherit attributes and methods from a parent class.
#  This promotes code reusability and allows for the creation of more specific classes based on a general class.

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self,new_end_time):
        self.end_time = new_end_time


class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


staff1 = AdminStaff("Manager")

print(staff1.role, staff1.start_time, staff1.end_time)

# Types of Inheritance:
# 1. Single Inheritance: A child class inherits from a single parent class.
# 2. Multiple Inheritance: A child class inherits from multiple parent classes.
# 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.   


class Teachers:
    def __init__(self, salary):
        self.salary = salary
    
class Student:
    def __init__(self, gpa):
        self.gpa = gpa
    
class TA(Teachers, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(15_000, 9.4, "Saurabh")
print(ta1.name, ta1.salary, ta1.gpa)


