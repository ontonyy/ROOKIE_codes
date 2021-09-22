from operator import itemgetter

rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]

rows_fname = sorted(rows, key=itemgetter('fname'))
rows_uid = sorted(rows, key=itemgetter('uid'))

rows_fname2 = sorted(rows, key=lambda k: k['fname'])
rows_uid2 = sorted(rows, key=lambda k: k['uid'])

print(rows_fname, '\n')
print(rows_uid, '\n')

print(rows_fname2, '\n')
print(rows_uid2, '\n')
