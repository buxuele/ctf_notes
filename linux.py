1. 把Mannaged mode 切换成 Monitor mode, 然后方便wireshark来抓包
	# sudo airmon-ng start wlx488ad2683511
2. 使用 espeak:
	# sudo apt install espeak # echo "hello" | espeak
4. 添加 subl 到终端, 设置别名:
	sudo gedit ~/.bashrc
	alias subl='/home/fc/Downloads/sublime_text_3/sublime_text'
	source ~/.bashrc
8. 查看 CPU 总的线程数：
# grep 'processor' /proc/cpuinfo | sort -u | wc -l
11. ctrl-u 可以删除行内光标所在位置之前的内容
12.  # 把标准错误导入另一个文件,剩下的都是标准输出
find / -size 33c -user fc -group team2 2>/dev/null
13. cat data.txt | sort | uniq -c |grep -v "10"
15. 使用 ssh key 登录(切换用户身份登录同一台主机):
ssh -i sskey.private userX@localhost
16. stat filename, 显示文件的详细信息
17. 在命令结尾加上&,表示后台运行, fg 可以跳出来.
18. nc打开连接的同时传给一定的参数, 使用 cat 不加参数,等待输入
 for i in {1..50}; do ltrace ./app 'python2 -c "print 'a'*$i"'; done
19. nmap localhost -p31000-32000
８．常用命令:
	查看已经设置过的命令别名：　alias
	rev, 逆转一个字符串
	tac, 逆转一个文件的每行的顺序
	tr -d 删除字符
	cut -d 剪切字符
3. oepnssl 语法:
#　$ openssl s_client -connect www.feistyduck.com:443 other_paras
# 这里的这个 s_client 是固定写法,不是变量名称
9. crontab的用法.
10. 命令行处理　凯撒加密：
# for i in {1..26}; do echo "ciphertext" |caesar $i; done
5. ltrace -s 1000 ./app , 把执行的结果 stringSize 扩大到1000 以免错过某些信息
6. apktool 解压apk文件
7. sudo apt install dosbox，　执行MS-DOS文件
8. stegcracker <file> [<wordlist>] 恢复隐藏的文件
9. zbarimg some.png 解析二维码
10. pycharm 重新格式化代码 全选然后: Ctrl+Alt+L
15. 在/home目录下查找以.txt结尾的文件名
find /home -name "*.txt"
７．tail -n 1, 输出最后一行
12. 除了使用strings  也使用 tail 试试看
3. 输入sudo lshw -C network显示Ubuntu正在使用的网卡信息
