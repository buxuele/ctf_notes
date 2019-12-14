***************** 各种解压 ******************
1. 解压 7z 文件 	#　7z e [file]
2. cpio - copy files to and from archives
	#  cpio -i -F initramfs.cpio # How to extract a ASCII cpio archive
3. 解压 some.bz2 文件
	# bzip2 -dk some.bz2 # -k, 保存原文件
4. fcrackzip, 破解一些加密的 zip 文件
#　fcrackzip -v -D -u -p rockyou.txt secret.zip

***************** mount ******************
1. 挂在一个文件系统,比如 ext4,
# sudo mount some.ext4 /media/fc
# ls -a /media/fc
2. 挂载一个文件系统, mount 命令:
mkdir /mnt/you
sudo mount -o loop -t ntfs dd.img /mnt/you


***************** others ******************
2. liunx 查看所有的系统变量: printenv | less
	# 或者 直接 env
3. quipqiup ,  solve simple substitution ciphers(替代解密?)
4. hexedit, 来查看图片的hex, 或者 xdd 也行的, 或者试一下 strings
5. 尝试在客户端添加一个 cookie, admin, 1, 然后刷新查看服务器的响应.
12. Local File Inclusion:
# http://vulnerable_host/preview.php?file=../../../../etc/passwd
14. XOR cipher,
# plaintext ^ key = ciphertext
# plaintext ^ ciphertext = key

16. 给一个php 文件添加头部信息，欺骗服务器：GIF89a
GIF89a
<?
	// php code here
?>
17. BLIND SQL Injection
# 'AND password LIKE "<iter>%"'
18. 截屏或图片上的文字识别: GOCR  # gocr -h
11. testdisk 修复,恢复删除的文件
12. zip archive headers是 50 4B 03 04
