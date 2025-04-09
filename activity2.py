# polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Meow"

animal1 = Dog("Rocket")
animal2 = Cat("Chloe")

print(f"{animal1.name} says {animal1.speak()}")
print("\n")
print(f"{animal2.name} says {animal2.speak()}")
