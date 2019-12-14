#!/usr/bin/python3
# Time: 2019/07/27 11:56 AM
# About: 

import redis


class Broker:
    """
    use redis as our broker.
    this is a basic FIFO queue
    """
    def __init__(self):
        host = "localhost"
        port = "6379"
        password = None
        self.redis_instance = redis.StrictRedis(
            host=host, port=port, password=password, db=0, socket_timeout=8.0
        )

    def enqueue(self, item, queuename):
        self.redis_instance.lpush(queuename, item)

    def dequeue(self, queuename):
        dequed_item = self.redis_instance.brpop(queuename, timeout=3)
        if not dequed_item:
            return None
        dequed_item = dequed_item[1]
        return dequed_item



























