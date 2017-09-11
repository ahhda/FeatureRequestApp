from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.title)

class ClientRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime)
    url = db.Column(db.Text)
    product_id = db.Column(db.Integer)

    def __init__(self, id, title, description, client_id, priority,target_date,url,product_id):
        self.id = id
        self.title = title
        self.description = description
        self.client_id = client_id
        self.priority = priority
        self.target_date = target_date
        self.url = url
        self.product_id = product_id

    def __repr__(self):
        return '<Request title %r>' % (self.title)