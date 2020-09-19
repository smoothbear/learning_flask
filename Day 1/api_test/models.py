from api_test import db


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
