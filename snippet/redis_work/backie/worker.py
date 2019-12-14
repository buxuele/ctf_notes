#!/usr/bin/python3
# Time: 2019/07/27 12:03 PM
# About: 

import json


""" 
w = Worker()
w.start()
"""

class Worker:
    def __init__(self, task) -> None:
        self.task = task

    def start(self, ):
        while True:
            try:
                _dequeued_item = self.task.broker.dequeue(queuename=self.task.task_name)
                dequeued_item = json.loads(_dequeued_item)
                task_id = dequeued_item['task_id']
                task_args = dequeued_item['args']
                task_kwargs = dequeued_item['kwargs']

                print(f'running task {task_id}')
                self.task.run(*task_args, **task_kwargs)
                print(f"successfully run of task {task_id}")

            except Exception:
                print("Unable to execute task")
                continue

