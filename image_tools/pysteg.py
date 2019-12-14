from PIL import Image

# 注意: 修改一下文件名
img = Image.open('a.jpg')
data = img.load()
# print(img.size)

def get_plane(img, channel, index=0):
	if channel in img.mode:			# mode ???
		new_image = Image.new('1', img.size)
		new_image_data = new_image.load()

		img_data = img.load()
		channel_index = img.mode.index(channel)

		for x in range(img.size[0]):
			for y in range(img.size[1]):
				color = img_data[x, y]
				# color[1] , color[channel]  0, 1, 2   R G B
				channel = color[channel_index]
				plane = bin(channel)[2:].zfill(8)
				# print(plane)
				try:
					new_image_data[x, y] = 255*int(plane[abs(index-7)])
				except IndexError:
					pass

		return new_image

		# print(color)

# new_image = get_plane(img, 'R', 0)
# new_image.show()

for channel in img.mode:
	for plane in range(8):
		x = get_plane(img, channel, plane)
		# x.show()
		x.save(f'{channel}-{plane}.png')
