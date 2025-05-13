from app.extensions import db

# Mantém a tabela para compatibilidade com código existente
purchase_product = db.Table('purchase_product',
    db.Column('purchase_id', db.Integer, db.ForeignKey('purchases.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False),
    db.Column('unit_price', db.Float, nullable=False)  # Preço no momento da compra
)

# Modelo ORM para a mesma tabela, permitindo acesso aos campos
class PurchaseProduct(db.Model):
    __tablename__ = 'purchase_product'
    
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    
    # Relacionamentos
    purchase = db.relationship('Purchase', back_populates='purchase_products')
    product = db.relationship('Product')
    
    def __repr__(self):
        return f'<PurchaseProduct {self.purchase_id}-{self.product_id}>'
