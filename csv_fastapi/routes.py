from fastapi import APIRouter, Path, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
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

# ✅ Fetch all students from DB and sort
@router.get("/sort-students", response_model=List[StudentSchema])
def sort_student(db:Session=Depends(get_db), sort_by:str=Query(description="sort on the basis of gpa, attendance or scholarship"), order:str=Query('asc', description="")):

    valid_sort_fields=["gpa","attendance", "scholarship"]

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field! select one from {valid_sort_fields}")

    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail=f"Invalid order! select asc or desc")

    # one way to sort
    # students=db.query(Student).all()
    # sort_order=True if order=="desc"else False
    # sorted_students=sorted(students,key= lambda x: getattr(x, sort_by) or 0, reverse=sort_order)

    # return sorted_students

    # another and the better/faster way to do sorting  
    column = getattr(Student, sort_by)           # ✅ gets the actual SQLAlchemy column
    order_func = desc(column) if order == "desc" else asc(column)

    students = db.query(Student).order_by(order_func).all()  # ✅ DB sorts, not Python
    return students



@router.get("/student-details/{student_id}", response_model=StudentSchema)
def get_student(student_id: str, db:Session=Depends(get_db)):

    student=db.query(Student).filter(Student.student_id==student_id).first()  # DataFrame


    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
