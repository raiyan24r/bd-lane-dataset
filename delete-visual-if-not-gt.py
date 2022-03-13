import os
import shutil
from os.path import exists

gt = r'H:\Thesis 400\1.Dataset_Creation\Final\gt\\'
visual = r'H:\Thesis 400\1.Dataset_Creation\Final\visual'
for filename in os.scandir(visual):
    if filename.is_file():
        # print(filename.name)
        img_name = str(filename.name).split('_main')[0]
        print(img_name)
        # break
        if not os.path.exists(gt+img_name+'_gt.png'):
            print(filename.path)
            os.remove(filename.path)
