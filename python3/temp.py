临时笔记:
1. 对字典的 "值" 排序:
	dict1={'a':2,'e':3,'f':8,'d':4}
	list1= sorted(dict1.items(),key=lambda x:x[1])
4. int.from_bytes(b'\x00\x10', byteorder='big')
6. 解决python3 中的 yaml问题, pip3 install pyyaml


jupyter notebook
1. 安装 notebook, pip3 install jupyter
2. 启动 notebook: jupyter notebook --allow-root
3. shift + enter, 运行代码且移动下一格
4. !pwd, run bash
5. %lsmagic 查看相关有用的命令
6. %matplotlib inline 引入绘图工具
7. %%HTML, 可以直接插入HTML
8. numpy 版本报错, 卸载再卸载,然后再卸载.
https://github.com/numpy/numpy/issues/12976#issuecomment-491688711

1. pdb, 检查bug
import pdb; pdb.set_trace()
2. eval() 函数用来执行一个字符串表达式，并返回表达式的值。
3. 内建函数 filter(function, iterable),
用于过滤序列，返回一个迭代器对象，可以使用 list() 来转换。
4. divmod(a, b) 返回一个包含商和余数的元组(a // b, a % b)
5. import time
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
6. import uuid
uuid_str = str(uuid.uuid1()).replace('-', '')
7. for i in reversed(range(1, 10)):
    print(i, end=',')
8.
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

10. 查看本机默认 字符编码:
import locale; print(locale.getdefaultlocale())


1. f, e = os.path.splitext('duck.jpg')		# // duck .jpg
2. l.get('src'), l['href'], 获取链接地址的方式是不同的.
3. attrs={'class': 'some'}, class_='thumbnail' 都可以的.
5. json, dump() dumps():
with an s take string parameters. The others take file streams.
