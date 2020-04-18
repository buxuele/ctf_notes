#!/usr/bin/python2
# Time: 2019/05/03 2:35 AM
# About: pwn.xor

import pwn

with open("cipher.txt") as handle:
    cipher = handle.read()
    cipher = cipher.decode("base64")

    for i in range(256):
        message = pwn.xor(cipher, i)
        print(message)
