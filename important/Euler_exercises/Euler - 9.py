# Euler 9 my SOLUTION

from math import sqrt

d = 1000
# 1000 = a + b + c
# c*c = a*a + b*b

for a in range(1, 1000):
    for b in range(1, 1000):
        c = sqrt(a * a + b * b)
        if (float(a) + float(b) + c == float(d)):
            print(a, '+', b, '+', c)
            print('These numbers multiplying - ', a*b*c)


