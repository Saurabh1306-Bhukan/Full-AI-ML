# Class & Instance :

class Student:
    college_name = "ABC College"  # class attribute

    def __init__(self, name, gpa):
        self.name = name # instance attribute
        self.gpa = gpa

stu1 = Student("Om", 8.3)

print(stu1.name)
print(Student.college_name)
print(stu1.college_name)  # we can access class attribute using instance as well