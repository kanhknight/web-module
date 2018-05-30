from flask import *
from jinja2 import *
from mongoengine import StringField, IntField, BooleanField, Document
import mlab
from models.service import Service

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/delete/<service_id>')
def delete_document(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Không tìm thấy bản ghi!"


@app.route('/new-service', methods = ['GET','POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form_data = request.form
        name = form_data['name']
        yob = form_data['yob']

        # Lưu lại database vào csdl
        new_service = Service(name = name, yob = yob)
        new_service.save()
        return redirect(url_for('admin'))


@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(
        gender = g, 
        yob__lte = 2000, # Toán tử so sánh trong truy vấn mongoengine
        address__contains = "Hà Nội", 
        id = "5af5a7739f880b0d90e126ae"
        ) # Lọc dữ liệu ngay tại đây cũng đc 
    return render_template(
        'search.html',
        all_service = all_service
        )

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)