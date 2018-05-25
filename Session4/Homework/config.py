# mongodb://<dbuser>:<dbpassword>@ds135290.mlab.com:35290/warmwinter
import mongoengine

host = "ds135290.mlab.com"
port = 35290
db_name = "warmwinter"
username = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)