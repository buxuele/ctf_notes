from pymongo import MongoClient
import datetime
import pprint


"""1. 启动服务
1. sudo service mongodb status
2. sudo service mongodb start
"""

"""２．创建
# 连接，数据库，数据表:
client = MongoClient('localhost', 27017, maxPoolSize=200)
client = MongoClient('mongodb://localhost:27017/')
"""
client = MongoClient()  # connect to default host and port
db = client.test_db     # or: client['test_db']

post = {
    'author': "albert",
    'text': 'some good shit',
    'tags': ['gold', 'beef', 'milk'],
    'time': datetime.datetime.now()
}
# if table(posts) is None, create posts
posts = db.posts


"""3. 插入数据"""
p = posts.insert_one(post)   # insert one
pprint.pprint(posts.find_one()) #


# insert bulk items
more_posts = [{
    'author': "a",
    'text': 'some bad shit',
    'tags': ['belt', 'melt'],
    'time': datetime.datetime.now()
    }, {
    'author': "b",
    'text': 'new good shit',
    'tags': ['gold'],
    'time': datetime.datetime.now()
    }]

res = posts.insert_many(more_posts)


"""4. 查询。"""
# print(res.inserted_ids)
# for p in posts.find():
#     pprint.pprint(p)

print(posts.count_documents({}))


# read this for more info:
# https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.bulk_write
