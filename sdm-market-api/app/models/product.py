from datetime import datetime
from app import db
from .purchase_product import purchase_product

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    purchases = db.relationship('Purchase', 
                              secondary=purchase_product,
                              back_populates='products')

    def __repr__(self):
        return f'<Product {self.name}>'
