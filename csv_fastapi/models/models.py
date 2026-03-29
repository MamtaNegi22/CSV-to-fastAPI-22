from sqlalchemy import Column, Integer, Float, String
from DB import Base


class Student(Base):
    __tablename__="student_csv_table"
    student_id=Column(String(10),primary_key=True, index=True)
    first_name=Column(String(50), nullable=False)
    last_name=Column(String(50))
    age=Column(Integer)
    major=Column(String(15))
    gpa=Column(Float)
    attendance=Column(Float)
    scholarship=Column(Float)
    city=Column(String(50))
    status=Column(String(10))