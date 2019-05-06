一些生词
substitutions 代替,代用

笔记:
1. 使用foremost,来查看损坏的或者删除的文件
2. liunx 查看所有的系统变量: printenv | less
	# 或者 直接 env
3. quipqiup ,  solve simple substitution ciphers(替代解密?)
4. hexedit, 来查看图片的hex, 或者 xdd 也行的, 或者试一下 strings
5. 尝试在客户端添加一个 cookie, admin, 1, 然后刷新查看服务器的响应.
6. 使用 exiftool 查看图片的元信息. metadata
7. hopper, linux 反编译工具,用来查看可执行文件中函数的的详细调用过程
8. gdb + peda(是一个python2库), liunx下的一个 debug工具.
	r ,运行.
9. dmesg, 查看程序运行到哪了,具体的内存地址
10. readelf,  查看ELF文件

11. python -- requests下带参数请求的3中写法:
	 resp =requests.get(url, headers={'User-Agent': ua})
	 resp =requests.get(url, cookies={'cookie_name': cookie_value})
        resp = requests.get(url, auth=(username, password))

12. Local File Inclusion:
# http://vulnerable_host/preview.php?file=../../../../etc/passwd

13. 命令行 注入.很有意思哦, 用分号和井好来注释语句.

14. XOR cipher,
# plaintext ^ key = ciphertext
# plaintext ^ ciphertext = key

15. php中　system($_GET['c']);
# 这里的　c　可以是 anything

16. 给一个php 文件添加头部信息，欺骗服务器：GIF89a
GIF89a
<?
	// php code here
?>

17. BLIND SQL Injection
# 'AND password LIKE "<iter>%"'
from string import ascii_letters, digits
characters = ascii_letters + digits

18. 截屏或图片上的文字识别: GOCR
#　sudo apt install gocr
# gorc -h
