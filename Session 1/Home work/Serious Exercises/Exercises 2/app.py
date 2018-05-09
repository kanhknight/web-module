from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    Users = {
        "canh":{
            "name":"Vu Viet Canh",
            "age":30,
            "status":"Get married",
            "hobbies":"Codding" 
        },
        "tuananh":{
            "name":"Nguyen Tuan Anh",
            "age":20,
            "status":"Alone",
            "hobbies":"Traveling" 
        },
        "huy":{
            "name":"Nguyen Huy",
            "age":26,
            "status":"Alone",
            "hobbies":"Reading" 
        }
    }
    if username in Users.keys():
        return render_template('index.html', users = Users[username])
    else:
        return render_template('notfound.html', user = username)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 