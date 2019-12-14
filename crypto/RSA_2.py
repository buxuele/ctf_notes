# python3
import codecs
from Crypto.Util.number import inverse

n = 561985565696052620466091856149686893774419565625295691069663316673425409620917583731032457879432617979438142137
e = 65537
c = 328055279212128616898203809983039708787490384650725890748576927208883055381430000756624369636820903704775835777

# http://factordb.com/   查看质数


p = 29 				  # n 不是质数，　n = 29 * 'some_num'
q = n // p 			  # n = p * q		# 这个是定理

phi = (p-1) * (q-1)
d = inverse(e, phi)
m = pow(c, d, n)

print(m)
print(codecs.decode(hex(m)[2:], "hex"))
