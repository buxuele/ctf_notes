#!/usr/bin/python3
# Time: 2019/07/07 12:10 PM
# About: works fine!!!

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


""" 
尝试登录，并且点赞别人的微博
install Firefox driver
1. wget:   https://github.com/mozilla/geckodriver/releases 
2. chmod +x geckodriver
3. sudo mv geckodriver /usr/local/bin/
"""


class WeiboBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.option = Options()
        self.option.add_argument("--start-maximized")
        self.bot = webdriver.Chrome(chrome_options=self.option)

    def login(self):
        bot = self.bot
        bot.get("https://weibo.com/")
        time.sleep(random.randint(3, 7))
        username = bot.find_element_by_id("loginname")
        password = bot.find_element_by_name("password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(random.randint(3, 7))

    def like_weibo(self, hashtag):
        bot = self.bot

        for i in range(1, 5):

            bot.get(f"https://s.weibo.com/weibo/{hashtag}?topnav=1&wvr=6&b=1&page={i}")
            time.sleep(random.randint(3, 7))
            # bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(random.randint(3, 7))
            buttons = bot.find_elements_by_xpath('//*[@id="pl_feedlist_index"]/div[1]/div[*]/div/div[2]/ul/li[4]/a')

            for b in buttons:
                time.sleep(random.randint(3, 7))
                b.click()


meme = WeiboBot("15026758603", "7398611111")
meme.login()
meme.like_weibo("跑步")























