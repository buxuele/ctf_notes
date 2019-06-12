some gdb command:

1. info functions               固定写法,列出所有的 函数
    info registers
2. disassemble + 函数名          查看详细的过程
3. x/s + 地址[0x400684]          查看某个地址的详细内容
    xinfo + 地址
4. p + func_name                打印出函数的地址
    pdis + main
5. break * main+47              断点测试
6.



mov a, b : can be interpreted as a = b
