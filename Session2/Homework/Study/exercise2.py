import mongoengine
from mongoengine import StringField, IntField, BooleanField, Document
# Design database
# Create Collection
# mongodb://<dbuser>:<dbpassword>@ds219100.mlab.com:19100/pilot_app
host = "ds219100.mlab.com"
port = 19100
db_name = "pilot_app"
user_name = "mlab_admin"
password = "mlab_admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
connect()

class Service(Document):
    name = StringField()
    yob  = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

def remove_document(id_revmove):
    Service.objects(id = "{0}".format(id_revmove)).delete()

all_service = Service.objects() # Có thể filter dữ liệu tại đây !

fist_service = all_service[0]

def nine_item():
    for index, service in enumerate(all_service):
        print(service["id"])
        print(service["name"])
        print(service["yob"])
        print(service["gender"])
        print(service["height"])
        print(service["phone"])
        print(service["address"])
        print(service["status"])
        print()
        if index == 9:
            break
nine_item()
remove_choice = input("Nhập vào ID muốn xóa: ")
remove_document(remove_choice)