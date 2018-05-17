import mongoengine

host = "ds021182.mlab.com"
port = 21182
db_name = "c4e"
user_name = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)