class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name1(self):
        print('Name of commits is {} and his num2 is {}'.format(self.name, self.age))

    def name2(self):
        print('Name of second commits is {} and her num2 is {}'.format(self.name, self.age))


c1 = Person('Mikhail', 32)
c2 = Person('Anna', 17)
c2.name2()

c1.name1()
