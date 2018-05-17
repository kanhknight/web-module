from mongoengine import *
from flask import *
from jinja2 import *
from models.service import Service
from controllers.remove_service import xoa
from models.populate import populate

connect()
# xoa()
# populate()
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html', all_service = all_service)

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def capnhat(service_id):
    capnhatdv = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('/update_service.html', capnhatdv = capnhatdv)
    elif request.method == 'POST':
        form_data = request.form
        name = form_data['name']
        yob = form_data['yob']
        capnhatdv.update(set__name = name, set__yob = yob)
        capnhatdv.reload()
        return redirect('/admin')

@app.route('/detail/<id_chitiet>')
def detail(id_chitiet):
    chitiet = Service.objects.with_id(id_chitiet)
    return render_template('detail.html', detail = chitiet)

@app.route('/create-service', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('add_service.html')
    elif request.method == 'POST':
        form_data = request.form
        image = form_data['image']
        name = form_data['name']
        yob = form_data['yob']
        height = form_data['height']
        phone = form_data['phone']
        address = form_data['address']
        description = form_data['description']
        measurements = [form_data['measure1'], form_data['measure2'], form_data['measure3']]
        if form_data['gender'] == 'male':
            gender = 1
        elif form_data['gender'] == 'female':
            gender = 0
        new_service = Service(
            name = name, 
            yob = yob, 
            height = height, 
            phone = phone, 
            address = address, 
            description = description, 
            measurements = measurements, 
            gender = gender,
            image = image
            )
        new_service.save()
    return redirect('/service')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 

