# python3  测试这个 序列化功能的类
import pickle

# 1. 序列化数据
"""
data = {
	'a': [1, 2.0, 3, 4+6j],
	'b': ("character string", b"byte string"),
	'c': {None, True, False}
}

with open("data.pickle", "wb") as f:
	pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

"""


# 2. 解压序列化
with open("data.pickle", "rb") as f:
	data = pickle.load(f)
	print(data)
