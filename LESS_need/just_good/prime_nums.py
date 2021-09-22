# Prime numbers
sieve = [True] * 101
for x in range(2, 100):
    for j in range(x*x, 100, x):
        sieve[j] = False
    if sieve[x]:
        print(x)