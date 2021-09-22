import random


def guessing(guess_num):
    while True:
        ans = int(input("Guess the number: "))
        if ans < guess_num:
            print("More...")
        elif ans > guess_num:
            print("Less...")
        else:
            print(f"\nGUESSED!!!\nIT is number {guess_num}")
            break


guess_num = random.randint(1, 100)
if __name__ == '__main__':
    guessing(guess_num)





