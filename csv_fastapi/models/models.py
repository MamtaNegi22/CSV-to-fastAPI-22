from sqlalchemy import Column, Integer, Float, String
from DB import Base


class Student(Base):
    __tablename__="student_csv_table"
    student_id=Column(String(20),primary_key=True, index=True)
    first_name=Column(String(50), nullable=False)
    last_name=Column(String(50), nullable=True)
    age=Column(Integer, nullable=True)
    major=Column(String(100), nullable=True)
    gpa=Column(Float,nullable=True)
    attendance=Column(Float, nullable=True)
    scholarship=Column(Float, nullable=True)
    city=Column(String(50), nullable=True)
    status=Column(String(20), nullable=True)