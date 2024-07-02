# repositories/item_repository.py
from pymongo.collection import Collection

class ItemRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def find_by_id(self, item_code):
        return self.collection.find_one({"_id": item_code})

    def insert(self, item):
        return self.collection.insert_one(item.to_dict())

    def update(self, item_code, data):
        return self.collection.update_one({"_id": item_code}, {"$set": data})

    def delete(self, item_code):
        return self.collection.delete_one({"_id": item_code})

    def find_all(self):
        return list(self.collection.find())