from app.extensions import db

purchase_product = db.Table('purchase_product',
    db.Column('purchase_id', db.Integer, db.ForeignKey('purchases.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False),
    db.Column('unit_price', db.Float, nullable=False)  # Preço no momento da compra
)
