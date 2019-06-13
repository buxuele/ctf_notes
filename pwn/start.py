1. ROP 和 buffer overflow 是2种不同的类型





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
