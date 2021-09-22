# My own image-reader and then image rotation changing
import random
from PIL import Image
import glob

for img in glob.glob('C:/Users/gavra/Desktop/ВСЯКОЕ очень ВАЖНОЕ/Pictures/*.jpg'):
    # Finding a image name
    first = img.split('\\')
    second = first[1].split('.')
    try:
        i = Image.open(img)
        # Random rotation
        i.rotate(random.randint(1, 360)).save(f"special_files/rotates/{second[0]}.png")
    except:
        continue