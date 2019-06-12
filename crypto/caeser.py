enc = "CGULKVIPFRGDOOCSJTRRVMORCQDZG"

for i in range(26):
	ans = ''
	for j in range(len(enc)):
		d = ord(enc[j]) - i - (26-j)
		while d < 65:
			d += 26
			print(d, "hahahhaha")
		ans += chr(d)

	print(ans.lower())


#　凯撒加密，　注意一点 chr('a') < 65, 需要再加上26
