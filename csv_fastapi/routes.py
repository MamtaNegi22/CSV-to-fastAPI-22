from fastapi import APIRouter, Path, Depends, HTTPException
from sqlalchemy.orm import Session
from DB import get_db
from models.models import Student

from schemas import StudentSchema        # ✅ import schema
from typing import List

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@router.get("/about")
def about():
    return {"message": "Fetch data from CSV"}

# ✅ Fetch all students from DB
@router.get("/view", response_model=List[StudentSchema])
def view(db:Session=Depends(get_db)):
    students=db.query(Student).all()
    return students


@router.get("/student-details/{student_id}", response_model=StudentSchema)
def get_student(student_id: str, db:Session=Depends(get_db)):

    student=db.query(Student).filter(Student.student_id==student_id).first()  # DataFrame


    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
