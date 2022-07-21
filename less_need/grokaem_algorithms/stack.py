def greet(name):
    print("Hello," + name + "!")
    greet2(name)
    print("getting ready to say goodbye!...")
    bye()


def greet2(name):
    print("How are you, " + name + "?")


def bye():
    print("Ok bye!")

if __name__ == '__main__':
    greet("maggie")
