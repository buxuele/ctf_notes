1. math.sqrt(7) ----> 2.6457513110645907,  <class 'float'>
3. collections.Counter() 是可以直接操作交集,合集   源代码 Line 866
   >  同样的 set() 集合可以直接操作 交集 合集: ret = {"a", "b"} & {"d", "d"}


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

1. atom 中全局搜索文件的快捷键是　ctrl + Shift +　Ｆ

2. 这种写法很清秀啊。list(range(2,10,2))　--->  [2, 4, 6, 8]

3. python的装饰器，本质上是一个函数，它把被传入的函数包裹在自己里面，
   自身也可以执行东西。

4. [1,2,3] * 2 ----> [1, 2, 3, 1, 2, 3]

5. [1,2] + [3,4] ----> [1,2, 3, 4]

6. 对一个浮点数取3位小数
   a = 3.14158
   ret = round(a, 3)

7. 获取一个字典所有的键，直接用list()来转换
   d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
   print(list(d))

8. 根据用户名来查找某个用户在社交媒体上的账户信息
   ```python
   https://github.com/sherlock-project/sherlock
   python3 sherlock  [fanchuang]

   可以根据这个库的思想来改写自己的库。比如改变网站列表。
   ```
   
9. 查看某个包的安装路径
      ```python
      import speech_recognition as sr
      import os.path as p
      print(p.dirname(sr.__file__))
      ```

10. a = sys.maxsize         # 9223372036854775807   , len(str(a)) = 19

11. os  文件路径的一些用法
    ```python
       - os.path.realpath = os.path.abspath, 返回的是某个文件的绝对路径
       - os.path.dirname(your_file_path), 返回的是某个文件所在的文件夹的路径。
       - os.path.join()的正确用法。x = os.path.join("/home/fc/Desktop", "data.json")
    ```

12. import operator; "Same as a[b]."

13. time.monotonic(),

14. 如果想直接使用 self 作为一个可迭代对象的话，需要自己来实现一个 __iter__()方法。

15. pathlib.Path('.')  / "some.txt" 操作文件路径，是一种更简洁更优雅的方式。

16. bytes("some info", "utf-8"), 按照指定的 encoding 将字符串转换为字节序列；

17. flask 获取用户的 ip 地址 :

 ```python
 from flask import request
 # request.environ['REMOTE_ADDR']
 request.remote_addr
 ```
18.   flask_wtf 获取用户提交的信息，只需要, form.msg_info.data.  加上一个 .data
19. WSGI is the Web Server Gateway Interface
