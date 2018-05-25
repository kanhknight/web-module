from mongoengine import *

class User(Document):
    name = StringField()
    username = StringField()
    password = StringField()
    email = StringField()
    phone = StringField()