from pprint import pprint as pp 
from pymongo import MongoClient as MC 

""" connect to MongoDB """

client = MC("keith-logger-mongodb.web.chal.hsctf.com", 27017, username="admin", password="keithkeithkeith")

# show all databases
print("database name: ", client.list_database_names())	# database

db = client.get_database('database')
print("Collection name", db.list_collection_names())	# collection
coll = db.get_collection("collection")

for c in coll.find():
	pp(c)

