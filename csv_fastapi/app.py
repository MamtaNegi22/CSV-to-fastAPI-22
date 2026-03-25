from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return "Welcome to the FastAPI...we will fetch the data from CSV FILE"

