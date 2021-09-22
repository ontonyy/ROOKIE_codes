W = int(input("Type number of you weight: "))
D = str(input("This is in (K)G or (L)bs: "))


if D.upper() == "K":
    print("Your weight in LBS is", W * 2.2)

elif D.lower() == "l":
    print("Your weight in KG is ", W / 2.2)

else:
    print("Try again!")
