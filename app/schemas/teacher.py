from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    academic_background: str
    research_projects: str
    patents: str

class TeacherResponse(TeacherCreate):
    id: int

    class Config:
        orm_mode = True
