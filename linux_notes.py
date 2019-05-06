2. 使用 espeak:
	# sudo apt install espeak
	# echo "hello" | espeak

3. 如何解压 some.bz2 文件
	# bzip2 -dk some.bz2 # -k, 保存原文件
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
