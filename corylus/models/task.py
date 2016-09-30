from sqlalchemy import Column, Integer, String, TIMESTAMP

from corylus.database import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(36))
    name = Column(String(50))
    status = Column(Integer, default=0)
    target_url = Column(String(200))
    created_at = Column(Integer)

    def __init__(self, name=None, target_url=None, file_id=None, created_at=None, status=0):
        self.name = name
        self.file_id = file_id
        self.status = status
        self.target_url = target_url
        self.created_at = created_at

    def __repr__(self):
        return '<Task %r>' % (self.name or self.file_id)
