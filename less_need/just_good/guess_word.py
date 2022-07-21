
class Guessing:

    def __init__(self, secret_word, guess, guess_count, guess_limit, out_of_guesses, countdown):
        self.secret_word = secret_word
        self.guess = guess
        self.guess_count = guess_count
        self.guess_limit = guess_limit
        self.out_of_guesses = out_of_guesses
        self.countdown = countdown

    def secret(self):
        while self.guess != self.secret_word and not self.out_of_guesses:
            print(f'Word have {len(self.secret_word)} signs')
            print(f'You have only {self.countdown} attempts for guess the secret word!\n')
            if self.guess_count < self.guess_limit:
                self.guess = input("Enter your word - ")
                self.guess_count += 1
                self.countdown -= 1
                print('Left only {} attempts\n'.format(self.countdown))
            else:
                self.out_of_guesses = True
        if self.out_of_guesses:
            print('You lose your tries!')
        else:
            print('\nWHAT A CHAMPION, YOU WIN<3')

Guessing('calculator', "", 0, 5, False, 5).secret()
