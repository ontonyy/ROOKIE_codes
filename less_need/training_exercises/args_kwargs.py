# Args принимает значения и сет выводит построчно
def myFunc(*first):
    for arg in first:
        print(arg)


myFunc('Hello', 'My', 'Young', 'Lord')

print("\n^_^Next example^_^\n")


# arg обычный аргумент, а * и есть args в форме сета
def next_myFunc(arg, *first):
    print("First argument in my set: ", arg)
    for x in first:
        print("Next items in my set: ", x)


next_myFunc("Seignior", "your", "num1", "is", "Margetti")

print("\n^_^Next example - KWARGS^_^\n")


# kwargs как словарь, пишется через равно, и items главное
def newFunc(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


newFunc(name="Jave", age=23, nationality="Russian", job="waiter")

print("\n^_^Next example - KWARGS^_^\n")


def lastFunc(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


first = ("Tony", "is", "Tony")
second = {"arg1": "Smoking", "arg2": "health can", "arg3": "pull up"}
lastFunc(*first)
lastFunc(**second)

print("\n^_^Next example - KWARGS^_^\n")


def lastestFunc(*first, **kwargs):
    print("first: ", first)
    print("kwargs: ", kwargs)


first = "Debug", "Mod", "Mister"
lastestFunc(first, name="Konan", ass="fatASS", hair="grey a little bit")
