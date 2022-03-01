# Author: Tracy Vierra
# Date Created: 3/1/2022
# Date Modified: 3/1/2022

# Description:

# Usage:


# function example:
# def abc():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     print(name)
#     print(age)

# abc()  

# oop example:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display(self):
        print(self.name)
        print(self.age)

student1 = Student("", "")
student1.get_data()
student1.display()
