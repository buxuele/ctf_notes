#!/usr/bin/python3
# Time: 2019/07/18 9:38 PM
# About: 

import os
import cv2

dir_path = '/home/fc/Pictures/screenShots/'
ext = '.png'
output = 'little_ideas.mp4'
fps = 0.5     # 这个数越小, 照片切换越慢..

frame_array = []
files = [i for i in os.listdir(dir_path) if i.endswith(ext)]
# print(files)

for j in range(len(files)):
    filename = dir_path + files[j]
    img = cv2.imread(filename)
    h, w, c = img.shape
    frame_array.append(img)

out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (1920, 1080))

for i in range(len(frame_array)):
    out.write(frame_array[i])

out.release()




































