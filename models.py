from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.title)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Client %r>' % (self.name)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product %r>' % (self.name)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class ClientRequest(db.Model):
    __tablename__ = 'client_request'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime)
    product_id = db.Column(db.Integer)

    def __init__(self, title, description, client_id, priority,target_date,product_id):
        self.title = title
        self.description = description
        self.client_id = client_id
        self.priority = priority
        self.target_date = target_date
        self.product_id = product_id

    def __repr__(self):
        return '<Request title %r>' % (self.title)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}