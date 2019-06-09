6. 使用john the ripper 破解office文档密码:
# 1. office2john.py some.docx # get a hash, save to a file
# 2. john --woldlist=rockyou myhash.text
# ./john --wordlist=/home/fc/Dowloads/rockyou.txt /home/fc/Documents/CTF/allmn/myhash.txt
7.使用john the ripper 破解shadow密码:
# 参考https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/　
8. stegsolvestegsolve.jar
# 2. java -jar stegsolve.jar

10. 在　man page中, !whoami, 一个感叹号,可以获取bash

2. 查看站点的隐藏文件:
	nikto -h [target.com]

5. gitdumper
6. sympy 基本数学计算的库

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
