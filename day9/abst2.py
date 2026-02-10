from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def  sound(self):
        pass
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def sound(self):
        print("Bark")
    # def sound1(self):
    #     print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
class Cow(Animal):
    def sound(self):
        print("Moo")
# obj1=Dog()
# obj1.sound()   #Bark
# obj1.sound1()  #bark

obj2=Cat()
obj2.sleep()

