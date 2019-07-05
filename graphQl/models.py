from mongoengine import Document, StringField, IntField


class User(Document):
    meta = {'collection': 'users'}
    name = StringField
    age = IntField
    email = StringField
    number = StringField
