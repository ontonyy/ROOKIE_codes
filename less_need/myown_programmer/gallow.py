from random import choice

def hangman(word):
    wrong = 0
    stages = ['',
              '--------        ',
              '|               ',
              '|       |       ',
              '|       0       ',
              '|      /|\      ',
              '|      / \      ',
              '|               ']
    letters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to the decimation!')
    while wrong < len(stages) - 1:
        msg = input('\nInput letter: ')
        if msg in letters:
            cind = letters.index(msg)
            board[cind] = msg
            letters[cind] = '$'
        else:
            print(f'\n{len(stages) - wrong} attempts left')
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '_' not in board:
            print(f"\nYou won! Hidden word was: {' '.join(board)}")
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print(f"\nYou lost! Hidden word was: {word}")

if __name__ == '__main__':
    hangman(choice(['cat', 'cow', 'computer', 'weird', 'rat', 'same', 'shit', 'key', 'idea', 'scale']))