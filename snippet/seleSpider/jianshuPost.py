#!/usr/bin/python3
# Time: 2019/07/10 1:13 PM
# About: 

import time
import random
import json
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""尝试自动登录简书，利用cookies"""

"""
1. 任意网站，从插件editThisCookie导出所有的cookies,保存为json文件
2. 运行此文件的过程中，会自动生成pickle文件
3. 继续　selenium 的其他功能
"""

URL = "https://www.jianshu.com/"
PKL_NAME = "target.pkl"


class Jianshu:
    def __init__(self):
        self.option = Options()
        self.option.add_argument("--start-maximized")
        self.bot = webdriver.Chrome(chrome_options=self.option)

    @staticmethod
    def make_cookie():
        data = open("jianshu.json", encoding="utf-8").read()
        py_file = json.loads(data)
        pickle.dump(py_file, open(PKL_NAME, "wb"))

    def login(self):
        self.make_cookie()
        bot = self.bot
        bot.get(URL)
        time.sleep(random.randint(3, 7))
        try:
            cookies = pickle.load(open(PKL_NAME, "rb"))
            for c in cookies:
                bot.add_cookie(c)
            bot.refresh()
        except Exception as e:
            print(e)
            print("Fail! check your cookies!")

    def post_stuff(self, hashtag):
        pass
        # later maybe


meme = Jianshu()
meme.login()



































