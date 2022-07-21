def palindrome(pal, pal_rev):
    if pal == pal_rev:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")

pal = str(input("Type some palindrome: "))
pal_rev = pal[::-1]
palindrome(pal, pal_rev)
