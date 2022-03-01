# Author: Tracy Vierra
# Date Created: 3/1/2022
# Date Modified: 3/1/2022

# Description:

# Usage:

class Student:              # base class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display(self):
        print(self.name)
        print(self.age)

class ScienceStudent(Student):  # derived class
    def science(self):
        print("this is a science method")


    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.major = "Physics"

    # def get_data(self):
    #     self.name = input("Enter name: ")
    #     self.age = input("Enter age: ")

    # def display(self):
    #     print(self.name)
    #     print(self.age)
    #     print(self.major)


# student1 = Student("", "")
# student1.get_data()
# student1.display()

a = ScienceStudent("", "")
a.science()
a.get_data()
a.display()


