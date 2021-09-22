def reversed_string(ans):
    reversed_ans = ans[::-1]
    return " ".join(reversed_ans)

answer = str(input("Some string: ")).split(" ")
if __name__ == '__main__':
    print(reversed_string(answer))