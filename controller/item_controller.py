from flask import Blueprint, request, jsonify
from service.item_service import ItemService

item_controller = Blueprint('item_controller', __name__)
item_service = None

#add cors origin
@item_controller.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


def initialize_service(service):
    global item_service
    item_service = service

@item_controller.route('/items', methods=['POST'])
def add_item():
    data = request.json
    result, status = item_service.add_item(data)
    return jsonify(result), status

@item_controller.route('/items/<item_code>', methods=['GET'])
def get_item(item_code):
    result, status = item_service.get_item(item_code)
    return jsonify(result), status

@item_controller.route('/items/<item_code>', methods=['PUT'])
def update_item(item_code):
    data = request.json
    result, status = item_service.update_item(item_code, data)
    return jsonify(result), status

@item_controller.route('/items/<item_code>', methods=['DELETE'])
def delete_item(item_code):
    result, status = item_service.delete_item(item_code)
    return jsonify(result), status

@item_controller.route('/items', methods=['GET'])
def get_all_items():
    result, status = item_service.get_all_items()
    return jsonify(result), status
