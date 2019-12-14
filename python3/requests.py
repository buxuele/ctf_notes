1. requests 请求参数:allow_redirects, 默认是True, 改为False, 以免错过任何信息

2. python -- requests下带参数请求的3中写法:
	 resp =requests.get(url, headers={'User-Agent': ua})
	 resp =requests.get(url, cookies={'cookie_name': cookie_value})
     resp = requests.get(url, auth=(username, password))
3.
