1. python3 string
"""
import _string
hexdigits = digits + 'abcdef' + 'ABCDEF'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
"""
2. python3 可以造成 MemoryError
x = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
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

5. python, pow():
x = pow(3, 2) = 3**2
x = pow(3, 2, 2) = 3**2 % 2
6. @classmethod,
	可以从类直接调用,不必实例化,也不需要括号:
	A.do_something()

7. @staticmethod
	不需要传入self和cls, 就像普通的函数一样.也是不需要实例化就可以调用的
	A.do_what()

1. python3 input 注入:
echo '__import__("os").system("cat flag.txt") ' | python3 evil.py
3. chrome extensions location:
/home/fc/.config/google-chrome/Default/Extensions/
4. python3 查看当前环境下,所有的可用内建对象
h = ().__class__.__bases__[0].__subclasses__()[0:50]
# print(h)
[c for c in h if c.__name__=='BuiltinImporter'][0].load_module('io').open('flag.txt').read()

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

1. 60 << 2 = 240
左移动位运算  运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，
高位丢弃，低位补0。

2.
