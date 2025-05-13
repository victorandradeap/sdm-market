from app import db
from app.models.product import Product
from app.api.errors import NotFoundError, ValidationError

class ProductService:
    def __init__(self, database=None):
        self.db = database or db

    def get_all(self):
        return Product.query.all()
    
    def get_by_id(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            raise NotFoundError('Product not found')
        return product
    
    def create(self, data):
        if not data.get('name') or not data.get('price'):
            raise ValidationError('Name and price are required')
            
        product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price']
        )
        
        self.db.session.add(product)
        try:
            self.db.session.commit()
            return product
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def update(self, product_id, data):
        product = self.get_by_id(product_id)
        
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
            
        try:
            self.db.session.commit()
            return product
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def delete(self, product_id):
        product = self.get_by_id(product_id)
        self.db.session.delete(product)
        try:
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e
