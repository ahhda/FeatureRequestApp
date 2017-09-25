from flask import Flask, jsonify, abort, request
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RequestForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models


#This should come from db
clients = [
    {
        'id': 1,
        'name': u'Client1',
    },
    {
        'id': 2,
        'name': u'Client2',
    },
    {
        'id': 5,
        'name': u'Client5',
    }
]

products = [
    {
        'id': 1,
        'name': u'Policies',
    },
    {
        'id': 2,
        'name': u'Billing',
    },
    {
        'id': 3,
        'name': u'Claims',
    },
    {
        'id': 5,
        'name': u'Reports',
    }
]

#Get priorities according to client
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
    clients = models.Client.query.all()
    clients_list = [client.as_dict() for client in clients]
    return jsonify({'clients': clients_list})

@app.route('/api/products/', methods=['GET'])
def get_products():
    products = models.Product.query.all()
    products_list = [product.as_dict() for product in products]
    return jsonify({'products': products_list})

@app.route('/api/priorities/<int:pr_id>', methods=['GET'])
def get_priorities(pr_id):
    priority = [priority for priority in priorities if priority['id'] == pr_id]
    if not priority:
        return jsonify({})
    return jsonify({'priorities': priority[0]})

@app.route('/api/all_requests/', methods=['GET'])
def get_requests():
    requests = models.ClientRequest.query.all()
    request_list = [request.as_dict() for request in requests]
    return jsonify({'requests': request_list})

@app.route('/api/request/', methods=['POST'])
def create_request():
    # if not request.json:
    #     abort(400)
    formData = request.form
    form = models.ClientRequest(description=formData['description'], title=formData['title'], 
        client_id=int(formData['client']), priority=int(formData['priority']), 
        target_date=datetime.strptime(formData['date'],'%Y-%m-%d'),
        product_id=int(formData['product']))
    # if form.validate() == False:
    #     print "FALSE"
    #     print form.errors
    # else:
    print "TRUE"
    db.session.add(form)
    db.session.commit()
    flash(u'Request item was successfully created')
    print "Request added"
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.run(debug=True)