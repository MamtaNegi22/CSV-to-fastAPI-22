from sqlalchemy import create_engine, text
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

def db_connection_check():
    try:
        with engine.connect() as con:
            res=con.execute(text("SELECT 1"))
            print({"database":"connected", "result": str(res.fetchone())})
    except Exception as e:
        print(f"connection failed! {str(e)}")

