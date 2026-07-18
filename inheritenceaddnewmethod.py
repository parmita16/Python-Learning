class Animal:
    def eat(self):
        print("Eating food")

class Dog(Animal):
    def bark(self):
        print("Woof Woof!")

dog = Dog()

dog.eat()
dog.bark()