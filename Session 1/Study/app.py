from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def index():
    about = {
        "Name":"Vũ Viết Cảnh",
        "Work": "IT Project Management",
        "School": "Techkids",
        "Hobbies": "Movies, Travel, Coding..",
        "Status": "Get Married",
        "Child": "2 Daughter"
    }
    return render_template('index.html',about = about)

@app.route('/school')
def chuyentrang():
    return redirect('http://techkids.vn', code = 302)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
