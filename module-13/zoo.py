from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        self.__name='monkey'
    @abstractmethod
    def eat(self):
        pass
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print("I can move slowly")

class Monkey(Animal):
    def sing(self):
        print('I ma singing')
    def eat(self):
        print("i don't eat grass")
    def move(self):
        super().move()
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

layka = Monkey()

print(layka)
layka.eat()
layka.move()
layka.name="khanki"
print(layka.name)