from pwn import * 

# pwntools 中常用的命令
r.remote(host, port)

r.recvuntil("?")	# 指的是　直到出现这个字符
r.sendline("my answer")

# 按照指定的分隔符，打印出返回信息
print(r.recvutil(">").decode("UTF-8"))

r.interactive()	# 不退出回话, 与远程服务器交互

chattycathy
