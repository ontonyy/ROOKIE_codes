class Robot:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('\nInitialization - {}'.format(self.name))
        '''При создание робота, сразу добавляется к числу роботов'''

        Robot.population += 1

    def __del__(self):
        '''Смерть робота'''
        print('\n{} destroyed...'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was last droid'.format(self.name))
        else:
            print('Remain {0:d} robots'.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота'''
        print('Hello my owner, my num1 is {} and I am only {} years old'.format(self.name, self.age))

    def HowMany():
        '''Численность роботов'''
        print('Now space station have a {0:d} robots'.format(Robot.population))
    HowMany = staticmethod(HowMany)

droid1 = Robot('MK-12', 3)
droid1.sayHi()
Robot.HowMany()

droid2 = Robot('Tony-300', 12)
droid2.sayHi()
Robot.HowMany()

droid3 = Robot('Mask-CUM', 5)
droid3.sayHi()
Robot.HowMany()

print('\n In here robot doing some work, and after relax\n')
print('Enough we don\'t need this robots, and can destroy them.' )

del droid2, droid1, droid3

print('This was great work from robots, but now is new era for new droids already.')


