class Question:
    def __init__(self, answer, prompt):
        self.answer = answer
        self.prompt = prompt


questions_prompts = [
    "What color have Black man?\n(a) Black \n(b) Usual color \n(c) White or snow color\n\n",
    "How many IQ have Silvester Stallone?\n(a) roughly 170IQ \n(b) like as kid, 55IQ \n(c) average IQ - 100\n\n",
    "Who now is the Boss in Russia?\n(a) Vladimir Lenin \n(b) Vladimir Putin \n(c) Dmitrii Hrustalev\n\n"
]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "b"),
]


def main(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct answers!")


main(questions)
