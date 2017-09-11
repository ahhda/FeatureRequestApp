from flask import Flask, jsonify, abort, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from forms import RequestForm
from datetime import datetime


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models

clients = [
    {
        'id': 1,
        'name': u'Client1',
    },
    {
        'id': 2,
        'name': u'Client2',
    }
]

products = [
    {
        'id': 1,
        'name': u'Android App',
    },
    {
        'id': 2,
        'name': u'iPhone App',
    },
    {
        'id': 3,
        'name': u'Web App',
    }
]

priorities = [
    {
        'id': 1,
        'name': u'prior1',
    },
    {
        'id': 2,
        'name': u'prior2',
    }
]

@app.route('/')
def hello_world():
    user = {'nickname': 'Miguel'}  # fake user
    form = RequestForm()
    return render_template('request.html',
                           title='Home',
                           form=form)

@app.route('/hello/')
def hello():
    return 'Hello, World'

@app.route('/api/clients/', methods=['GET'])
def get_clients():
    return jsonify({'clients': clients})

@app.route('/api/products/', methods=['GET'])
def get_products():
    return jsonify({'products': products})

@app.route('/api/priorities/<int:pr_id>', methods=['GET'])
def get_priorities(pr_id):
    priority = [priority for priority in priorities if priority['id'] == pr_id]
    return jsonify({'priorities': priority[0]})

@app.route('/api/request/', methods=['POST'])
def create_request():
    # if not request.json:
    #     abort(400)
    formData = request.form
    form = RequestForm(description=formData['description'], title=formData['title'], 
        client_id=int(formData['client']), priority=int(formData['priority']), url=formData['url'], 
        target_date=datetime.strptime(formData['date'],'%Y-%m-%d'),
        product_id=int(formData['product']))
    if form.validate() == False:
        print "FALSE"
        print form.errors
    else:
        print "TRUE"
    print request.method
    print "HELLLOO\n\n"
    print request.data
    print "HELLLOO\n\n"
    print request.form
    print "HELLLOO\n\n"
    print request.form['description']
    print request.form['date']
    print "HELLLOO\n\n"
    return jsonify({}), 201

if __name__ == "__main__":
    app.run(debug=True)