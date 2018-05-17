from mongoengine import *
from flask import *
from jinja2 import *
from mlab import connect
connect()

from flask import Flask, render_template
app = Flask(__name__)

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/africa')
def africa():
    continent = "Africa"
    all_river = River.objects(continent = continent)
    return render_template('river.html', all_river = all_river, continent = continent)
@app.route('/america')
def america():
    continent = "S. America"
    all_river = River.objects(continent = continent, length__gt = 1000)
    return render_template('river.html', all_river = all_river, continent = continent)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
