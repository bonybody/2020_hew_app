from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma


class RemainingFormat(db.Model):
    __tablename__ = 'remaining_format'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    item = db.relationship('Item', backref='remaining_format')

    def __init__(self, name=''):
        self.name = name

    def setAttr(self, name=''):
        self.name = name

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def getRecord(cls, category_id):
        record = cls.query.filter_by(id=category_id).first()
        return record

    @classmethod
    def addTestData(cls):
        models = []
        data_lists = ['whole', 'day', 'week', 'month']
        for data in data_lists:
            models.append(cls(data))

        db.session.add_all(models)
        db.session.commit()
# class RemainingFormatSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = RemainingFormat

