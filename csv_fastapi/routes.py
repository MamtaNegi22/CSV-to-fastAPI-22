from fastapi import APIRouter, Path
from data_loader import load_data   # import preloaded data

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@router.get("/about")
def about():
    return {"message": "Fetch data from CSV"}

@router.get("/view")
def view():
    data=load_data()
    return data.to_dict(orient="records")


@router.get("/student-details/{student_id}")
def get_student(student_id: str):

    data = load_data()   # DataFrame

    student = data[data["student_id"] == student_id]

    if student.empty:
        return {"message": "Student not found"}

    return student.to_dict(orient="records")
