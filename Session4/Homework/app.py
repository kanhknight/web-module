from flask import *
from jinja2 import *
from datetime import *
import config
from mongoengine import *
from models.user import User
from models.order import Order
config.connect()

app = Flask(__name__)
app.secret_key = "day la chuoi bi mat duoc khai bao de su dung voi session dang nhap"

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        all_user = User.objects()
        return render_template('index.html', all_user = all_user)
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
        all_user = User.objects()
        form = request.form
        username = form['username']
        password = form['password']
        for user in all_user:
            if username == user.username and password == user.password:
                session['loggedin'] = True
                return redirect('/')
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
    return redirect('/')


@app.route('/welcome')
def welcome():
    if "loggedin" in session:
        return "Helooooo"
    else:
        return redirect(url_for("signin"))

@app.route('/service_detail/<user_id>')
def service_detail(user_id):
    if "loggedin" in session:
        detail = User.objects.with_id(user_id)
        return render_template('service-detail.html', detail = detail)
    else:
        return redirect('/sign-in')


@app.route('/logout')
def logout():
    if session['loggedin'] == True:
        del session['loggedin']
        return redirect(url_for("welcome"))
    else:
        return "What are you doing !"

@app.route('/request_service/<user_id>')
def request_service(user_id):
    new_order = Order(
        userid = user_id,
        accepted = False,
        timeorder = datetime.now()
    )
    new_order.save()
    return "Requested!"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 