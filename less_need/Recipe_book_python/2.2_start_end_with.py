import os

filenames = os.listdir('.')

print(any(name.endswith('.py') for name in filenames))