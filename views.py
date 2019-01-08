from flask import render_template
from flask import request
from ManagerApp.app import app


@app.route('/')
def index():
    name = request.args.get('name')
    if not name:
        name = '<unknown>'
    return render_template('homepage.html', nombre=name)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        pass

