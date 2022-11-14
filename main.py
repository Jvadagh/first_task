from fastapi import FastAPI
from DB_Tables import TblStudents
from DB_Tables import TblCourses
from DB_Tables import TblSelectedCourse

app = FastAPI()
app.include_router(TblStudents.router)
app.include_router(TblCourses.router)
app.include_router(TblSelectedCourse.router)
