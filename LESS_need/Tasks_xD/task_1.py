class User:
    def __init__(self):
        self.name = str(input("Your name: "))
        self.age = int(input("Your age: "))
        self.year = int(input("What year is today?: "))
        self.quantity = 0

    def main(self):
        self.quantity = (self.year - self.age) + 100
        print("Your name {} and your age is {}, when you will be 100 years old, year shall be {} OMG!".format(self.name,
                                                                                                              self.age,
                                                                                                              self.quantity))


end = User()

end.main()
