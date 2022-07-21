class Control:

    def __init__(self):
        self.num1 = int(input("First number: "))
        self.num2 = int(input("Second number:"))

    def main(self):
        if self.num1 % 2 == 0 and self.num2 % 2 != 0:
            print("\nOnly your first num({}) is even, and the second({}) is odd!".format(self.num1, self.num2))
        elif self.num1 % self.num2 == 0:
            print("\nIncredible your divided first num and second num, gives answer 1!")
        elif self.num2 % 2 == 0 and self.num1 % 2 != 0:
            print("\nFirst num({}) is odd, but the second({}) is even!".format(self.num1, self.num2))
        elif self.num1 % 2 == 0 and self.num2 % 2 == 0:
            print("\nYour first num({}) and second num({}) together is even!".format(self.num1, self.num2))
        else:
            print("\nYour first num({}) and second num({}) is odd!".format(self.num1, self.num2))


part = Control()
part.main()
