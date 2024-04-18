from marshmallow import Schema, fields, validates, ValidationError, post_load

from models import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    registration_time = fields.DateTime(dump_only=True)

    @post_load
    def create_user(self, data: dict) -> User:
        return User(**data)
