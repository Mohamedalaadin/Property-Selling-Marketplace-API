from enum import Enum, unique
from app import db

@unique
class PropertyStatus(Enum):
    AVAILABLE = 'available'
    SOLD = 'sold'
    UNAVAILABLE = 'unavailable'

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    num_rooms = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(PropertyStatus))

    # Relationship to link back to the owner
    owner = db.relationship('User', back_populates='properties')

    def to_dict(self):
        """
        Convert the Property object to a dictionary format, suitable for JSON serialization.
        """
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'location': self.location,
            'num_rooms': self.num_rooms,
            'price': self.price,
            'status': self.status.value if self.status else None  # Convert Enum to string
        }