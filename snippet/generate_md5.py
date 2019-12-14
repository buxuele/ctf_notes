# Time: 2019/05/16 1:14 PM
# About: 

from hashlib import md5

"""
generate md5 hash:

plaintext = 'this is a good joke'
res = md5(plaintext.encode('utf-8')).hexdigest()
print(res)
# 598d82d97a42280cf89636cc1ab47dba


# single example:
def md5_test(someStr):
	# 直接传入也可以，使用 update() 也可以。
	# hash = hashlib.md5(someStr.encode("utf-8"))
	hash = hashlib.md5()
	hash.update(someStr.encode("utf-8")) # 这个必须转为 bytes类型
	return hash.hexdigest() # 使用一个32位的16进制字符串表示。

print(md5_test("hello"))

"""


i = 0
while True:
    plaintext = '0e%d' % i
    h = md5(plaintext.encode('utf-8')).hexdigest()

    if h.startswith('0e'):
        if h[2:].isdigit():
            print(plaintext, h)
            break
    print(plaintext, h)
    i += 1

