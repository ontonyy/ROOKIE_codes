import os
import string


def path_changing(a):
    os.mkdir('C:\main_modules\my_modules\Tasks_xD\zproger_task\codes')

    for a in range(1, len(a)):
        os.replace(f'File_{a}', f'codes\File_{a}')

if __name__ == '__main__':
    alphabet = [a for a in string.ascii_letters]
    path_changing(alphabet)
