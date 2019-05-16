1. python3 string
"""
import _string
hexdigits = digits + 'abcdef' + 'ABCDEF'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
"""

12. python3 字符串中 可能不怎么常用的方法:
	1. # print(text.capitalize())       # 只是一个字母
	2. # print(text.center(40, "*"))　  # 写注释很有用
	3. # 制作一个转换映射表
		# intab = "aeiou"
		# outtab = "12345"
		# text = "this is a string example...wow...oops"
		# transtab = text.maketrans(intab, outtab)
		# print(text.translate(transtab))
	4. # print(text.swapcase())      # 将字符串中 大小写互换

2. zip(), map(), iter()都是内建的函数, 需要再看看

5. python, pow():subl
x = pow(3, 2) = 3**2
x = pow(3, 2, 2) = 3**2 % 2

6. @classmethod,
	可以从类直接调用,不必实例化,也不需要括号:
	A.do_something()

7. @staticmethod
	不需要传入self和cls, 就像普通的函数一样.也是不需要实例化就可以调用的
	A.do_what()


ord() 返回对应的 ASCII 数值，或者 Unicode 数值
chr() 用一个整数作参数，返回一个对应的字符。
int('0101011010110', 2)	binary---int
int('776f726c64', 16)	hex---int
format(14, 'b') ------> '1110' 去除 0b
bytes(string, 'utf-8') ------>bytes_string


11. # 逐行读取一个文件。节省内存。
with open("./notes.py", 'r') as f:
	for line in f.readlines():
		print(line)
