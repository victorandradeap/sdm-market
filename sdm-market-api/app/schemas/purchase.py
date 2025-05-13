from marshmallow import Schema, fields
from .purchase_product import PurchaseProductSchema

class PurchaseSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    purchase_date = fields.DateTime(dump_only=True)
    total_amount = fields.Float(required=False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema', exclude=('purchases',), dump_only=True)
    products = fields.List(fields.Nested(PurchaseProductSchema), required=True)
    
    # Adicionar os produtos com detalhes da compra (quantidade e preço unitário)
    purchase_products = fields.List(fields.Nested(PurchaseProductSchema), dump_only=True)

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)
