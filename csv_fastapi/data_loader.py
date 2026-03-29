import pandas as pd
import numpy as np
from DB import SessionLocal
from models.models import Student

def load_data():
    """Insert CSV into DB only if table is empty."""
    db = SessionLocal()

    # ✅ Skip if data already exists
    existing = db.query(Student).first()
    if existing:
        print("Data already loaded. Skipping.")
        db.close()
        return

    data = pd.read_csv("students_complete.csv")
    data['gpa'] = data['gpa'].fillna(data['gpa'].mean())
    data = data.replace({np.nan: None})

    for _, row in data.iterrows():
        student = Student(
            student_id=row["student_id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            age=row["age"],
            major=row["major"],
            gpa=row["gpa"],
            attendance=row["attendance"],
            scholarship=row["scholarship"],
            city=row["city"],
            status=row["status"]
        )
        db.add(student)

    db.commit()
    db.close()
    print("Data inserted successfully!")