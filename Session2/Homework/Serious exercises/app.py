from flask import *
from configs.database import connect
from models.customer import Customer
from models.populate_customer import khoi_tao

#  Kết nối database
connect()

# Khởi tạo customer 
# khoi_tao()

# Khởi tạo server
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def show_10_male():
    show_male = Customer.objects(gender = 1, contacted = 0)
    show_male = show_male[:10]
    return render_template('index.html', show_male = show_male)

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
