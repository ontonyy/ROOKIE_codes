def bottles_of_beer(bob):
    if bob < 1:
        print("No one bottle of beer on wall. No beer bottles")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on wall. {} beer bottles. 
          Take one, let it on in circle, {} beer bottles on wall!\n""".format(tmp, tmp, bob))
    bottles_of_beer(bob)


if __name__ == '__main__':
    bottles_of_beer(99)