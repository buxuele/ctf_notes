1. 如何加速git clone
	- 官方推荐使用https, 而不是ssh. stackoverflow上的解释是:可以通过防火墙
	- 如果不需要 历史记录的话:
# git clone --depth 1 some@repo

2. 使用 espeak:
	# sudo apt install espeak
	# echo "hello" | espeak

3. 如何解压 some.bz2 文件
	# bzip2 -dk some.bz2 # -k, 保存原文件

4. 添加 subl 到终端:
	1. open this file:
	# sudo gedit ~/.bashrc
	2. add a alias for sublime:
	alias subl='/home/fc/Downloads/sublime_text_3/sublime_text'
	3. update and test it:
	source ~/.bashrc
	subl

5. SQL注入 例子:
   user admin' OR 1=1 --
   pass admin' OR 1=1 --
# 'UNION SELECT 1, 2, 3--  pass is the same

6. @classmethod,
	可以从类直接调用,不必实例化,也不需要括号:
	A.do_something()

7. @staticmethod
	不需要传入self和cls, 就像普通的函数一样.也是不需要实例化就可以调用的
	A.do_what()

8. 查看 CPU 总的线程数：
# grep 'processor' /proc/cpuinfo | sort -u | wc -l

9. 判断 RAM 和 I/0 瓶颈,每 5 秒采样一次，共 10 次。
# vmstat 5 10

10. sar 之 CPU 使用情况（判断 CPU 瓶颈）
命令：sar -u 5 10，每 5 秒采样一次，共 10 次

11.ctrl-w 删除你键入的最后一个单词，
   ctrl-u 可以删除行内光标所在位置之前的内容

12.  # 把标准错误导入另一个文件,剩下的都是标准输出
find / -size 33c -user fc -group team2 2>/dev/null

13. cat data.txt | sort | uniq -c |grep -v "10"

14. gunzip [something]    bunzip2 [something]


15. 使用 ssh key 登录(切换用户身份登录同一台主机):
ssh -i sskey.private userX@localhost

16. stat filename, 显示文件的详细信息

17. 在命令结尾加上&,表示后台运行, fg 可以跳出来.

18. 让 cd, 对大小写不敏感,把下面这行写入.bashrc 里面,以长久生效
# bind "set completion-ignore-case off"
