
def mydecorator(fn):
    def inner_funcrion():
        fn()
        print('How are you?')
    return inner_funcrion

@mydecorator
def greet():
    print('Hello ', end='')

greet()

@mydecorator
def dosomething():
    print('\nHere I can do something')

dosomething()