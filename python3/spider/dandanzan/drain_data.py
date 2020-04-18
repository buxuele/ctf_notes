#!/usr/bin/python3
# Time: 2019/07/13 4:55 AM

from gevent import monkey
monkey.patch_all()

import re
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import gevent
from gevent import pool
from pymongo import MongoClient as MC

# ******************************   common stuff  ***************************
ua = UserAgent()
headers = {"User-Agent": ua.random}
s = requests.Session()
start_url = "https://www.dandanzan.com/dianying/"
urls = [start_url if i == 1 else f'{start_url}/index_{i}.html' for i in range(1, 10)]


# 1097
# general function
def make_soup(url):
    html = s.get(url, headers=headers).text
    return BeautifulSoup(html, 'lxml')


# ******************************   real work  ***************************
def get_link(url):
    soup = make_soup(url)
    lis = soup.find_all("a", href=re.compile(r'/dianying/\d+'), class_='thumbnail')
    # print(len(lis))       # 24
    for l in lis:
        # print(l['href'])
        # print(f'https://www.dandanzan.com{l["href"]}')
        # yield f'https://www.dandanzan.com{l["href"]}'
        u = f'https://www.dandanzan.com{l["href"]}'
        get_info(u)


# 获取 想要的内容
def get_info(url):
    data = {}
    soup = make_soup(url)
    data["name"] = soup.find(class_='product-title').contents[0].split(' ')[0]
    data["url"] = url
    data["english_name"] = soup.find(class_='product-title').contents[0].split(' ')[1]
    data["year"] = soup.find(class_='product-title').contents[1].text[1:-1]
    data["rate"] = soup.find(class_='product-title').contents[-1].text
    data["author"] = soup.find_all(class_='product-excerpt')[0].text[3:]
    data["actor"] = soup.find_all(class_='product-excerpt')[1].text[3:]
    data["type"] = soup.find_all(class_='product-excerpt')[2].text[3:]
    data["another_name"] = soup.find_all(class_='product-excerpt')[4].text[:3]
    data["about"] = soup.find_all(class_='product-excerpt')[5].text[5:]
    save_data(data)


def save_data(data):
    c = MC('localhost', 27017)
    db = c['movie_database']
    coll = db['movie_collection']
    coll.insert_one(data)


def main():
    t1 = time.time()
    urls = [start_url if i == 1 else f'{start_url}/index_{i}.html' for i in range(1, 1097)]

    poo = pool.Pool(30)
    jobs = []
    for u in urls:
        jobs.append(poo.spawn(get_link, u))
    gevent.joinall(jobs)

    t2 = time.time()
    print("cost time: ", t2 - t1)


if __name__ == '__main__':
    # a = "https://www.dandanzan.com/dianying/25531.html"
    # get_info(a)
    # get_link(a)
    main()

