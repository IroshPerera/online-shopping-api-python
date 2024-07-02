# services/item_service.py
from dto.itemDTO import ItemDTO
from model.item import Item
from repository.item_repository import ItemRepository

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def add_item(self, item_data):
        item_dto = ItemDTO.from_dict(item_data)
        if self.repository.find_by_id(item_dto.item_code):
            return {"error": "Item already exists"}, 400
        item = Item(item_dto.item_code, item_dto.description , item_dto.price, item_dto.rating, item_dto.stock, item_dto.brand, item_dto.category)
        self.repository.insert(item)
        return {"success": True}, 201

    def get_item(self, item_code):
        item = self.repository.find_by_id(item_code)
        if item:
            return item, 200
        return {"error": "Item not found"}, 404

    def update_item(self, item_code, item_data):
        if self.repository.update(item_code, item_data).modified_count:
            return {"success": True}, 200
        return {"error": "Item not found or no update made"}, 404

    def delete_item(self, item_code):
        if self.repository.delete(item_code).deleted_count:
            return {"success": True}, 200
        return {"error": "Item not found"}, 404
    
    def get_all_items(self):
        return self.repository.find_all(), 200
