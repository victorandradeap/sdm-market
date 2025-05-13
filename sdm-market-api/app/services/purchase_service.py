from app.extensions import db
from app.models.purchase import Purchase
from app.models.product import Product
from app.models.purchase_product import purchase_product, PurchaseProduct
from app.services.user_service import UserService
from app.services.product_service import ProductService
from app.api.errors import NotFoundError, ValidationError

class PurchaseService:
    def __init__(self, database=None, user_service=None, product_service=None):
        self.db = database or db
        self.user_service = user_service or UserService(database)
        self.product_service = product_service or ProductService(database)

    def get_all(self):
        # Carrega as compras com os produtos e detalhes
        purchases = Purchase.query.options(
            db.joinedload(Purchase.purchase_products).joinedload(PurchaseProduct.product)
        ).all()
        return purchases
    
    def get_by_id(self, purchase_id):
        purchase = Purchase.query.options(
            db.joinedload(Purchase.purchase_products).joinedload(PurchaseProduct.product)
        ).get(purchase_id)
        if not purchase:
            raise NotFoundError('Purchase not found')
        return purchase
    
    def get_user_purchases(self, user_id):
        purchases = Purchase.query.options(
            db.joinedload(Purchase.purchase_products).joinedload(PurchaseProduct.product)
        ).filter_by(user_id=user_id).all()
        return purchases
    
    def create(self, data):
        # Validar usuário
        user = self.user_service.get_user_by_id(data['user_id'])
        
        # Validar produtos e calcular total
        if not data.get('products'):
            raise ValidationError('Products list is required')
            
        total_amount = 0
        products = []
        
        for item in data['products']:
            product = self.product_service.get_by_id(item['product_id'])
            quantity = item.get('quantity', 1)
            
            if quantity <= 0:
                raise ValidationError('Quantity must be greater than 0')
                
            total_amount += product.price * quantity
            products.append({
                'product': product,
                'quantity': quantity,
                'unit_price': product.price
            })
        
        # Criar a compra
        purchase = Purchase(
            user_id=user.id,
            total_amount=total_amount
        )
        
        self.db.session.add(purchase)
        
        try:
            # Precisamos fazer commit primeiro para ter o ID da compra
            self.db.session.flush()
            
            # Adicionar produtos à compra - usar apenas a inserção explícita na tabela de junção
            for item in products:
                # NÃO fazer append diretamente, pois isso não inclui quantity e unit_price
                # purchase.products.append(item['product']) 
                
                # Criar uma instância PurchaseProduct e adicioná-la ao banco de dados
                purchase_product_item = PurchaseProduct(
                    purchase_id=purchase.id,
                    product_id=item['product'].id,
                    quantity=item['quantity'],
                    unit_price=item['unit_price']
                )
                self.db.session.add(purchase_product_item)
            
            self.db.session.commit()
            return purchase
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def delete(self, purchase_id):
        purchase = self.get_by_id(purchase_id)
        self.db.session.delete(purchase)
        try:
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e
