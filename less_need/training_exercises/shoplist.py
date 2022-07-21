shoplist = ['mango', 'chocolate', 'banans', 'water', 'candies']
print("Here is how seeing my shoplist ", shoplist, '. And I should buy whole ', len(shoplist), 'items!')

print('Мy purchases: ', end = ', ')
for item in shoplist:
    print(item, end=', ')

print('\nI want to buy some milk')
shoplist.append('milk')
print('Now my purchases like this: ', shoplist)

print('I am going to sort my buying: ')
shoplist.sort()
print('Now it look like: ', shoplist)

print('First what I should buy is: ', shoplist[2])
olditem = shoplist[2]
del shoplist[2]
print('I bought -', olditem)
print('Now remained only: ', shoplist)

