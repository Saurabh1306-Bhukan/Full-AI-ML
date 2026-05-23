# Class : A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# Object : An object is an instance of a class. It is a specific realization of the class, with its own unique set of attributes and methods.   

class Student:
    subject = "Python"
    college = "ABC College"
    year = "4th Year"

a = 10
stu1 = Student()
stu2 = Student()
print(stu1)
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)


