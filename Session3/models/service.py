from mongoengine import *

class Service(Document):
    name = StringField()
    yob = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    image = StringField()
    description = StringField()
    measurements = ListField()