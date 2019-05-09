
3. jsfuck 这种加密很有意思啊
# 例子参考 http://utf-8.jp/public/jsfuck.html

4. 最最最常见且有效的SQL注入命令是:
# ' OR 1 = 1 --

5. requests 请求参数:allow_redirects, 默认是True, 改为False,
以免错过任何信息

6. 使用john the ripper 破解office文档密码:
# 1. office2john.py some.docx # get a hash, save to a file
# 2. john --woldlist=rockyou myhash.text
# ./john --wordlist=/home/fc/Dowloads/rockyou.txt /home/fc/Documents/CTF/allmn/myhash.txt

7.使用john the ripper 破解shadow密码:
# 参考https://null-byte.wonderhowto.com/how-to/crack-shadow-hashes-after-getting-root-linux-system-0186386/　

8. stegsolve
# 1. wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
# 2. java -jar stegsolve.jar

9. 侦查图片的顺序:
#　exiftool--> foremost-->

10. 命令行处理　凯撒加密：
# for i in {1..26}; do echo "ciphertext" |caesar $i; done

11. 挂载一个ntfs文件系统, mount 命令:
sudo mkdir /mnt/you_shall_not_pass
sudo mount -o loop -t ntfs dd.img /mnt/you_shall_not_pass
