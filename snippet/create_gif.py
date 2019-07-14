import sys
import glob 
import imageio

"""
barely worked!!!
"""

DURATION = 1.5
OUT_GIF = 'out.gif'
VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration=DURATION):
	images = []
	for f in filenames:
		images.append(imageio.imread(f))
	# mim-save, for many images
	imageio.mimsave(OUT_GIF, images, duration=duration)


if __name__ == "__main__":
	# script = sys.argv.pop(0)
	# args = sys.argv
	#
	# if len(args) == 0:
	# 	print("111")
	# 	sys.exit(1)
	#
	# elif len(args) == 1:
	# 	print("2222")
	# 	filenames = glob.glob(args[0])
	#
	# else:
	# 	filenames = args
	#
	# if not all(f.lower().endwith(VALID_EXTENSIONS) for f in filenames):
	# 	print("use png or jpg")
	# 	sys.exit(1)

	filenames = glob.glob('*.png')
	print(filenames)
	create_gif(filenames)


















