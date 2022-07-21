import os

from PIL import Image
import math

png_dir = r'H:\Thesis 400\1.Dataset_Creation\images\for gif'
images = []
for file_name in sorted(os.listdir(png_dir)):
    foo = Image.open(os.path.join(png_dir, file_name))
    x, y = foo.size
    foo = foo.resize((math.floor(x/5), math.floor(y/5)), Image.ANTIALIAS)
    foo.save(r"H:\Thesis 400\1.Dataset_Creation\images\gif-optimized\\" +
             file_name, optimize=True, quality=60)
