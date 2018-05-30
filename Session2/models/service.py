from mongoengine import StringField, IntField, BooleanField, Document
# Design database
# Create Collection

class Service(Document):
    name = StringField()
    yob  = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
