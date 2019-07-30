#!/usr/bin/python3
# Time: 2019/07/27 12:51 PM
# About: 


from py_stuff.redis_work.run_task import EmailTask
from py_stuff.redis_work.backie.worker import Worker


if __name__ == '__main__':
    e = EmailTask()
    w = Worker(task=e)
    w.start()































