#!/usr/bin/python3
# Time: 2019/07/27 1:14 PM
# About: test how to use Mixin in complex class-files


class BaseClass:
    def __init__(self):
        self.name = 1


# 一个 Mixin 一般只包含一个典型的 特征(作用)
class JobMixin:
    def do_job(self):
        return "maybe"


# ************ use Mixin ********************
class RealClass(BaseClass, JobMixin):
    def __init__(self):
        super().__init__()
        self.do_job()


r = RealClass()































