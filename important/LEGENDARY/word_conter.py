class myFunc:
    def __init__(self, user_list):
        self.user_list = user_list

    def word_counter(self):
        counter = list(self.user_list.split(" "))
        print("|----->", len(counter), "<-----|")


intro = myFunc(input("Some text or string, or phrase: "))
intro.word_counter()

while True:
    response = str(input("You wanna continue?(y/n): "))
    if response == "Y" or response == "y":
        intro = myFunc(input("Some text or string, or phrase: "))
        intro.word_counter()
    elif response != "Y" or response != "y":
        break
