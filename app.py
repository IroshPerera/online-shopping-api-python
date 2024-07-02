# app.py
from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from controller.item_controller import item_controller, initialize_service
from repository.item_repository import ItemRepository
from service.item_service import ItemService


app = Flask(__name__) 
app.config.from_object(Config)

mongo = PyMongo(app)
db = mongo.db
item_repository = ItemRepository(db.items)
item_service = ItemService(item_repository)

initialize_service(item_service)

app.register_blueprint(item_controller)

if __name__ == '__main__':
    app.run(debug=True)
