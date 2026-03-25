from fastapi import FastAPI
import pandas as pd

app=FastAPI()

# -----------data_load------------------

def load_data():
    with open("students_complete.csv","r") as f:
        data=pd.read_csv(f)
    return data

@app.get("/")
def home():
    return "Welcome to the FastAPI...we will fetch the data from CSV FILE"

@app.get("/about")
def about():
    return "here you will get the data from the csv file"

@app.get("/view")
def view():
    data=load_data()
    return data.to_json(orient="records")
# to_dict se nhi hoga - Pandas converts structure → but NOT always datatypes
# to_json will work - Pandas converts everything into a JSON string