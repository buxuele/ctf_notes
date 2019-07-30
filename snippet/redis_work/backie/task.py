#!/usr/bin/python3
# Time: 2019/07/27 11:48 AM
# About: 

import abc
import json
import uuid

from .broker import Broker


class BaseTask(abc.ABC):
    task_name = None

    def __init__(self):
        if not self.task_name:
            raise ValueError(" need a name.")
        self.broker = Broker()

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError('task run method must be implemented')

    def delay(self, *args, **kwargs):
        try:
            task_id = str(uuid.uuid4())
            _task = {"task_id": task_id, "args": args, "kwargs": kwargs}
            serialized_task = json.dumps(_task)
            self.broker.enqueue(queuename=self.task_name, item=serialized_task)
            print(f"task: {task_id} successfully queued.")
        except Exception:
            raise Exception("unable to publish task to the broker.")































