from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Text

from server.config import db


class PostModel(db.Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String(255))
    body = Column(Text(50000))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.userId,
            'title': self.title,
            'body': self.body,
        }
