from sqlalchemy.orm import backref

from app import db
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = 'Tickets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    date_of_creation = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('Dashboards.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    status = db.Column(
        db.Enum(
            'open', 'inProgress', 'review', 'test', 'closed', name='ticketProgressStatus'
        ),
        default='open'
    )

    creator = db.relationship('User', backref=backref('created_tickets', uselist=True), foreign_keys=[creator_id])
    assignee = db.relationship('User', backref=backref('assigned_tickets', uselist=True), foreign_keys=[assignee_id])
    dashboard = db.relationship('Dashboard', backref=backref('tickets', uselist=True), foreign_keys=[dashboard_id])

    __table_args__ = (
        db.CheckConstraint("title <> ''", name='valid_ticket'),
    )

    def __repr__(self):
        return f'<Ticket title={self.title} id={self.id}>'
