# date: 2019/03/21 7:56 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. 

"""
import psycopg2

try:
	# 注意这里各个参数之间是没有逗号的，只是一个空格而已。
	con_info = "dbname='testpython' user='mm' host='localhost'" + \
		"password='my-password'"

	conn = psycopg2.connect(con_info)
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE penny (name char(40));""")
	cursor.execute("""SELECT * FROM penny""")
	rows = cursor.fetchall()
	print(rows)	# [] 成功了！！！
except Exception as e:
	print("Oh, no, failed!")
	print(e)






