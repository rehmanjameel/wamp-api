from marshmallow import fields, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AccountSchema(SQLAlchemyAutoSchema):
    fullname = fields.Str()
    age = fields.Int()
    email = fields.Email()

    @validates('age')
    def validate_age(self, age):
        if age > 100:
            raise ValidationError('Age is too old')
        elif 0 > age < 10:
            raise ValidationError('Age is too young')
        elif age < 0:
            raise ValidationError('Invalid age')
