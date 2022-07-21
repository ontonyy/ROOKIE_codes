zoo = ('cow', 'shark', 'tiger', 'lion', 'snakes')

print('Now zoo have a', len(zoo), 'animals')

new_zoo = 'crocodile', 'monkeys'
newest_zoo = new_zoo + zoo

print('New zoo, and all animals in there', newest_zoo)
print('Oldest animals from old zoo', newest_zoo[2:7])
print('The last bringing animal was', newest_zoo[6])
y = list(newest_zoo)
y.remove('lion')
y.sort()
newest_zoo = tuple(y)
print(newest_zoo)

print('The quantity of all animals in new zoo', len(newest_zoo))

