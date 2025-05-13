from datetime import datetime
from app.extensions import db
from app.models.purchase_product import purchase_product

class Purchase(db.Model):
    __tablename__ = 'purchases'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    products = db.relationship('Product', 
                             secondary=purchase_product, 
                             back_populates='purchases',
                             lazy='joined')
                             
    purchase_products = db.relationship('PurchaseProduct', 
                                     back_populates='purchase',
                                     lazy='joined')

    def __repr__(self):
        return f'<Purchase {self.id} by User {self.user_id}>'
