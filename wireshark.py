1. 一些常用的 wireshark 过滤数据包的命令:
ip.addr == 0.0.0.0	ip.src ip.dst
dns and/or http
tcp.port == 443  udp
tcp.analysis.flags 				# no args  显示有问题的数据包
!(nds or icmp)  				# 清除不关心的
tcp/udp contains facebook 		# 关键词查找
http.request					# 请求了哪些页面和地址
http.request.uri.query			# 搜索了哪些东西
http.response.code == 200
tcp.flags.syn == 1
sip && ftp
usb.src==host                   # protocol.src==value 按照这种格式来过滤
2.
