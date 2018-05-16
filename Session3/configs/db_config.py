import mongoengine

host = "ds219100.mlab.com"
port = 19100
db_name = "pilot_app"
user_name = "mlab_admin"
password = "mlab_admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)