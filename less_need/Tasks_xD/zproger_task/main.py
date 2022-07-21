import os
import string
import time

alphabet = [a for a in string.ascii_letters]


def make_files(a):

    for x, a in zip(range(1, len(a)), a):
        with open(f'File_{x}', 'w') as file:
            file.write(f"Character - {a}\n")


if __name__ == '__main__':
    alphabet = [a for a in string.ascii_letters]
    make_files(alphabet)
