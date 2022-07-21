# HASH or HASH function or HASH tables
# Chapter 5 in "Грокаем алгоритмы"
import string


def first_func(input):
    dict_1 = dict()
    dict_1[input] = 1
    print(dict_1)
    return f"Always return - {dict_1[input]}\n"


def second_func(input):
    dict_2 = dict()
    dict_2[input] = int(len(input))
    print(dict_2)
    return f"String length - {dict_2[input]}\n"


def third_func(input):
    dict_3 = {}
    dict_3[input] = input[0]
    print(dict_3)
    return f"First character - {dict_3[input]}\n"


def four_func(input):
    prime_nums = []
    alphabet = list(string.ascii_lowercase)
    dict_4 = {}

    for num in range(1, 1000):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            prime_nums.append(num)
        if len(prime_nums) == len(alphabet):
            break

    for num, char in zip(prime_nums, alphabet):
        dict_4[char] = num

    user_inp = list(input)
    summa = 0

    for u in user_inp:
        summa += dict_4[u]

    print(dict_4)
    return f"Summa of '{input}' characters - {summa}"

def main(inp):
    print(first_func(inp))
    print(second_func(inp))
    print(third_func(inp))
    print(four_func(inp))


if __name__ == '__main__':
    inp = input("Input something: ")
    main(inp)
