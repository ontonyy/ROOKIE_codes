import random
import string


def password(ans):
    password_list1 = []
    password_list2 = []

    alphabet = list(string.ascii_letters)    # import ABC lower/upper from module string

    while len(password_list1) < ans:
        random_abc = random.choice(alphabet)
        random_int = random.randint(1, 9)   # Random numbers between 1 - 9, with module random

        password_list1.append(random_abc)
        password_list1.append(str(random_int))

    while len(password_list2) < ans:    # Choosing random sign from password_list1
        random_choice = random.choice(password_list1)
        password_list2.append(random_choice)

    print("\nYour safely password - ", "".join(password_list2))


answer = int(input("How long would be your password?(num): "))
if __name__ == '__main__':
    password(answer)
