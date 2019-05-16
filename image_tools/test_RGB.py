from PIL import Image
import os

# 打印一张照片上所有的 像素值
img = Image.open('a.jpg')
data = img.load()
for x in range(img.size[0]):
	for y in range(img.size[1]):
		color = data[x, y]
		# print(color)
		print(type(color))
