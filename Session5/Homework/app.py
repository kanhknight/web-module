from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bai2')
def bai2():
    return render_template('bai2.html')

@app.route('/bai1')
def bai1():
    return render_template('bai1.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 