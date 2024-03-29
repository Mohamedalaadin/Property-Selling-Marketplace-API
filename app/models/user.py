from enum import Enum, unique
from app import db

# Define the UserRole enum
@unique
class UserRole(Enum):
    PROPERTY_OWNER = 'PropertyOwner'
    BUYER = 'Buyer'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    mobile = db.Column(db.String(32))
    role = db.Column(db.Enum(UserRole))

    properties = db.relationship('Property', back_populates='owner')
