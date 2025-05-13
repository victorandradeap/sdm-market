from marshmallow import Schema, fields

class PurchaseProductSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    unit_price = fields.Float(required=True)
    product = fields.Nested('ProductSchema', only=('name', 'price'), dump_only=True)
