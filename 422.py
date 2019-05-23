常用诊断命令:
file --->exiftool --->strings --->hexedit --->foremost --->

2. liunx 查看所有的系统变量: printenv | less
	# 或者 直接 env
3. quipqiup ,  solve simple substitution ciphers(替代解密?)
4. hexedit, 来查看图片的hex, 或者 xdd 也行的, 或者试一下 strings
5. 尝试在客户端添加一个 cookie, admin, 1, 然后刷新查看服务器的响应.
12. Local File Inclusion:
# http://vulnerable_host/preview.php?file=../../../../etc/passwd
13. 命令行 注入.很有意思哦, 用分号和井好来注释语句.
14. XOR cipher,
# plaintext ^ key = ciphertext
# plaintext ^ ciphertext = key

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
# gocr -h


2. fcrackzip, 破解一些加密的 zip 文件
#　fcrackzip -v -D -u -p rockyou.txt secret.zip
3. hexedit, 以16进制模式,编辑查看data文件,一般是图片等媒体文件
4. 谷歌 ihdr, 查询文件的header
5. png文件的headers是: 89 50 4e 47 0d 0a 1a 0a
jpg 的header: FF d8 FF
6. foremost 也可以处理 .pcap文件(网络数据包文件)
#　foremost, 处理丢失或破损的文件
7. scapy 也可以处理网络数据包
９．binwalk -e [file] 也是来查看陌生文件的
10. 挂在一个文件系统,比如 ext4,
# sudo mount some.ext4 /media/fc
# ls -a /media/fc
11. testdisk 修复,恢复删除的文件
12. zip archive headers是 50 4B 03 04
13. 解压 7z 文件
#　7z e [file]
