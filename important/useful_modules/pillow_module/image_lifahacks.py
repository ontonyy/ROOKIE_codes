from PIL import Image, ImageFilter
import os

image = Image.open('dogs_images_png/dog1.png')

# Image rotation
image.rotate(90).save(f'with_mod/1dog1.png')

# Image Black and White style
image.convert(mode='L').save(f'with_mod/2dog1.png')

# Image Blur
image.filter(ImageFilter.GaussianBlur(10)).save(f'with_mod/3dog1.png')
