1. xxd 命令 用来生成一个hexdump

2. nc, 用来连接确定的服务器端口

3. oepnssl 语法:
#　$ openssl s_client -connect www.feistyduck.com:443 other_paras
# 这里的这个 s_client 是固定写法,不是变量名称

4. nmap localhost -p31000-32000

5. crontab的用法.
	#　．．．
	添加天气查询和其他服务...
	定时打印某些语录

６．ｌtrace 来运行二进制脚本，并且查看详细的运行过程

７．grep -i "info", 用-i来查找想要的字符串

８．常用命令:
	命令行打开文件管理器：　nautilus .
	命令行打开图片查看器：　eog .
	查看已经设置过的命令别名：　alias
	rev, 逆转一个字符串
	tac, 逆转一个文件的每行的顺序
	tr -d 删除字符
	cut -d 剪切字符

11. 0*41转为 int:
# python3!
>>>int(0x41)

12. python中:
	ord(<string>) --> ascii value <int>,
	chr() 用一个整数作参数，返回一个对应的字符
	bin() 返回一个整数 int 的二进制表示
	0b+others, ob 是自动添加的前缀

15. grep -oE "picoCTF{.*}"
# 查找唯一的结果,使用正则表达式

16. linux:
# base64 -d filename

17. 解密图片的一个库,zsteg:
#　detect stegano-hidden data in PNG & BMP
