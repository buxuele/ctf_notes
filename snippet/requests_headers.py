# when: 2019/03/30 10:07 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. failed...

"""
import requests
from fake_useragent import UserAgent

ua = UserAgent()

url = 'https://m.weibo.cn/'
headers = {'Host': 'm.weibo.cn',
           'Referer': 'm.weibo.cn',
           "User-Agent": ua.random,
           "X-Requested-With": 'XMLHttpRequest'}


def grab():
    html = requests.get(url, headers=headers).text
    print(html)


if __name__ == "__main__":
    grab()



