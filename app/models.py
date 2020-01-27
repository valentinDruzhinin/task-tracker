from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    created_dashboards = db.relationship('Dashboard', backref='creator')
    created_tickets = db.relationship(
        lambda: Ticket, foreign_keys=lambda: Ticket.creator_id, back_populates='creator'
    )
    assigned_tickets = db.relationship(
        lambda: Ticket, foreign_keys=lambda: Ticket.assignee_id, back_populates='assignee'
    )

    __table_args__ = (
        db.CheckConstraint('name <> "" and email <> "" and password <> ""', name='valid_user'),
    )

    def __repr__(self):
        return f'<User name={self.name} email={self.email} id={self.id}>'


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

    creator = db.relationship(User, foreign_keys=creator_id, back_populates='created_tickets')
    assignee = db.relationship(User, foreign_keys=assignee_id, back_populates='assigned_tickets')

    __table_args__ = (
        db.CheckConstraint("title <> ''", name='valid_ticket'),
    )

    def __repr__(self):
        return f'<Ticket title={self.title} id={self.id}>'


class Dashboard(db.Model):
    __tablename__ = 'Dashboards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    date_of_creation = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    tickets = db.relationship('Ticket', backref='dashboard')

    def __repr__(self):
        return f'<DashboardNode name={self.name} id={self.id}>'
