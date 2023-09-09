# Object Oriented Programming (OOP)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        print(name, age)


    def get_name(self):
        return self.name

    def hello(self):
        return "Haw!"
    
    def bark(self):
        print("Bark")


d1 = Dog("Laui", 17)
d2 = Dog("Muer", 18)




