#!/usr/bin/python3
# Time: 2019/05/02 12:50 AM
# About: itertools:  “pretty much the coolest thing ever,”

import itertools

""" itertools 中有用的函数

1. zip_longest()            默认以None 来填充分组的结果
2. permutations(iter, len)  排序组合, 重点在排序, 包含逆序
3. combinations(iter, n)    可迭代对象中的元素不与自身重复
4. combinations_with_replacement(iter, n),     有重复
5. count(start=1, step=2)
6. repeat(4, 3)           # 4, 4, 4
7. cycle(iter)
8. accumulate(iter)          # 累加
9. product(iter, iter)

"""
# 1. 排序组合 permutations
# for possible in itertools.permutations(range(1, 50), 2):
#     print(possible)
#

x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']

print(list(zip(x, y)))
print(list(itertools.zip_longest(x, y)))
