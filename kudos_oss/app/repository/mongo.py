import os
from pymongo import MongoClient

COLLECTION_NAME = 'kudos'

class MongoRepository(object):
    def __init__(self):
#       mongo_url = os.environ.get('MONGO_URL')
        mongo_url = os.environ.get('mongodb://mongo_user:mongo_secret@0.0.0.0:27017/')
        self.db = MongoClient(mongo_url).kudos

        def find_all(self, selector):
            return self.db.kudos.find(selector)

        def find(self, selector):
            return self.db.kudos.find_one(selector)

        def create(self,kudo):
            return self.db.kudos.insert_one(kudo)

        def update(self,select, kudo):
            return self.db.kudos.replace_one(selector,kudo).modified_count

        def delete(self,selector):
            return selfdb.kudos.delete_one(elector).deleted_count


