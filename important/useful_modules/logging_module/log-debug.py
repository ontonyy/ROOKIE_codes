import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

file_handler = logging.FileHandler(r'C:\ROOKIE_codes\python_projects\IMPORTANT\useful_modules\logging_module\catch.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def multiple(a, b):
    return a * b

def division(c, d):
    try:
        result = c / d
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result

num1 = 5
num2 = 0

multiple_result = multiple(num1, num2)
logger.debug('Multiple: {} * {} = {}'.format(num1, num2, multiple_result))

division_result = division(num1, num2)
logger.debug('Division: {} / {} = {}'.format(num1, num2, division_result))


