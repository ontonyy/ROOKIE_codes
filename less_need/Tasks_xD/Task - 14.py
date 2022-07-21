def user_list(ans):
    sett = set(ans)
    list_new = []
    for x in sett:
        list_new.append(x)

    return sorted(list_new)


answer = str(input("Type some numbers(comma separated): ")).split(", ")

if __name__ == '__main__':
    print(user_list(answer))
