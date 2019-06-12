二进制文件诊断步骤，工具
ｌtrace --->exiftool---->binwalk -e [file]---> hopper

steps:
1. checksec ./binary_app
NX Enabled, so can’t embed shell code.
Canary no enabled, so can use Buffer Overflow
2. 查看所有的　functions 及其地址：
nm ./elf , readelf -s ./elf

4. dmesg | grep babyrop2
dmesg 是打印出整个系统缓冲区的内容


１．转为python能读取的字符
# pwn.p32(0xcaf3baee)
# 等于: import struct; struct.pack('<I', 0x0804853b)
# 注意查看特定函数的存储位置
4. dmesg | tail, 查看运行结果
5. pwntools shellcraft 可以处理shellcode
#  pwn.shellcraft.i386.linux.cat("flag.txt")
6. pwn.asm('push 0x08048540; ret')
把特定地址的内容转为　汇编语言, 然后输出给 nc *** **
７．tail -n 1, 输出最后一行
8. shellstrom 这个网站可以 找到很多有用的 shellcode
9. idle中, 把一个二进制的数 移位 4位
>>> 0x08048520 >> 4
'0b1111'

12. bigprimes.net 有很多有趣的数字,比如计算很大的　fib()
13. format string attack
# %s%s%s%s%s%s  内存溢出多个地址
# %3$x　 　　查看第三个值
4. steghide extract -sf stego.jpg, 给个任意的密码试试看
6. xxd -r -p , 这个是一个常用写法，把hexdump转为binary

8. gdb + peda(是一个python2库), liunx下的一个 debug工具.
	r ,运行.
