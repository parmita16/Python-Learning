class GrandParent:
    def house(self):
        print("House")

class Parent(GrandParent):
    def car(self):
        print("Car")

class Child(Parent):
    def bike(self):
        print("Bike")

c = Child()

c.house()
c.car()
c.bike()