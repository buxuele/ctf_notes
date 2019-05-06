"""
二进制文件诊断步骤，工具

１．转为python能读取的字符
# pwn.p32(0xcaf3baee)
# 等于: import struct; struct.pack('<I', 0x0804853b)

2. nc打开连接的同时传给一定的参数, 使用 cat 不加参数,等待输入
#  (python -c print("something") ; cat) | nc host port

3. 也是一个查看 二进制的工具
# readelf -s program | grep something
# 注意查看特定函数的存储位置

4. dmesg | tail, 查看运行结果

5. pwntools shellcraft 可以处理shellcode
#  pwn.shellcraft.i386.linux.cat("flag.txt")

6. # pwn.asm('push 0x08048540; ret')
把特定地址的内容转为　汇编语言, 然后输出给 nc *** **

７．tail -n 1, 输出最后一行

8. shellstrom 这个网站可以 找到很多有用的 shellcode

9. idle中, 把一个二进制的数 移位 4位
>>> 0x08048520 >> 4
'0b1111'

10. 在　man page中, !whoami, 一个感叹号,可以获取bash

11. 使用pwntools来修改 可执行文件

12. bigprimes.net 有很多有趣的数字,比如计算很大的　fib()

13. format string attack
# %s%s%s%s%s%s  内存溢出多个地址
# %3$x　 　　查看第三个值

14.


"""

from pwn import *

elf = ELF("./exefile")

# 列出所有的function
for key, address in elf.symbols.iteritems():
    print(key, hex(address))

#　修改特定的函数, ret, return None, do nothing
elf.asm(elf.symbols['yourfunc'], 'ret')

number = 111111111111111111111111111111

# 0xFFFFFFFF 取出前32位
elf.asm(elf.symbols['calcu'], 'mov eax,%s\nret\n' %(hex(number & 0xFFFFFFFF)))

# 把修改过的，　保存为新的文件
ｅlf.save('./newfile')
