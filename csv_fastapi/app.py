from fastapi import FastAPI
from routes import router
from data_loader import load_data

import models

from sqlalchemy.orm import session
from DB import engine, SessionLocal, Base

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    load_data()   # load once

app.include_router(router)