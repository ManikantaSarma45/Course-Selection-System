from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    academic_background = Column(Text)
    research_projects = Column(Text)
    patents = Column(Text)
