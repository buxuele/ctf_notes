common re pattern:
1. find all links in a html:
# re.findall('"((http|https)://.*?)"', html)

2. remove <a> tag:
# html = re.sub('<a.*?>|</a>', '', html)

my note:

# basic rules
\w  匹配字母数字及下划线
\W  匹配非字母数字及下划线
\s  匹配任意空白字符，等价于 [\t\n\r\f].
\S  匹配任意非空字符
\d  匹配任意数字，等价于 [0-9]
\D  匹配任意非数字
\A  匹配字符串开始
\Z  匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
\z  匹配字符串结束
\G  匹配最后匹配完成的位置
\n  匹配一个换行符
\t  匹配一个制表符
^   匹配字符串的开头
$   匹配字符串的末尾。
.   匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
*   匹配0个或多个的表达式。
+   匹配1个或多个的表达式。
?   匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n} 精确匹配n个前面表达式。
a|b 匹配a或b
()  匹配括号内的表达式，也表示一个组, use, group() to read stuff inside
[...]   用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]  不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
{n, m}  匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式

*****about flags*****
re.I    使匹配对大小写不敏感
re.L    做本地化识别（locale-aware）匹配
re.M    多行匹配，影响 ^ 和 $
re.S    使 . 匹配包括换行在内的所有字符
re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
在网页匹配中较为常用的为re.S、re.I。

********Attention !!! Trap here****************
1. .*? greedy match
2. but, if .*? in the end of line, it's none
3. re.S    is a flag.
4. \.  match   .
5. . match blank space, try \w

1. re.match(), start from beginning
2. re.search(), scan all strings, returns the first match
3. re.findall(), find all match
4. re.sub(old, new, target), replace something
