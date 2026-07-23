from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    group_name = db.Column(db.String(50))

    image = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=db.func.now())