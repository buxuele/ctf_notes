
6. 使用john the ripper 破解office文档密码:
# 1. office2john.py some.docx # get a hash, save to a file
# 2. john --woldlist=rockyou myhash.text
# ./john --wordlist=/home/fc/Dowloads/rockyou.txt /home/fc/Documents/CTF/allmn/myhash.txt

7.使用john the ripper 破解shadow密码:
# 参考https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/　

8. stegsolve
# 1. wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
# 2. java -jar stegsolve.jar
