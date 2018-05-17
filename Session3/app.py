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


@app.route('/service')
def index():
    all_service = Service.objects()
    return render_template('service.html', all_service = all_service)
@app.route('/detail/<id_chitiet>')
def detail(id_chitiet):
    chitiet = Service.objects.with_id(id_chitiet)
    return render_template('detail.html', detail = chitiet)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 

