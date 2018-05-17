from mongoengine import *

class Service(Document):
    image = StringField()
    description = StringField()
    measurements = ListField()