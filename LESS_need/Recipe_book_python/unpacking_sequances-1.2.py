# Обычная распаковка
def middle(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


if __name__ == '__main__':
    print(middle([25, 65, 20, 75, 90, 45]))

record = [15, '55661123', '55515985', 'mail@ru']
grade, *numbers, mail = record
print(numbers)

# Расширенная распаковка

record = [('foo', 5, 1), ('bar', 'hello'), ('foo', 9, 8)]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(x):
    print('bar', x)


for tag, *args in record:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)


# Суммирование списка
def summ(items):
    head, *tail = items
    return head + sum(tail) if tail else head


if __name__ == '__main__':
    print(summ([12, 15, 10, 9]))