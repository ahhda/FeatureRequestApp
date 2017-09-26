from flask import Flask, jsonify, abort, request
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from forms import RequestForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    return render_template('request.html',
                           title='Home')

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
    old_requests = models.ClientRequest.query.filter_by(client_id=pr_id).order_by(desc(models.ClientRequest.priority))
    if not old_requests.first():
        return jsonify({'priorities': [{'id':1,'name':1}]})
    max_priority = old_requests.first().priority
    priorities = []
    for i in range(1, max_priority+2):
        priority = {'id':i, 'name':i}
        priorities.append(priority)
    return jsonify({'priorities': priorities})

@app.route('/api/all_requests/', methods=['GET'])
def get_requests():
    requests = models.ClientRequest.query.all()
    request_list = [request.as_dict() for request in requests]
    return jsonify({'requests': request_list})

@app.route('/api/request/', methods=['POST'])
def create_request():
    formData = request.form
    old_requests = db.session.query(models.ClientRequest).filter(models.ClientRequest.client_id==formData['client'],
        models.ClientRequest.priority>=int(formData['priority']))
    for old_request in old_requests:
        print old_request.as_dict()
        old_request.priority += 1
    form = models.ClientRequest(description=formData['description'], title=formData['title'], 
        client_id=int(formData['client']), priority=int(formData['priority']), 
        target_date=datetime.strptime(formData['date'],'%Y-%m-%d'),
        product_id=int(formData['product']))
    db.session.add(form)
    db.session.commit()
    flash(u'Request item was successfully created')
    print "Request added"
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)