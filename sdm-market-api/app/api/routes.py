from flask import jsonify, request, current_app
from app.api import bp
from app.schemas.user import user_schema, users_schema
from app.schemas.product import product_schema, products_schema
from app.schemas.purchase import purchase_schema, purchases_schema
from app.services.user_service import UserAlreadyExistsError

@bp.route('/users', methods=['POST'])

# User routes
def create_user():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
        
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify({'error': 'Validation error', 'messages': errors}), 400

    user = current_app.user_service.create_user(data)
    return jsonify(user_schema.dump(user)), 201

@bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = current_app.user_service.get_all_users()
        return jsonify(users_schema.dump(users))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = current_app.user_service.get_user_by_id(id)
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify({'error': 'Validation error', 'messages': errors}), 400

    try:
        user = current_app.user_service.update_user(id, name=data['name'])
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        current_app.user_service.delete_user(id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Product routes
@bp.route('/products', methods=['POST'])
def create_product():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
        
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify({'error': 'Validation error', 'messages': errors}), 400

    try:
        product = current_app.product_service.create(data)
        return jsonify(product_schema.dump(product)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/products', methods=['GET'])
def get_products():
    try:
        products = current_app.product_service.get_all()
        return jsonify(products_schema.dump(products))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    try:
        product = current_app.product_service.get_by_id(id)
        return jsonify(product_schema.dump(product))
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.get_json()
    try:
        product = current_app.product_service.update(id, data)
        return jsonify(product_schema.dump(product))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        current_app.product_service.delete(id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Purchase routes
@bp.route('/purchases', methods=['POST'])
def create_purchase():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
        
    data = request.get_json()
    errors = purchase_schema.validate(data)
    if errors:
        return jsonify({'error': 'Validation error', 'messages': errors}), 400

    try:
        purchase = current_app.purchase_service.create(data)
        return jsonify(purchase_schema.dump(purchase)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/purchases', methods=['GET'])
def get_purchases():
    try:
        purchases = current_app.purchase_service.get_all()
        return jsonify(purchases_schema.dump(purchases))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/purchases/<int:id>', methods=['GET'])
def get_purchase(id):
    try:
        purchase = current_app.purchase_service.get_by_id(id)
        return jsonify(purchase_schema.dump(purchase))
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/users/<int:user_id>/purchases', methods=['GET'])
def get_user_purchases(user_id):
    try:
        purchases = current_app.purchase_service.get_user_purchases(user_id)
        return jsonify(purchases_schema.dump(purchases))
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/purchases/<int:id>', methods=['DELETE'])
def delete_purchase(id):
    try:
        current_app.purchase_service.delete(id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404
