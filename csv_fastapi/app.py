from fastapi import FastAPI
from routes import router
from data_loader import load_data
from models.models import *
from sqlalchemy.orm import session
from sqlalchemy import text
from DB import engine, Base

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    load_data()   # load once

@app.get("/db-test")
def test_db():
    try:
        with engine.connect() as con:
            result=con.execute(text("SELECT 1"))
            return {"database": "connected",
            "result": str(result.fetchone())
            }
    except Exception as e:
        return str(e)


app.include_router(router)