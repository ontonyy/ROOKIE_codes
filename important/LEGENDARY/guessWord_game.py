import random

list = ["mouse", "football", "printer", "space", "goal", "cow"]
word = random.choice(list)
lives = 7
guessed_words = []
game_over = False
guesses = ["_ "] * len(word)

print("GUESSING WORD BY LETTER\nYou have only 7 LIVES")
while not game_over:

    hidden_word = ''.join(guesses)

    print("\nYou guessed letters: {}".format(", ".join(guessed_words)))
    print(f"Hidden word - {hidden_word}")

    ans = input("Guess the letter/word: ").lower()

    if ans in word and ans not in guessed_words:
        print("right!")
        for i in range(len(word)):
            for x in range(len(ans)):
                if word[i] == ans[x]:
                    guesses[i] = ans[x]

    elif ans == 'quit':
        print("Game is over")
        game_over = True

    elif ans in guessed_words:
        print("Already you type this word")

    else:
        lives -= 1
        print(f"Lives - {lives}")

    if ans not in guessed_words:
        guessed_words.append(ans)

    if lives <= 0:
        print("Game is over, you lost all lives")
        game_over = True

    elif word == ''.join(guesses):
        print(f"\nYOU GUESSED! this was word - {word.upper()}")
        game_over = True




