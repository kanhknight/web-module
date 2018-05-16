from mongoengine import *
from models.service import Service
from controllers.remove_service import xoa

connect()
xoa()
