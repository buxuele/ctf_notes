1. python3 string
"""
import _string
hexdigits = digits + 'abcdef' + 'ABCDEF'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
"""

2. zip(), map(), iter()都是内建的函数, 需要再看看

5. python, pow():
x = pow(3, 2) = 3**2
x = pow(3, 2, 2) = 3**2 % 2

6. @classmethod,
	可以从类直接调用,不必实例化,也不需要括号:
	A.do_something()

7. @staticmethod
	不需要传入self和cls, 就像普通的函数一样.也是不需要实例化就可以调用的
	A.do_what()


ord() 返回对应的 ASCII 数值，或者 Unicode 数值

11. # 逐行读取一个文件。节省内存。
with open("./notes.py", 'r') as f:
	for line in f.readlines():
		print(line)
