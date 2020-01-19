from sqlalchemy.orm import backref
from app import db
from datetime import datetime


class Dashboard(db.Model):
    __tablename__ = 'Dashboards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    date_of_creation = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    creator = db.relationship('User', backref=backref(
        "created_dashboards", uselist=True
    ))

    def __repr__(self):
        return f'<Dashboard name={self.name} id={self.id}>'

