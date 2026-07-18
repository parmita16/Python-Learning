class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog Constructor")

dog = Dog("Tommy")
print(dog.name)