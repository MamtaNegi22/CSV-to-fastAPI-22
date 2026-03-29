import pandas as pd

 # global variable

# def load_data():
    
#     data = pd.read_csv("students_complete.csv")
#     data['gpa']=data['gpa'].fillna(data['gpa'].mean())
#     data = data.where(pd.notnull(data), None)
#     # print(data)
#     return data.to_dict(orient="records")

def load_data():
    data = pd.read_csv("students_complete.csv")
    data['gpa']=data['gpa'].fillna(data['gpa'].mean())
    return data