class Item:
    def __init__(self, item_code, description, price , rating,stock,brand,category):

        self.item_code = item_code
        self.description = description
        self.price = price
        self.rating = rating
        self.stock = stock
        self.brand = brand
        self.category = category

    def to_dict(self):
        return {
            "_id": self.item_code,
            "item_code": self.item_code,
            "description": self.description,
            "price": self.price,
            "rating": self.rating,
            "stock": self.stock,
            "brand": self.brand,
            "category": self.category
            
        }
