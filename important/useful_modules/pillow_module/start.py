import os
from PIL import Image

size_300 = (300, 300)
size_700 = (700, 700)

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.jfif') or f.endswith('.jpeg') or f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save(f'700_dogs/700_{fn}.png')

        i.thumbnail(size_300)
        i.save(f'300_dogs/300_{fn}.png')
