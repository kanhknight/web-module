from mongoengine import *

class Order(Document):
    userid = StringField()
    accepted = BooleanField()
    timeorder = DateTimeField()