#!/usr/bin/python3
# Time: 2019/07/10 3:15 PM
# About: 


import time
import json
import pickle


"""
注意pickle的使用，序列化对象和python类型，　互相转换
"""

data = open("jianshu.json", encoding="utf-8").read()
py_file = json.loads(data)
print(type(py_file))

for p in py_file:
    print(p)


pickle.dump(py_file, open("jianshu.pkl", "wb"))
print("good work!")
time.sleep(2)


data = pickle.load(open("jianshu.pkl", "rb"))
print(data)
print("fine work!")































