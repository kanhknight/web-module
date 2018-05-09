from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def index(weight,height):
# Body Mass Index
    height = height/100
    b = weight/(height**2)
    status = [
        "Severy underweight",
        "Underweight",
        "Normal",
        "Over Weight",
        "Obese"
    ]
    if b < 16:
       return render_template('index.html', status = status[0])
    elif b >= 16 and b <18.5:
        return render_template('index.html', status = status[1])
    elif b >= 18.5 and b < 25:
       return render_template('index.html', status = status[2])
    elif b >= 25 and b < 30:
        return render_template('index.html', status = status[3])
    else:
        return render_template('index.html', status = status[4])

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 