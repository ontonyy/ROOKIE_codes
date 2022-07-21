import random


def game(p1, p2, a, b, c):
    if p1 == a and p2 == c:
        print(f"YOU WIN!\n{p1.capitalize()} punch the {p2}!")
    elif p1 == a and p2 == b:
        print(f"Computer win!\n{p2.capitalize()} cover the {p1}!")
    elif p1 == b and p2 == a:
        print(f"YOU WIN!\n{p1.capitalize()} cover the {p2}")
    elif p1 == b and p2 == c:
        print(f"Computer win!\n{p2.capitalize()} cut the {p1}!")
    elif p1 == c and p2 == b:
        print(f"YOU WIN!\n{p1.capitalize()} cut the {p2}")
    elif p1 == c and p2 == a:
        print(f"Computer win!\n{p2.capitalize()} punch the {p1}!")
    elif p1 == a and p2 == a:
        print(f"IT IS A TIE!\n{p2.capitalize()} and {p1}!")
    elif p1 == b and p2 == b:
        print(f"IT IS A TIE!\n{p2.capitalize()} and {p1}!")
    elif p1 == c and p2 == c:
        print(f"IT IS A TIE!\n{p2.capitalize()} and {p1}!")


player1 = input("rock, paper or scissors: ")
computer_choice = ["rock", "paper", "scissors"]
player2 = random.choice(computer_choice)
rock = "rock"
paper = "paper"
scissors = "scissors"
if __name__ == '__main__':
    game(player1, player2, rock, paper, scissors)
