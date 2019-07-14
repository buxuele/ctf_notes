import os 
import time 

"""
去除文件名称的空格这部分还需要再改进一下.
需要定义一个函数来处理. 


    option 1 (no-key is needed):
        cat *.ts > all.ts   
        ffmpeg -i all.ts -acodec copy -vcodec copy  a.mp4
    
    option 2(need key):
        1. change *.m3u8: 
            #EXT-X-KEY:METHOD=AES-128,URI=key.key !!! no-quote-marks
        2. run : 
            # ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy j2.mp4
    
    option 3(not sure about this):
        ffmpeg -i index.m3u8 -c copy rename_me.mp4
 
"""


def _rename():
	A = os.listdir()
	for i in A:
		filename, suffix = os.path.splitext(i)
		# print(filename, suffix)
		if suffix == ".ts":
			new_filename = ''.join(filename.split(' ')[:2]) + '.ts'
			os.rename(i, new_filename)
			print(new_filename)


def convert():
	B = os.listdir()
	for i in B:
		filename, suffix = os.path.splitext(i)
		if suffix == ".ts":
			# 下面是开始进行格式转换
			output_name = filename + ".mp4"
			os.system(f"ffmpeg -i {i} -acodec copy -vcodec copy {output_name}")
			time.sleep(2)
			print(filename + " --- is Done!")

# 基本语法是
# ffmpeg -i some.ts -acodec copy -vcodec copy new.mp4

if __name__ == "__main__":
	_rename()
	time.sleep(2)

	convert()
	time.sleep(2)

	# os.system("rm *.ts")



