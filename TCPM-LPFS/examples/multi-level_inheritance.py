# Author: Tracy Vierra
# Date Created: 3/1/2022
# Date Modified: 3/1/2022

# Description: multi-level inheritance example

# Usage:


class A:
    def a_method(self):
        print("A method")

class B(A):
    def b_method(self):
        print("B method")

class C(B):
    def c_method(self):
        print("C method")


c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()

print(" ")

b_object = B()
b_object.a_method()
b_object.b_method()

print(" ")

a_object = A()
a_object.a_method()

print(" ")

