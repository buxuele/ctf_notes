#!/usr/bin/python3
# Time: 2019/07/27 12:46 PM
# About: 


from py_stuff.redis_work.backie.task import BaseTask
import requests


class EmailTask(BaseTask):
    task_name = 'EmailTask'

    def run(self, order_id, email_address):
        url = f"https://httpbin.org/{order_id}/{email_address}"
        print(url)
        resp = requests.get(url, timeout=5.0)
        print(resp)


""" open 3 terminal:
1. run redis: redis-server
2. run tasks
3. run worker
"""


if __name__ == '__main__':
    order_id = "24dkq40"
    email_address = "example@example.com"
    e = EmailTask()
    e.delay(order_id, email_address)
































