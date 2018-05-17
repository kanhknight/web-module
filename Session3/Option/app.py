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

@app.route('/africa')
def africa():
    all_river = River.objects(continent = "Africa")
    return render_template('river.html', all_river = all_river)
@app.route('/america')
def america():
    all_river = River.objects(continent = "S. America", length__gt = 1000)
    return render_template('river.html', all_river = all_river)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
