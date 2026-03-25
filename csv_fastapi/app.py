from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return "Welcome to the FastAPI...we will fetch the data from CSV FILE"

@app.get("/about")
def about():
    return "here you will get the data from the csv file"