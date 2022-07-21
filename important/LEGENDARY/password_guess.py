import random
import string
import pyautogui
import time

start = time.time()

def send(password, guess_password="", att=0):
    chars = string.ascii_letters + string.digits
    chars_list = list(chars)

    

    while guess_password != str(password):
        att += 1
        guess_password = random.choices(chars_list, k=len(str(password)))
        print(list(guess_password))

        if guess_password == list(str(password)):
            print("Your password is: " + "".join(guess_password) + f", after {att} attempts")
            break

if __name__ == '__main__':
    send(pyautogui.password("Enter your password: "))


# target_password = pyautogui.password("Enter your password: ")
# password_length = len(target_password)
#
#
# characters = string.ascii_letters + string.digits
#
# status = "ongoing"
#
#
# def crack():
#     global target_password, status, password_length
#     count = 0
#
#     while status == "ongoing":
#         guess = ""
#
#         while len(guess) < password_length:
#
#             guess += random.choice(characters)
#
#         if guess == target_password:
#             print("Password cracked!: " + str(guess))
#             status = "finished"
#             count += 1
#             print(str(count) + " guesses")
#         else:
#             count += 1
#
# if __name__ == '__main__':
#     crack()

end = time.time()
print(f"Time taken - {end - start}")

