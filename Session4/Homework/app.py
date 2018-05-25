from flask import *
from jinja2 import *
import config
from mongoengine import *
from models.user import User
config.connect()

app = Flask(__name__)
app.secret_key = "day la chuoi bi mat duoc khai bao de su dung voi session dang nhap"

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('user-login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("welcome"))
        else:
            return redirect(url_for("signup"))

@app.route('/sign-in',  methods = ['GET', 'POST'])
def signin():
    if request.method == "GET":
        return render_template('user-login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("welcome"))
        else:
            return redirect(url_for("signup"))

@app.route('/register', methods = ['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('user-register.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        username = form['username']
        email = form['email']
        phone = form['phone']
        password = form['password']

        new_user = User(
            name = name,
            username = username,
            email = email,
            phone = phone,
            password = password
        )
        new_user.save()
        return redirect('/success')

@app.route('/success')
def success():
    return "Register Success!"


@app.route('/welcome')
def welcome():
    if "loggedin" in session:
        return "Helooooo"
    else:
        return redirect(url_for("signin"))

@app.route('/logout')
def logout():
    if session['loggedin'] == True:
        del session['loggedin']
        return redirect(url_for("welcome"))
    else:
        return "What are you doing !"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=False)
 