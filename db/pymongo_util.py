import datetime
import pymongo
from pprint import pprint
from pymongo import MongoClient


class PyMongoUtil:
    def __init__(self, db_url, port, db_name: str):
        self.client = self.connect_db(db_url, port)
        self.db = self.access_db(db_name)

    def connect_db(self, db_url: str = "localhost", port: int = 27017):
        # self.client = MongoClient('mongodb://localhost:27017/')
        return MongoClient(db_url, port)

    def access_db(self, db_name: str):
        return self.client[db_name]

    def access_collection(self, collection_name: str):
        return self.db[collection_name]
        # print(collection)

    # 插入
    def inset_document(self, collect_name, inset_doc):
        post_id = ""
        if type(inset_doc) == dict:
            post_id = self.db[collect_name].insert_one(inset_doc).inserted_id
        elif type(inset_doc) == list:
            post_id = self.db[collect_name].insert_many(inset_doc).inserted_ids
        return post_id

    # 查找
    def find(self, collect_name, params=None):
        if params is None:
            result = self.db[collect_name].find_one()
        else:
            result = self.db[collect_name].find_one(params)
        return result

    def find_id(self, collect_name, post_id):
        result = self.db[collect_name].find_one({"_id": post_id})
        return result

    def find_all(self, collect_name, params=None):
        result_list = []
        if params is None:
            for item in self.db[collect_name].find():
                result_list.append(item)
        else:
            for item in self.db[collect_name].find(params):
                result_list.append(item)
        return result_list

    def find_range(self, collect_name, params, sort):
        tmp_list = []
        for post in self.db[collect_name].find(params).sort(sort):
            tmp_list.append(post)
        return tmp_list

    # 建立索引
    def indexes_create(self, collect_name, params, is_unique=True):
        self.db[collect_name].create_index([(params, pymongo.ASCENDING)], unique=is_unique)
        return self.db[collect_name].index_information()

    def indexes_list(self, collect_name):
        return self.db[collect_name].index_information()

    def show_collection_list(self):
        return self.db.list_collection_names()

    # 计算doc数量
    def count(self, collect_name, params=None):
        if params is None:
            result_num = self.db[collect_name].count_documents({})
        else:
            result_num = self.db[collect_name].count_documents(params)
        return result_num

    def stary(self):
        pass


if __name__ == '__main__':
    collection_name = "collection_test"
    py_mongo_util = PyMongoUtil("localhost", 27017, "test")

    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    post1 = {"author": "AAA",
             "text": "My first blog post!",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow()}

    post_list = [{"author": "CCC",
                  "text": "My first blog post!",
                  "tags": ["mongodb", "python", "pymongo"],
                  "date": datetime.datetime.utcnow()},
                 {"author": "DDD",
                  "text": "My first blog post!",
                  "tags": ["mongodb", "python", "pymongo"],
                  "date": datetime.datetime.utcnow()}
                 ]

    # post_id1 = py_mongo_util.inset_document(collection_name, post)

    # post_id2 = py_mongo_util.inset_document(collection_name, post1)

    # post_id3 = py_mongo_util.inset_document(collection_name, post_list)

    # pprint(py_mongo_util.show_collection_list())

    py_mongo_util.find(collection_name)

    py_mongo_util.find(collection_name, {"author": "AAA"})

    # py_mongo_util.find_id(collection_name, post_id2)

    py_mongo_util.find_all(collection_name)

    d = datetime.datetime(2021, 11, 16, 18)
    find_params = {"date": {"$lt": d}}
    py_mongo_util.find_range(collection_name, find_params, "author")
    tmp_list = py_mongo_util.find_all(collection_name, {"author": "AAA"})
    # pprint(tmp_list)

    num1 = py_mongo_util.count(collection_name)
    num2 = py_mongo_util.count(collection_name, {"author": "AAA"})
    pprint(num1)
    pprint(num2)

    # 索引
    collection_a_name = "test2"
    user_a = [
        {'user_id': 211, 'name': 'Luke'},
        {'user_id': 212, 'name': 'Ziltoid'},
    ]
    py_mongo_util.inset_document(collection_a_name, user_a)
    # indexes_list = py_mongo_util.indexes_create(collection_a_name, "user_id")
    indexes_list = py_mongo_util.indexes_list(collection_a_name)
    pprint(indexes_list)

    # print(post_id3)
