# Object Oriented Programming (OOP)

# Inheritance


#General Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet): 
    def speak(self):
        print("meow")

class Dog(Pet):
    def speak(self):
        print("Haw!")

Cat1 = Cat("C", 1)
Cat1.show()
Dog1 = Dog("A" , 2)
Dog1.show()