def get_int():
    return int(input("Prime number: "))

user_int = get_int()

def main():
    for i in range(2, user_int):
        if user_int % i == 0:
            print(f"{user_int} is not prime!")
            break
        else:
            print(f"{user_int} is prime!")
            break

if __name__ == '__main__':
    main()
