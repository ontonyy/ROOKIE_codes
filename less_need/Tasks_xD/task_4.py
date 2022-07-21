user_input = int(input("Type a number and see the divisors: "))
divisor = list(range(1, 1000))
answer = []


def main():
    for i in divisor:
        if user_input % i == 0:
            answer.append(i)
    for x in answer:
        print(x, end=", ")


print('''Divisors is |
           //
          //
         //
        //
       //
      //
_____//''')

main()
