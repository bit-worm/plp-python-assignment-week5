# encapsulation
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Manager(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__position = "manager"

    def getPosition(self):
        return self.__position

class SalesRep(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__position = "sales rep"

    def getPosition(self):
        return self.__position


employee1 = Manager("Bob", "21st BV")
employee2 = SalesRep("Joy", "Va 232")

print(f"Name: {employee1.name}")
print(f"Address: {employee1.address}")
print(f"Possition: {employee1.getPosition()}")
print("\n")
print(f"Name: {employee2.name}")
print(f"Address: {employee2.address}")
print(f"Possition: {employee2.getPosition()}")
