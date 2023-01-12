import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


myclient = pymongo.MongoClient('mongodb://localhost:27017/')

print(myclient.list_database_names())
