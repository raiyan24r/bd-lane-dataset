import os
import imageio


png_dir = r'H:\Thesis 400\1.Dataset_Creation\images\gif-optimized'
images = []
for file_name in sorted(os.listdir(png_dir)):
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.imread(file_path))
imageio.mimsave(r'H:\Thesis 400\1.Dataset_Creation\images\data.gif', images)
print("done")
