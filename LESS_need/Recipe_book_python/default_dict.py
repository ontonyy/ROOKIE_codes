from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(4)

print(dict(d))