from marshmallow import Schema, fields, ValidationError, post_load, validates
from models import User


# Не использовал потому что забыл как

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    registration_time = fields.DateTime(dump_only=True)

    @post_load
    def create_user(self, data: dict) -> User:
        return User(**data)

    @validates('email')
    def validate_email(self, email):
        existing_user = User.query.filter(User.email == email).first()
        if existing_user is not None and existing_user.id != self.id:
            raise ValidationError(f'User with email "{email}" already exists!')
        return email

    @validates('username')
    def validate_username(self, username):
        existing_user = User.query.filter(User.username == username).first()
        if existing_user is not None and existing_user.id != self.id:
            raise ValidationError(f'User with username "{username}" already exists!')
        return username
