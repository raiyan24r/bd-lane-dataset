import json
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import shutil
directory = r'H:\Thesis 400\1.Dataset_Creation\Final\visual-revised'
og = r'H:\Thesis 400\1.Dataset_Creation\lane_frames'
dest = r'H:\Thesis 400\1.Dataset_Creation\Final\final-dataset-sanitized'

for filename in os.scandir(directory):
    if filename.is_file():
        print(str(filename.name).split('_main')[0])
        img_name = str(filename.name).split('_main')[0]
        shutil.copy2(og+'\\'+img_name, dest)

        # break
