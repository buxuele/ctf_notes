# when: 2019/04/05 11:53 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

import sqlite3

# if db, conn db, else, create db
conn = sqlite3.connect("my_database.db")

cur = conn.cursor()

# table can be created once
# cur.execute("""create table quotes_tb(
#     title text,
#     author text,
#     tags text
#     )""")

# insert some data
cur.execute("""insert into quotes_tb values(
            'Python is awesome!',
            'fanchuang',
            'python'
            )""")

conn.commit()
conn.close()



