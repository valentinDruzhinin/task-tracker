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
