import datetime
import sqlalchemy as sa
from project.database import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime(timezone=False), default=datetime.datetime.utcnow)
    first_name = sa.Column(sa.String(255), nullable=False)
    last_name = sa.Column(sa.String(255), nullable=False)


class Post(db.Model):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255), nullable=False)
    body = sa.Column(sa.Text(), nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=False), default=datetime.datetime.utcnow)

    author_id = sa.Column(sa.Integer, sa.ForeignKey(Author.id))
    author = db.relationship(
        Author, foreign_keys=author_id, backref=db.backref('posts', lazy='dynamic'))
