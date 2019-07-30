#!/usr/bin/python3
# Time: 2019/07/13 10:14 PM
# About: 

from pprint import pprint as pp
from pymongo import MongoClient as MC


def find_coll(db_name, coll_name):
    c = MC('localhost', 27017)
    coll = c.get_database(db_name).get_collection(coll_name)

    for i in coll.find():       # .find()
        pp(i)
    # return coll


find_coll("movie_database", "movie_collection")
