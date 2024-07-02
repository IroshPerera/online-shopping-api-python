# models/dto.py
class ItemDTO:
    def __init__(self, item_code,description,price,rating,stock,brand,category):
        self.item_code = item_code
        self.description = description
        self.price = price
        self.rating = rating
        self.stock = stock
        self.brand = brand
        self.category = category
        

    @classmethod
    def from_dict(cls, data):
        return cls(
            item_code=data.get('item_code'),
            description=data.get('description'),
            price=data.get('price'),
            rating=data.get('rating'),
            stock=data.get('stock'),
            brand=data.get('brand'),
            category=data.get('category')
        )
