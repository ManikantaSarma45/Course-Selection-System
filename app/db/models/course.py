from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    course_type = Column(String, nullable=False)  # "Theory" or "Lab"
