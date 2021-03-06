from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db
# from api.app import ma

class User(db.Model):
    __tablename__ = 't_productgazou'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, image=''):
        self.image = image
        
    @classmethod
    def getUserInfo(cls, user_id):
        record = cls.query.filter_by(id=user_id).first()
        return {
            'id': record.id,
            'image': record.image,
            'display_name': record.display_name
        }

