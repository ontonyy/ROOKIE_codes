class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and my age is {self.age}")

    def speak(self):
        print("I don't know what to say!")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and my age is {self.age}, and my skin have a {self.color} color")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Burka", 5)
p.show()
c = Cat("Musk'ka", 9, "White")
c.show()
d = Dog("Koer", 14)
d.show()
