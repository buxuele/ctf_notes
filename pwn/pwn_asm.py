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
