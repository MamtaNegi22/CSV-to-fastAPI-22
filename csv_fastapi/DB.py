from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="mysql+pymysql://root:root@localhost/student_db"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

#  Dependency (important for FastAPI)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
