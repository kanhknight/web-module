from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contacted = IntField()