from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    salary = Column(String, nullable=True)
    state = Column(String, nullable=True)
    local = Column(String, nullable=True)
    level = Column(String, nullable=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)

    def __repr__(self):
        return f'Name: {self.name}'