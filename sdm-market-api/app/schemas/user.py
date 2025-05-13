from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    purchases = fields.List(fields.Nested('PurchaseSchema', exclude=('user',)), dump_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)