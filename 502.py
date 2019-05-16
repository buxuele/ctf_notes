2. 查看站点的隐藏文件:
	nikto -h [target.com]
3. 命令行注入, 用分号:
ls -a ; ls -l
5. gitdumper
6. sympy 基本数学计算的库
7. steghide 查找文件的隐藏信息
# steghide extract -sf stg.jpg
10. ls, cat, grep, 这些常用的命令都是在 /bin目录下的.
	find, 是在 /usr/bin/find
11. 以字节为单位, 编辑一个文件
	dd if=originFile of=outputFile ibs=1 skip=17
	# ibs 每次读取的字节数, skip 从头开始跳过的的字节数

13. crackstation 一个解密hash的网站，

15. 把本地.py文件 复制到远程主机上:
	# 先base64 编码,去掉换行后,放进粘贴板
	# base64 yourfile.py | tr -d "\n" | xclip
	# echo "base64_stuff" | base64 -d > att.py
