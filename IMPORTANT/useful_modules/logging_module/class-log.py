import logging

# logging.basicConfig(filename=r'C:\ROOKIE_codes\python_projects\IMPORTANT\useful_modules\logging_module\employee.log', format='%(levelname)s:%(message)s', level=logging.INFO)
# or
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(r'C:\ROOKIE_codes\python_projects\IMPORTANT\useful_modules\logging_module\employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
