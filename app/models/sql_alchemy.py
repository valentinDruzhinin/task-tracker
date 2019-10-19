from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    __table_args__ = (
        db.CheckConstraint('name <> "" and email <> "" and password <> ""', name='valid_user'),
    )

    def __repr__(self):
        return f'<User name={self.name} email={self.email} id={self.id}>'


class DashboardToUser(db.Model):
    __tablename__ = 'DashboardToUser'

    id = db.Column(db.Integer, primary_key=True)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('Dashboards.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    role = db.Column(
        db.Enum('admin', 'write', 'read', name='userRole'),
        nullable=False
    )

    user = db.relationship('User', backref='authorized_dashboards')
    dashboard = db.relationship('Dashboard', backref='authorized_users')

    __table_args__ = (
        db.UniqueConstraint('dashboard_id', 'user_id'),
    )

    def __repr__(self):
        return f'<DashboardToUser dashboard_id={self.dashboard_id} user_id={self.user_id} id={self.id}>'


class Dashboard(db.Model):
    __tablename__ = 'Dashboards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    date_of_creation = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    creator = db.relationship('User', backref='created_dashboards')

    def __repr__(self):
        return f'<Dashboard name={self.name} id={self.id}>'


class Ticket(db.Model):
    __tablename__ = 'Tickets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    date_of_creation = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('Dashboards.id'), nullable=False)
    assignee = db.Column(db.Integer, db.ForeignKey('Users.id'))
    status = db.Column(
        db.Enum(
            'open', 'inProgress', 'review', 'test', 'closed', name='ticketProgressStatus'
        ),
        default='open'
    )

    creator = db.relationship('User', backref='created_tickets', foreign_keys=[creator_id])
    dashboard = db.relationship('Dashboard', backref='tickets', foreign_keys=[dashboard_id])

    __table_args__ = (
        db.CheckConstraint("title <> ''", name='valid_ticket'),
    )

    def __repr__(self):
        return f'<Ticket title={self.title} id={self.id}>'
