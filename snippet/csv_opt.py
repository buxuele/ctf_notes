# when: 2019/03/30 9:36 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. writer = csv.writer(f, delimiter=' ')
2. writerow, writerows,写入多行，需要二维列表
3. writer = csv.DicWriter(f）, 写入字典类型、
4.
"""

import csv


with open("a.csv", 'w') as f:
    writer = csv.writer(f, delimiter=' ')

    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1000001', 'mike', 50])


"""
读取 csv:

import pandas as pd

df = pd.read_csv("data.csv")
print(df)

"""