from tortoise import fields
from datetime import datetime
from passlib.hash import bcrypt
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, default='', unique=True)
    age = fields.IntField(default=0)
    password_hash = fields.CharField(128, default='')

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)


class Dogs(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, default='', unique=True)
    picture = fields.TextField()
    create_date = fields.DatetimeField(default=datetime.now())
    is_adopted = fields.BooleanField()
    user = fields.ForeignKeyField('models.User', related_name="user_id")
