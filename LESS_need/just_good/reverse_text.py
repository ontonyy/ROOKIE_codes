def reverse(text):
    return text[::-1]


def comparing(text):
    return text == reverse(text)


something = str(input("palindrome: "))
som = ''.join(something.split())

if comparing(som.lower()):
    print("Yes it is palindrome!")
else:
    print("No it is not palindrome" + " --> {}".format(som[::-1]))
