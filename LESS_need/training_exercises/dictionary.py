ab = {'ontonyy': 'gavranton.ee@gmail.com',
      'monkiez': 'monkiebrotherhood@mail.ru',
      'footballer': 'footbalLOVE@ok.ru',
      'philosof': 'philosofia@viber.com'
      }
print("Ontony's address is:", ab['ontonyy'])

del ab['footballer']

print('Now in address string only {} contacts\n'.format(len(ab)))

for name, address in ab.items():
    print("Contact {} have a this e-mail - {}\n".format(name, address))

ab['Dmitrik'] = 'dmitronnik@via.vk'

if 'Dmitrik' in ab:
    print('Dmitrik address - ', ab['Dmitrik'])
