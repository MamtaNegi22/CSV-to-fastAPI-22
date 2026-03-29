from pydantic import BaseModel
from typing import Optional

class StudentSchema(BaseModel):
    student_id: str
    first_name: Optional[str] = None
    last_name:  Optional[str] = None
    age:        Optional[int] = None
    major:      Optional[str] = None
    gpa:        Optional[float] = None
    attendance: Optional[float] = None
    scholarship:Optional[float] = None
    city:       Optional[str] = None
    status:     Optional[str] = None

    class Config:
        from_attributes = True   # ✅ lets Pydantic read SQLAlchemy objects