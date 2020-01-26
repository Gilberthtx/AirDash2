from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from peewee import *

# create database
DATABASE = SqliteDatabase('app.db')


'''MODEL FOR USER'''


class User(UserMixin, Model):
    # inputs needed to create a user account
    email = CharField(unique=True)
    password = CharField(max_length=100)

    # assigning the database to this class
    class Meta:
        database = DATABASE

    # method to create user account
    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password)
                )
        # expects that an error could occur if user exists
        except IntegrityError:
            raise ValueError("User already exists")


'''INITIALIZE DATABASE'''


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
