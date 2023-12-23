from app import db

class Main(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    street = db.Column(db.String(255))
    house = db.Column(db.String(10))
    building = db.Column(db.String(10))
    apartment = db.Column(db.String(10))
    phone = db.Column(db.String(15))

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))

    main_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    main = db.relationship('Main', backref='names')

class LastName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))

    main_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    main = db.relationship('Main', backref='last_names')

class MiddleName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))

    main_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    main = db.relationship('Main', backref='middle_names')

class Street(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))

    main_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    main = db.relationship('Main', backref='streets')
