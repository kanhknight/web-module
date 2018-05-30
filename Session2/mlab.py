import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds219100.mlab.com:19100/pilot_app

host = "ds219100.mlab.com"
port = 19100
db_name = "pilot_app"
user_name = "mlab_admin"
password = "mlab_admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())