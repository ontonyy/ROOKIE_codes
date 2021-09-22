items = [5, 9, 4, 3, 4, 9, 1, 5, 9]
some = []
for x in items:
    if x not in some:
        some.append(x)

print(some)


def func(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    print(list(func([5, 9, 4, 3, 4, 9, 1, 5, 9])))

