import time
from threading import *


def one(second):
    print(f'Sleeping time {second} seconds(s)')
    time.sleep(1)
    print('\nSleeping is done')


threads = []
for _ in range(10):
    t = Thread(target=one, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
