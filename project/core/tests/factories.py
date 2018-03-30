import factory
import factory.faker
import factory.fuzzy
from factory.alchemy import SQLAlchemyModelFactory
from project.database import db
from .. import models


class AuthorFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Author
        sqlalchemy_session = db.session

    first_name = factory.faker.Faker('name')
    last_name = factory.faker.Faker('name')


class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Post
        sqlalchemy_session = db.session

    author = factory.SubFactory(AuthorFactory)
    title = factory.fuzzy.FuzzyText(length=25)
    body = factory.fuzzy.FuzzyText(length=400)
