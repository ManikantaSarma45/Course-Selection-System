from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.routes import students, teachers, courses, feedback, admin

# Initialize FastAPI
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(students.router, prefix="/students")
app.include_router(teachers.router, prefix="/teachers")
app.include_router(courses.router, prefix="/courses")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(admin.router, prefix="/admin")
