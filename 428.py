常用诊断命令:
file --->exiftool --->strings --->hexedit --->foremost --->

1. imagemagick, 命令行图片处理库,有很多丰富的功能.
# maigck -version

2. fcrackzip, 破解一些加密的 zip 文件
#　fcrackzip -v -D -u -p rockyou.txt secret.zip

3. hexedit, 以16进制模式,编辑查看data文件,一般是图片等媒体文件

4. 谷歌 ihdr, 查询文件的header

5. png文件的headers是: 89 50 4e 47 0d 0a 1a 0a
jpg 的header: FF d8 FF

6. foremost 也可以处理 .pcap文件(网络数据包文件)
#　foremost, 处理丢失或破损的文件

7. scapy 也可以处理网络数据包

８．　exiftool, 查看陌生文件的隐藏的信息

９．binwalk -e [file] 也是来查看陌生文件的

10. 挂在一个文件系统,比如 ext4,
# sudo mount some.ext4 /media/fc
# ls -a /media/fc

11. testdisk 修复,恢复删除的文件

12. zip archive headers是 50 4B 03 04

13. 解压 7z 文件
#　7z e [file]
