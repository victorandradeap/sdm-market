from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    purchases = fields.List(fields.Nested('PurchaseSchema', exclude=('products',)), dump_only=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
