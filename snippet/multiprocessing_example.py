# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/29 18:29
# about:  下载某人全部的 图片


import re
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
from fake_useragent import UserAgent

u = UserAgent()

headers = {
    'User-Agent': u.random
}

def ask_page(url):
    s = requests.Session()
    page = s.get(url, headers=headers)
    print(page.status_code)
    return page


def get_link(url):
    page = ask_page(url)
    soup = BeautifulSoup(page.text, 'lxml')
    lis = soup.find_all(src=re.compile(r'cdn.sohucs.com/images'))
    # print(len(lis))
    for l in lis:
        # print(l.get('src'))
        if l.get('src')[:2] == '//':
            yield 'http:' + l.get('src')
        else:
            yield l.get('src')

# 下载图片
def download(url):
    print("正在下载：" + url)
    pic = ask_page(url).content
    fn = url.split('/')[-1]
    with open(fn, 'wb') as f:
        f.write(pic)


# 多线程下载
if __name__ == '__main__':

    start = time.time()
    for u in open('hey.txt'):

        lse = get_link(u.strip())

        pool = Pool(30)
        pool.map(download, lse)
        pool.close()
        pool.join()

    end = time.time()
    print("全部下载完成！下载一共消耗的时间是：" + str(end - start))
